#!/usr/bin/env python3
"""
FileSage 2.0 Setup Script
A cosmic installation ritual for directory architecture analysis
"""

import sys
import subprocess
from pathlib import Path

def print_cosmic(message: str):
    """Print with cosmic styling"""
    print(f"✨ {message}")

def check_python_version():
    """Ensure Python 3.6+ is available"""
    if sys.version_info < (3, 6):
        print("❌ FileSage requires Python 3.6 or higher")
        print(f"   Current version: {sys.version}")
        sys.exit(1)
    print_cosmic(f"Python {sys.version.split()[0]} detected - cosmic compatibility confirmed")

def install_dependencies():
    """Install required packages"""
    print_cosmic("Installing cosmic dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print_cosmic("Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        print("   Try running: pip install -r requirements.txt")
        sys.exit(1)

def verify_structure():
    """Verify FileSage directory structure"""
    required_dirs = ["scanner", "writer", "config", "docs", "output"]
    required_files = ["main.py", "scanner/walker.py", "scanner/interpreter.py", 
                     "writer/markdown_writer.py", "config/settings.yaml"]
    
    print_cosmic("Verifying cosmic architecture...")
    
    for dir_name in required_dirs:
        if not Path(dir_name).exists():
            print(f"❌ Missing directory: {dir_name}")
            return False
    
    for file_name in required_files:
        if not Path(file_name).exists():
            print(f"❌ Missing file: {file_name}")
            return False
    
    print_cosmic("Directory structure verified - all cosmic components present")
    return True

def create_output_dir():
    """Ensure output directory exists"""
    output_dir = Path("output")
    if not output_dir.exists():
        output_dir.mkdir()
        print_cosmic("Output directory created")

def run_test():
    """Run FileSage on itself as a test"""
    print_cosmic("Running cosmic self-analysis test...")
    try:
        # Run FileSage on current directory
        result = subprocess.run([sys.executable, "main.py"], 
                              input=str(Path.cwd()), 
                              text=True, 
                              capture_output=True)
        
        if result.returncode == 0:
            print_cosmic("Self-analysis completed successfully")
            print(f"   Report generated: {result.stdout.strip().split(': ')[-1]}")
            return True
        else:
            print(f"❌ Self-analysis failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def main():
    """Main setup orchestration"""
    print("🏛️  FileSage 2.0 Setup")
    print("=" * 50)
    
    # Check Python version
    check_python_version()
    
    # Verify structure
    if not verify_structure():
        print("❌ Setup failed - incomplete installation")
        sys.exit(1)
    
    # Install dependencies
    install_dependencies()
    
    # Create output directory
    create_output_dir()
    
    # Run test
    if run_test():
        print("\n🌟 Setup Complete!")
        print("=" * 50)
        print("FileSage 2.0 is ready for cosmic directory analysis.")
        print("\nTo analyze a directory:")
        print("  python main.py")
        print("\nFor more information:")
        print("  - README.md - Complete documentation")
        print("  - CONTRIBUTING.md - Development guidelines")
        print("  - docs/ - Architecture details")
        print("\nMay your directories remain structured and your chaos indices balanced! ✨")
    else:
        print("❌ Setup completed with warnings - test failed")
        print("   FileSage may still work, but please check the installation")

if __name__ == "__main__":
    main()
