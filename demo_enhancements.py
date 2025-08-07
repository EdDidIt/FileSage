#!/usr/bin/env python3
"""
🌌 FileSage Enhancement Demo
============================

This script demonstrates the enhanced capabilities of FileSage:
- Temporal Echoes (file modification timestamps)
- Cosmic Weight (file sizes with cosmic formatting)  
- Folder Archetypes (contextual folder descriptions)
- Entropy Index (chaos ratings for files)
- System folder filtering via settings.yaml

Run this to see Edward's enhanced neural networks in action!
"""

import os
import sys
from pathlib import Path
from datetime import datetime

# Add the scanner modules to path
sys.path.append(str(Path(__file__).parent))

from scanner.walker import load_settings, FileMetadata
from scanner.interpreter import calculate_chaos_index, generate_folder_archetype
from scanner.edwardizer import generate_cosmic_comment

def demonstrate_features():
    print("🛸 FileSage Enhancement Demonstration")
    print("=" * 50)
    
    # Show settings loading
    print("\n📡 Loading cosmic configuration...")
    settings = load_settings()
    ignore_patterns = settings.get("ignore_patterns", [])
    print(f"   Ignoring patterns: {ignore_patterns}")
    
    # Create a demo file for chaos index testing
    demo_file_path = "demo_file.py"
    with open(demo_file_path, "w") as f:
        f.write("# A simple demo file for testing chaos index\nprint('Hello, cosmic void!')\n")
    
    try:
        # Test chaos calculation
        stat = os.stat(demo_file_path)
        file_meta: FileMetadata = {
            "name": demo_file_path,
            "size": stat.st_size,
            "modified": datetime.fromtimestamp(stat.st_mtime),
            "tags": []
        }
        
        chaos_index = calculate_chaos_index(file_meta)
        cosmic_comment = generate_cosmic_comment(chaos_index)
        
        print(f"\n🌀 Chaos Analysis:")
        print(f"   File: {demo_file_path}")
        print(f"   Size: {stat.st_size} bytes")
        print(f"   Chaos Index: {chaos_index:.1f}")
        print(f"   Edward's Comment: {cosmic_comment}")
        
        # Demonstrate folder archetype generation
        print(f"\n🏛️ Folder Archetype Examples:")
        test_paths = ["config", "test", "utils", "data", "docs", "__pycache__", "mysterious_folder"]
        
        for path in test_paths:
            archetype = generate_folder_archetype(path, [])
            print(f"   📂 {path}: {archetype}")
        
        print(f"\n✨ FileSage enhancements are fully operational!")
        print(f"   The cosmic neural networks are transmitting at maximum clarity.")
        
    finally:
        # Cleanup demo file
        if os.path.exists(demo_file_path):
            os.remove(demo_file_path)

if __name__ == "__main__":
    demonstrate_features()
