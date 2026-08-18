import os
from dotenv import load_dotenv
from fortyguard import FortyGuardClient

load_dotenv()

client = FortyGuardClient()

# Sample polygon over Downtown Phoenix, AZ
aoi_phoenix = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [-112.0780, 33.4450],
                    [-112.0650, 33.4450],
                    [-112.0650, 33.4550],
                    [-112.0780, 33.4550],
                    [-112.0780, 33.4450]
                ]]
            }
        }
    ]
}

print("[*] Submitting live heatmap request to FortyGuard LTM engine...")

try:
    result = client.create_heatmap(
        polygon_aoi=aoi_phoenix,
        start_date="2024-07-15",
        filter_type=1,
        start_time="14:00",
        granularity=100,
        wait=True
    )
    print("\n[+] Success! Data received from FortyGuard:")
    if isinstance(result, dict):
        print(f"Keys in response: {list(result.keys())}")
        if "stats_data" in result:
            print("Stats:", result.get("stats_data"))
    else:
        print(result)
except Exception as e:
    print(f"[-] API Error: {e}")
