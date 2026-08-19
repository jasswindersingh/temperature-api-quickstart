import os
import sys
from pathlib import Path
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

from fortyguard import FortyGuardClient

load_dotenv()

client = FortyGuardClient()

# Downtown Baltimore AOI (Maryland Coverage Zone)
baltimore_aoi = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [-76.6200, 39.2850],
                    [-76.6080, 39.2850],
                    [-76.6080, 39.2950],
                    [-76.6200, 39.2950],
                    [-76.6200, 39.2850]
                ]]
            }
        }
    ]
}

print("[*] Dispatching real live heatmap request to FortyGuard LTM engine...")
try:
    task = client.create_heatmap(
        polygon_aoi=baltimore_aoi,
        start_date="2024-07-15",
        filter_type=1,
        start_time="14:00",
        granularity=100,
        wait=True
    )
    print("\n[+] SUCCESS! Cloud Heatmap Generated!")
    print(f"Response: {task}")
except Exception as e:
    print(f"[-] API Response: {e}")
