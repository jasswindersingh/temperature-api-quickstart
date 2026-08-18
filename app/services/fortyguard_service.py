import os
from dotenv import load_dotenv
from fortyguard import FortyGuardClient

load_dotenv()

class ThermalService:
    def __init__(self):
        self.api_key = os.getenv("FORTYGUARD_API_KEY")
        self.client = FortyGuardClient(api_key=self.api_key)

    def get_route_bbox(self, coords, buffer=0.005):
        """Calculates a GeoJSON polygon bounding box around a route."""
        lats = [c[0] for c in coords]
        lons = [c[1] for c in coords]
        min_lat, max_lat = min(lats) - buffer, max(lats) + buffer
        min_lon, max_lon = min(lons) - buffer, max(lons) + buffer

        return {
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[
                        [min_lon, min_lat],
                        [max_lon, min_lat],
                        [max_lon, max_lat],
                        [min_lon, max_lat],
                        [min_lon, min_lat]
                    ]]
                }
            }]
        }

    def fetch_heatmap(self, aoi_geojson, date_str="2024-07-15", time_str="14:00", granularity=100):
        """Fetches 2m-100m street-level temperature intelligence from FortyGuard."""
        try:
            result = self.client.create_heatmap(
                polygon_aoi=aoi_geojson,
                start_date=date_str,
                filter_type=1,
                start_time=time_str,
                granularity=granularity,
                wait=True
            )
            return result
        except Exception as e:
            print(f"[!] FortyGuard API dispatch note: {e}")
            return None
