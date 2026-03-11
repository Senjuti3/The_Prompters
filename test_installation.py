"""
Test script to check if all required packages are installed
"""

print("=" * 60)
print("Testing Package Installation")
print("=" * 60)
print()

packages = {
    'pandas': 'pandas',
    'openpyxl': 'openpyxl', 
    'PIL': 'Pillow',
    'cv2': 'opencv-python',
    'skimage': 'scikit-image',
    'requests': 'requests',
    'numpy': 'numpy'
}

missing = []
installed = []

for package_name, import_name in packages.items():
    try:
        if import_name == 'Pillow':
            import PIL
            print(f"[OK] {package_name} (PIL) - Installed")
        elif import_name == 'opencv-python':
            import cv2
            print(f"[OK] {package_name} (cv2) - Installed")
        elif import_name == 'scikit-image':
            import skimage
            print(f"[OK] {package_name} (skimage) - Installed")
        else:
            module = __import__(import_name)
            version = getattr(module, '__version__', 'unknown')
            print(f"[OK] {package_name} - Installed (version: {version})")
        installed.append(package_name)
    except ImportError:
        print(f"[X] {package_name} - MISSING")
        missing.append(import_name)

print()
print("=" * 60)
if missing:
    print(f"Missing packages: {', '.join(missing)}")
    print()
    print("To install missing packages, run:")
    print(f"  pip install {' '.join(missing)}")
    print()
    print("Or run: pip install -r requirements.txt")
    print()
    print("If you get permission errors:")
    print("  1. Run PowerShell/Command Prompt as Administrator")
    print("  2. Or use: pip install --user " + " ".join(missing))
else:
    print("[OK] All packages are installed! You can run the software.")
    print()
    print("Run: python evaluation_software.py")
print("=" * 60)
