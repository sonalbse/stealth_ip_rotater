# 🕵️‍♂️ Stealth_Ip_Rotater v1.0  
**Advanced Multi-Layer Anonymity & IP Rotation Framework**  
Built for ethical cybersecurity research, Red Team OPSEC, and privacy protection.

---

## 🚀 Features

### 🔄 Multi-Layer IP Rotation  
Stealth_Ip_Rotater cycles through multiple anonymity layers:

- **Tor IP Rotation** (via Tor ControlPort)
- **Proxy Rotation** (HTTP/SOCKS auto-switch)
- **VPN Rotation** (NetworkManager profiles)
- **MAC Address Randomization**
- **Auto Scheduler** (Runs all layers at customizable intervals)
- **Live IP Checker**

Each layer runs independently or combined — ideal for anonymity labs.


## 🛠 Installation

### Windows / Linux / Kali

git clone https://github.com/YOUR-USERNAME/stealthnet-rotator.git

cd stealthnet-rotator

pip install -r requirements.txt

Kali Linux (with Tor)

sudo apt update

sudo apt install tor -y

sudo systemctl enable tor

sudo systemctl start tor


** Usage

Run: python3 main.py

You will see:

=== StealthNet IP Rotator ===

[1] Tor Mode

[2] Proxy Mode

[3] VPN Mode

[4] MAC Randomization

[5] Auto Scheduler

[6] Show Current IP

📌 Auto Scheduler (Recommended)

The scheduler runs all anonymity layers automatically every user-defined interval (min 80 seconds):

Enter rotation interval (in seconds): 

Example: 120

⚠️ Legal Notice
This tool is strictly for educational & cybersecurity research.
Using it to hide illegal activity is prohibited.

See DISCLAIMER.txt for full notice.

👤 Author
Sonal K




