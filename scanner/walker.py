import os
import yaml
from typing import List, TypedDict, Dict, Any
from datetime import datetime

class FileMetadata(TypedDict):
    name: str
    size: int
    modified: datetime
    tags: List[str]

class DirectoryEntry(TypedDict):
    path: str
    folders: List[str]
    files: List[FileMetadata]
    tags: List[str]

def load_settings() -> Dict[str, Any]:
    """Load settings from config/settings.yaml"""
    try:
        with open("config/settings.yaml", "r") as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        return {"ignore_patterns": []}

def should_ignore(path: str, ignore_patterns: List[str]) -> bool:
    """Check if a path should be ignored based on patterns"""
    for pattern in ignore_patterns:
        if pattern in path:
            return True
    return False

def walk_directory(path: str) -> List[DirectoryEntry]:
    settings = load_settings()
    ignore_patterns = settings.get("ignore_patterns", [])
    
    structure: List[DirectoryEntry] = []
    for root, dirs, files in os.walk(path):
        rel_root = os.path.relpath(root, path)

        # Filter out ignored directories
        dirs[:] = [d for d in dirs if not should_ignore(d, ignore_patterns)]

        # Skip this directory if it should be ignored
        if should_ignore(rel_root, ignore_patterns):
            continue

        # Tag folders
        folder_tags: list[str] = []
        if rel_root.startswith('.github') or rel_root.startswith('.github/workflows'):
            folder_tags.append('#workflow')
        if '__pycache__' in rel_root:
            folder_tags.append('#cache')
        if 'docs' in rel_root or any(f.endswith('.md') for f in files):
            folder_tags.append('#documentation')
        if 'test' in rel_root or any(f.startswith('test_') for f in files):
            folder_tags.append('#validation_asset')
        if 'config' in rel_root:
            folder_tags.append('#config')

        # Collect file metadata with tags
        file_metadata: List[FileMetadata] = []
        for file in files:
            file_path = os.path.join(root, file)
            tags: list[str] = []
            fname = file.lower()
            # Tagging logic
            if rel_root.startswith('.github') or rel_root.startswith('.github/workflows') or fname.endswith(('.yml', '.yaml')):
                tags.append('#workflow')
            if fname.endswith('.pyc') or '__pycache__' in rel_root:
                tags.append('#cache')
            if fname.endswith('.md') or 'docs' in rel_root:
                tags.append('#documentation')
            if fname.startswith('test_') or 'test' in rel_root:
                tags.append('#validation_asset')
            if fname.endswith(('.yml', '.yaml', '.json', '.ini')) or 'config' in rel_root:
                tags.append('#config')
            # Composite action: utility functions (simple heuristic)
            if 'util' in fname or 'helper' in fname or 'tool' in fname:
                tags.append('#composite_action')

            try:
                stat = os.stat(file_path)
                file_metadata.append({
                    "name": file,
                    "size": stat.st_size,
                    "modified": datetime.fromtimestamp(stat.st_mtime),
                    "tags": tags
                })
            except (OSError, IOError):
                # If we can't stat the file, add it without metadata
                file_metadata.append({
                    "name": file,
                    "size": 0,
                    "modified": datetime.now(),
                    "tags": tags
                })

        structure.append({
            "path": rel_root,
            "folders": dirs,
            "files": file_metadata,
            # Optionally, add folder tags for future use
            "tags": folder_tags
        })
    return structure
