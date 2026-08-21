import os
from dotenv import load_dotenv
import fortyguard

load_dotenv()

api_key = os.getenv("FORTYGUARD_API_KEY")
print(f"[*] API Key loaded: {api_key[:6]}...{api_key[-4:] if api_key else 'NONE'}")
print("[*] FortyGuard package contents:")
print(dir(fortyguard))

# Check notebook or example files in repository
import glob
print("[*] Available sample notebooks/scripts:")
for f in glob.glob("**/*.ipynb", recursive=True) + glob.glob("notebooks/**/*.py", recursive=True):
    print(" -", f)
