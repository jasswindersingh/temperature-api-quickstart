import os
import json
from dotenv import load_dotenv
from fortyguard import FortyGuardClient

load_dotenv()

client = FortyGuardClient()

# Sample polygon over Phoenix, Arizona (within U.S. coverage)
phoenix_aoi = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [-112.0740, 33.4484],
                    [-112.0640, 33.4484],
                    [-112.0640, 33.4584],
                    [-112.0740, 33.4584],
                    [-112.0740, 33.4484]
                ]]
            }
        }
    ]
}

print("[*] Submitting task via FortyGuardClient...")
try:
    # Testing environmental parameters or heatmap endpoint via SDK client methods
    methods = [m for m in dir(client) if not m.startswith("_")]
    print(f"[*] Available Client Methods: {methods}")
    
    # Inspecting client method signatures
    import inspect
    for m in methods:
        sig = inspect.signature(getattr(client, m))
        print(f"  - client.{m}{sig}")
except Exception as e:
    print(f"[-] Error during SDK inspection: {e}")
