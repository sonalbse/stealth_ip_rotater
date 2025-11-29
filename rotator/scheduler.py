import time
from rotator.tor_mode import TorRotator
from rotator.proxy_mode import ProxyRotator
from rotator.vpn_mode import VPNRotator
from rotator.mac_mode import MACRotator
from rotator.ipchecker import IPChecker


class Scheduler:

    def full_rotation(self):
        print("\n==============================")
        print("🔥 FULL ANONYMITY ROTATION STARTED")
        print("==============================\n")

        # TOR Rotation
        try:
            print("[1] Rotating TOR...")
            TorRotator().rotate()
            print("[+] TOR rotation done.\n")
        except Exception as e:
            print("[-] TOR failed:", e, "\n")

        # Proxy Rotation
        try:
            print("[2] Rotating Proxy...")
            ProxyRotator().rotate()
            print("[+] Proxy rotation done.\n")
        except Exception as e:
            print("[-] Proxy failed:", e, "\n")

        # VPN Rotation
        try:
            print("[3] Rotating VPN...")
            VPNRotator().rotate()
            print("[+] VPN rotation done.\n")
        except Exception as e:
            print("[-] VPN failed:", e, "\n")

        # MAC Randomization
        try:
            print("[4] Changing MAC Address...")
            MACRotator().randomize()
            print("[+] MAC address changed.\n")
        except Exception as e:
            print("[-] MAC change failed:", e, "\n")

        # IP CHECK
        try:
            new_ip = IPChecker()
            print(f"[5] New IP Detected: {new_ip}\n")
        except Exception as e:
            print("[-] Unable to fetch new IP:", e)

        print("🔥 FULL ROTATION COMPLETED")
        print("==============================\n")

    def start(self):

        # Ask for user-defined interval
        while True:
            try:
                interval = int(
                    input("\nEnter rotation interval in seconds (must be > 80): ")
                )
                if interval > 80:
                    break
                else:
                    print("❌ Interval MUST be greater than 80 seconds!")
            except ValueError:
                print("❌ Please enter a valid number!")

        print(f"\n⏳ Scheduler started with {interval} seconds interval...\n")

        # Loop forever
        while True:
            print(f"Next rotation in {interval} seconds...\n")

            # Countdown display
            for remaining in range(interval, 0, -1):
                print(f"⏱️  {remaining} sec remaining...", end="\r")
                time.sleep(1)

            print("\n⏳ Time's up! Starting rotation...\n")
            self.full_rotation()
