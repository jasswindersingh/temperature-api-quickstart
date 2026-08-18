import os
import inspect
from dotenv import load_dotenv
from fortyguard import FortyGuardClient

load_dotenv()

print("Method Signature:")
print(inspect.signature(FortyGuardClient.create_heatmap))

print("\nMethod Docstring / Details:")
print(FortyGuardClient.create_heatmap.__doc__)
