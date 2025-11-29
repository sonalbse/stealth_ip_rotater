import random
import requests
from .ipchecker import IPChecker
from rich.console import Console

console = Console()

class ProxyRotator:
    def __init__(self):
        self.proxy_list = [
            "http://51.159.66.158:3128",
            "http://185.199.84.161:80",
            "http://5.189.184.6:80",
        ]

    def rotate(self):
        console.print("[yellow]Selecting a random proxy...[/yellow]")

        proxy = random.choice(self.proxy_list)
        console.print(f"[cyan]Using Proxy: {proxy}[/cyan]")

        try:
            ip = IPChecker.get_ip_via_proxy(proxy)
            console.print(f"[green]New IP via proxy: {ip}[/green]")
        except:
            console.print("[red]Proxy failed, try again.[/red]")
