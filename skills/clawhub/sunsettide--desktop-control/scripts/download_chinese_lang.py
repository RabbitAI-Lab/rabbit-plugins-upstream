"""
Download Chinese language pack for Tesseract OCR.
Attempts multiple mirrors.
"""
import os, sys, urllib.request, urllib.error

TESSDATA_DIR = r"C:\Program Files\Tesseract-OCR\tessdata"
OUTPUT = os.path.join(TESSDATA_DIR, "chi_sim.traineddata")

URLS = [
    # GitHub raw (primary)
    "https://github.com/tesseract-ocr/tessdata/raw/main/chi_sim.traineddata",
    # jsDelivr CDN
    "https://cdn.jsdelivr.net/gh/tesseract-ocr/tessdata@main/chi_sim.traineddata",
    # fastly CDN
    "https://tesseract-ocr-tessdata.nyc3.digitaloceanspaces.com/chi_sim.traineddata",
]

for url in URLS:
    print(f"Trying: {url}")
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        with urllib.request.urlopen(req, timeout=30) as response:
            data = response.read()
            if len(data) < 100000:  # should be multiple MB
                print(f"  Too small ({len(data)} bytes), skipping")
                continue
            os.makedirs(TESSDATA_DIR, exist_ok=True)
            with open(OUTPUT, "wb") as f:
                f.write(data)
            print(f"  SUCCESS: {len(data)} bytes downloaded to {OUTPUT}")
            sys.exit(0)
    except Exception as e:
        print(f"  Failed: {e}")

print("All sources failed. Manual download required:")
print("  Visit: https://github.com/tesseract-ocr/tessdata/raw/main/chi_sim.traineddata")
print(f"  Save to: {OUTPUT}")
print("  (~10MB file)")
sys.exit(1)
