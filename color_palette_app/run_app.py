import os
import sys
import subprocess

def check_dependencies():
    """Check and install required packages if needed"""
    required_packages = [
        'numpy',
        'matplotlib',
        'scikit-learn',
        'pillow',
        'gradio'
    ]
    
    def install_package(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
    print("Checking dependencies...")
    for package in required_packages:
        try:
            __import__(package)
            print(f"✓ {package} is already installed")
        except ImportError:
            print(f"Installing {package}...")
            install_package(package)
            print(f"✓ {package} has been installed")

def main():
    # Check if running with Python 3
    if sys.version_info[0] < 3:
        print("This application requires Python 3")
        sys.exit(1)
    
    # Install dependencies if needed
    check_dependencies()
    
    try:
        # Import and run the palette generator
        from palette_generator import iface
        print("\nLaunching Color Palette Generator...")
        print("Once launched, open your web browser and go to: http://localhost:7860")
        iface.launch()
    except Exception as e:
        print(f"Error launching the application: {str(e)}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()