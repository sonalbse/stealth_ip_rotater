import subprocess
from stem import Signal
from stem.control import Controller
from .ipchecker import IPChecker
from rich.console import Console

console = Console()

class TorRotator:

    def rotate(self):
        try:
            console.print("[yellow]Requesting new Tor identity...[/yellow]")

            with Controller.from_port(port=9051) as controller:
                controller.authenticate()
                controller.signal(Signal.NEWNYM)

            console.print("[green]Tor IP rotated successfully![/green]")
            console.print(f"New Tor Exit IP: {IPChecker.get_ip_via_tor()}")

        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")
