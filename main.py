from rotator.tor_mode import TorRotator
from rotator.proxy_mode import ProxyRotator
from rotator.vpn_mode import VPNRotator
from rotator.mac_mode import MACRotator
from rotator.scheduler import Scheduler
from rotator.ipchecker import IPChecker
from rich.console import Console

console = Console()

def menu():
    console.print("\n[bold cyan]=== StealthNet IP Rotator ===[/bold cyan]")
    console.print("[1] Tor Mode")
    console.print("[2] Proxy Rotation Mode")
    console.print("[3] VPN Rotation Mode")
    console.print("[4] MAC Address Randomization Mode")
    console.print("[5] Auto Scheduler (Random Intervals)")
    console.print("[6] Show Current IP")
    console.print("[0] Exit")
    return input("Select option: ")


def main():
    while True:
        choice = menu()

        if choice == "1":
            TorRotator().rotate()
        elif choice == "2":
            ProxyRotator().rotate()
        elif choice == "3":
            VPNRotator().rotate()
        elif choice == "4":
            MACRotator().randomize()
        elif choice == "5":
            Scheduler().start()
        elif choice == "6":
            print("Current IP:", IPChecker.get_ip())
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
