"""Install package speedtest-cli"""
import speedtest

def check_internet_speed():
    st = speedtest.Speedtest()

    print("🚀 Testing speed ...")

    st.get_best_server()
    download = st.download() / 1_000_000
    download_in_mb = download / 8
    upload = st.upload() / 1_000_000
    upload_in_mb = upload / 8


    ping = st.results.ping

    return {

        "download" : round(download, 2),
        "download_in_mb" : round(download_in_mb, 2),
        "upload" : round(upload, 2),
        "upload_in_mb" : round(upload_in_mb, 2),
        "ping" : round(ping, 2)

    }

speed = check_internet_speed()

print(f"⬇️ Download: {speed['download']} Mbps or {speed['download_in_mb']} MB/s")
print(f"⬆️ Upload: {speed['upload']} Mbps or {speed['upload_in_mb']} MB/s")
print(f"🕛 Ping: {speed['ping']} ms")


