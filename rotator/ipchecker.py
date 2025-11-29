import requests

class IPChecker:

    @staticmethod
    def get_ip():
        return requests.get("https://api.ipify.org").text

    @staticmethod
    def get_ip_via_tor():
        proxies = {"http": "socks5h://127.0.0.1:9050",
                   "https": "socks5h://127.0.0.1:9050"}
        return requests.get("https://api.ipify.org", proxies=proxies).text

    @staticmethod
    def get_ip_via_proxy(proxy):
        proxies = {"http": proxy, "https": proxy}
        return requests.get("https://api.ipify.org", proxies=proxies, timeout=8).text
