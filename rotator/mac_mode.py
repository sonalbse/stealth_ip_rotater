import subprocess
import random
from rich.console import Console

console = Console()

class MACRotator:
    iface = "eth0"  # Change to wlan0 for WiFi

    def random_mac(self):
        return "02:00:%02x:%02x:%02x:%02x" % (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

    def randomize(self):
        mac = self.random_mac()
        console.print(f"[cyan]New MAC: {mac}[/cyan]")

        subprocess.run(["sudo", "ip", "link", "set", self.iface, "down"])
        subprocess.run(["sudo", "ip", "link", "set", self.iface, "address", mac])
        subprocess.run(["sudo", "ip", "link", "set", self.iface, "up"])

        console.print("[green]MAC Address changed successfully![/green]")
