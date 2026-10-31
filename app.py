import socket
import time
from datetime import datetime

# Taranacak yaygın servis portları
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Alt"
}

def scan_port(target_ip, port):
    try:
        # TCP socket bağlantısı oluştur
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0) # 1 saniye zaman aşımı
        result = s.connect_ex((target_ip, port))
        s.close()
        
        if result == 0:
            return "OPEN 🟢"
        else:
            return "CLOSED 🔴"
    except Exception:
        return "FILTERED ⚠️"

def run_portvector():
    print("=" * 65)
    print(" 🚀 PortVector - Network & Port Scanner Tool")
    print("=" * 65)
    
    target = input("Hedef IP veya Alan Adı girin (Örn: 127.0.0.1 veya scanme.nmap.org): ").strip()
    if not target:
        target = "127.0.0.1"
        print("⚠️ Hedef girilmediği için varsayılan olarak yerel bilgisayar (127.0.0.1) taranacak.")

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("❌ Hata: Hedef IP adresi çözümlenemedi!")
        return

    print(f"\n🎯 Hedef: {target} ({target_ip})")
    print(f"⏰ Başlangıç Zamanı: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    print(f"{'PORT':<8} | {'SERVICE':<15} | {'STATUS':<15}")
    print("-" * 65)
    
    start_time = time.time()
    for port, service in COMMON_PORTS.items():
        status = scan_port(target_ip, port)
        print(f"{port:<8} | {service:<15} | {status:<15}")
        
    elapsed = round(time.time() - start_time, 2)
    print("-" * 65)
    print(f"✨ Tarama tamamlandı! Toplam süre: {elapsed} saniye.")
    print("=" * 65)

if __name__ == "__main__":
    run_portvector()