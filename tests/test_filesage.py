"""
FileSage 2.0 Test Suite
Basic functionality tests for cosmic directory analysis
"""

import unittest
import tempfile
import os
from pathlib import Path
from datetime import datetime
from typing import List

# Add parent directory to path for imports
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from scanner.walker import walk_directory, FileMetadata
from scanner.interpreter import interpret_structure, calculate_chaos_index, calculate_folder_summary, FileInfo, InterpretedEntry
from writer.markdown_writer import write_markdown


class TestWalker(unittest.TestCase):
    """Test the cosmic directory walker"""
    
    def setUp(self):
        """Create a temporary test directory structure"""
        self.test_dir = tempfile.mkdtemp()
        
        # Create test structure
        (Path(self.test_dir) / "test.py").write_text("print('hello')")
        (Path(self.test_dir) / "README.md").write_text("# Test Project")
        (Path(self.test_dir) / "config.yaml").write_text("setting: value")
        
        subdir = Path(self.test_dir) / "src"
        subdir.mkdir()
        (subdir / "main.py").write_text("# Main module")
        
    def tearDown(self):
        """Clean up test directory"""
        import shutil
        shutil.rmtree(self.test_dir)
    
    def test_walk_directory(self):
        """Test basic directory walking functionality"""
        structure = walk_directory(self.test_dir)
        
        # Should find root directory and subdirectory
        self.assertEqual(len(structure), 2)
        
        # Check root directory
        root = next(entry for entry in structure if entry['path'] == '.')
        self.assertEqual(len(root['files']), 3)  # test.py, README.md, config.yaml
        
        # Check that files have required fields including tags
        for file in root['files']:
            self.assertIn('name', file)
            self.assertIn('size', file)
            self.assertIn('modified', file)
            self.assertIn('tags', file)


class TestInterpreter(unittest.TestCase):
    """Test the cosmic interpreter"""
    
    def test_chaos_index_calculation(self):
        """Test chaos index calculation"""
        
        # Test file with low chaos
        low_chaos_file: FileMetadata = {
            'name': 'simple.py',
            'size': 100,
            'modified': datetime.now(),
            'tags': ['#documentation']
        }
        chaos = calculate_chaos_index(low_chaos_file)
        self.assertGreater(chaos, 0)
        self.assertLess(chaos, 5)
        
        # Test file with high chaos
        high_chaos_file: FileMetadata = {
            'name': 'requirements.txt',
            'size': 50000,
            'modified': datetime.now(),
            'tags': ['#config']
        }
        chaos = calculate_chaos_index(high_chaos_file)
        self.assertGreater(chaos, 5)
    
    def test_folder_summary(self):
        """Test folder summary calculation"""
        
        test_files: List[FileInfo] = [
            {
                'name': 'test1.py',
                'description': 'Test file',
                'size': 100,
                'modified': datetime.now(),
                'chaos_index': 2.0,
                'tags': []
            },
            {
                'name': 'test2.py',
                'description': 'Another test',
                'size': 200,
                'modified': datetime.now(),
                'chaos_index': 3.0,
                'tags': []
            }
        ]
        
        summary = calculate_folder_summary(test_files)
        self.assertEqual(summary['total_files'], 2)
        self.assertEqual(summary['total_size'], 300)
        self.assertEqual(summary['average_chaos'], 2.5)


class TestMarkdownWriter(unittest.TestCase):
    """Test the cosmic markdown writer"""
    
    def test_markdown_generation(self):
        """Test basic markdown generation"""
        
        # Create test structure
        test_structure: List[InterpretedEntry] = [{
            'path': '.',
            'description': 'Test directory',
            'files': [{
                'name': 'test.py',
                'description': 'Test file',
                'size': 100,
                'modified': datetime.now(),
                'chaos_index': 2.0,
                'tags': ['#validation_asset']
            }],
            'folder_archetype': 'Test chamber of cosmic validation',
            'tags': ['#validation_asset']
        }]
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            output_path = f.name
        
        try:
            write_markdown(test_structure, output_path)
            
            # Verify file was created and has content
            self.assertTrue(os.path.exists(output_path))
            
            with open(output_path, 'r', encoding='utf-8') as f:
                content = f.read()
                self.assertIn('FileSage Directory Architecture Report', content)
                self.assertIn('test.py', content)
                self.assertIn('#validation_asset', content)
                
        finally:
            if os.path.exists(output_path):
                os.unlink(output_path)


class TestIntegration(unittest.TestCase):
    """Test full FileSage integration"""
    
    def test_full_analysis_workflow(self):
        """Test complete analysis workflow"""
        # Create temporary directory with various file types
        with tempfile.TemporaryDirectory() as test_dir:
            # Create test files
            (Path(test_dir) / "main.py").write_text("print('hello')")
            (Path(test_dir) / "README.md").write_text("# Test")
            (Path(test_dir) / "config.yaml").write_text("test: true")
            (Path(test_dir) / "test_something.py").write_text("def test(): pass")
            
            # Create subdirectory
            docs_dir = Path(test_dir) / "docs"
            docs_dir.mkdir()
            (docs_dir / "guide.md").write_text("# Guide")
            
            # Run full workflow
            raw_structure = walk_directory(test_dir)
            interpreted = interpret_structure(raw_structure)
            
            # Verify results
            self.assertGreater(len(raw_structure), 0)
            self.assertGreater(len(interpreted), 0)
            
            # Check that tags were assigned
            root_files = next(entry for entry in interpreted if entry['path'] == '.')['files']
            readme_file = next(f for f in root_files if f['name'] == 'README.md')
            self.assertIn('#documentation', readme_file['tags'])
            
            test_file = next(f for f in root_files if f['name'] == 'test_something.py')
            self.assertIn('#validation_asset', test_file['tags'])


if __name__ == '__main__':
    print("🧪 Running FileSage 2.0 Cosmic Test Suite")
    unittest.main(verbosity=2)
