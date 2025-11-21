# debug.py
import sys

print("--- SYS.PATH ---")
for path in sys.path:
    print(path)
print("----------------")

try:
    import models
    print(f"\n✅ SUCCESS: Python found a module named 'data_models' at: {models.__file__}")
except ImportError:
    print("\n❌ FAILURE: Python could NOT find a module named 'data_models'.")
    print("This means the file is either named incorrectly, or a system path conflict is occurring.")