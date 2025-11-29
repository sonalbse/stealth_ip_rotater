import subprocess
from rich.console import Console

console = Console()

class VPNRotator:
    def __init__(self):
        self.vpn_profiles = ["vpn1", "vpn2"]  # nmcli connection names

    def rotate(self):
        console.print("[yellow]Rotating VPN...[/yellow]")

        for vpn in self.vpn_profiles:
            try:
                subprocess.run(["sudo", "nmcli", "connection", "down", vpn])
            except:
                pass

        try:
            subprocess.run(["sudo", "nmcli", "connection", "up", self.vpn_profiles[0]])
            console.print("[green]VPN reconnected with new IP![/green]")
        except Exception as e:
            console.print(f"[red]VPN error: {e}[/red]")
