from typing import List, TypedDict, Dict, Any
from .walker import DirectoryEntry, FileMetadata
from datetime import datetime

class FileInfo(TypedDict):
    name: str
    description: str
    size: int
    modified: datetime
    chaos_index: float
    tags: List[str]

class InterpretedEntry(TypedDict):
    path: str
    description: str
    files: List[FileInfo]
    folder_archetype: str
    tags: List[str]

def interpret_structure(structure: List[DirectoryEntry]) -> List[InterpretedEntry]:
    interpreted: List[InterpretedEntry] = []
    for entry in structure:
        folder_desc = f"Folder at {entry['path']}" if entry['path'] != '.' else "Root directory"
        files: List[FileInfo] = []
        
        for file_meta in entry['files']:
            file_info: FileInfo = {
                "name": file_meta["name"],
                "description": infer_file_purpose(file_meta["name"], file_meta.get("tags", [])),
                "size": file_meta["size"],
                "modified": file_meta["modified"],
                "chaos_index": calculate_chaos_index(file_meta),
                "tags": file_meta.get("tags", [])
            }
            files.append(file_info)
        
        interpreted.append({
            "path": entry['path'],
            "description": folder_desc,
            "files": files,
            "folder_archetype": generate_folder_archetype(entry['path'], files),
            "tags": entry.get('tags', [])
        })
    return interpreted

def calculate_folder_summary(files: List[FileInfo]) -> Dict[str, Any]:
    """Calculate folder-level metrics: total files, total size, average chaos"""
    if not files:
        return {
            "total_files": 0,
            "total_size": 0,
            "average_chaos": 0.0,
            "size_formatted": "void-sized"
        }
    
    total_files = len(files)
    total_size = sum(f["size"] for f in files)
    average_chaos = sum(f["chaos_index"] for f in files) / total_files if total_files > 0 else 0.0
    
    return {
        "total_files": total_files,
        "total_size": total_size,
        "average_chaos": round(average_chaos, 2),
        "size_formatted": format_file_size(total_size)
    }

def calculate_chaos_index(file_meta: FileMetadata) -> float:
    """Calculate the entropy/chaos rating for a file with enhanced metrics"""
    base_chaos = 1.0
    
    # Size factor - larger files tend to be more chaotic
    if file_meta["size"] > 100000:  # > 100KB
        base_chaos += 3.0
    elif file_meta["size"] > 10000:  # > 10KB
        base_chaos += 1.5
    
    # Age factor - older files without recent modification may be chaotic
    if "modified" in file_meta:
        from datetime import datetime
        age_days = (datetime.now() - file_meta["modified"]).days
        if age_days > 365:  # Over a year old
            base_chaos += 1.5
        elif age_days > 90:  # Over 3 months old
            base_chaos += 0.8
    
    # Tag-based chaos adjustment
    tags = file_meta.get("tags", [])
    if "#cache" in tags:
        base_chaos += 3.5  # Cache files are chaotic by nature
    elif "#workflow" in tags:
        base_chaos += 1.2  # CI/CD files can be complex
    elif "#validation_asset" in tags:
        base_chaos += 0.5  # Test files are usually well-structured
    elif "#documentation" in tags:
        base_chaos += 0.8  # Docs are generally orderly
    elif "#config" in tags:
        base_chaos += 1.0  # Config files vary in complexity
    elif "#composite_action" in tags:
        base_chaos += 2.0  # Utility functions can be complex
    
    # Name factor - certain patterns increase chaos
    name_lower = file_meta["name"].lower()
    if any(word in name_lower for word in ["temp", "tmp", "backup", "old", "copy"]):
        base_chaos += 2.0
    if "requirements" in name_lower:
        base_chaos += 4.7  # Special case for requirements.txt
    if name_lower.endswith(('.pyc', '.pyo', '.pyd')):
        base_chaos += 3.2
    
    # File extension factor
    if name_lower.endswith('.py'):
        base_chaos += 0.5  # Python is relatively orderly
    elif name_lower.endswith(('.txt', '.md')):
        base_chaos += 1.0
    elif name_lower.endswith(('.pdf', '.doc', '.docx')):
        base_chaos += 2.5
    else:
        base_chaos += 1.8  # Unknown types are mysterious
    
    return min(base_chaos, 10.0)  # Cap at 10.0

def generate_folder_archetype(path: str, files: List[FileInfo]) -> str:
    """Generate a cosmic archetype description for the folder"""
    if path == '.':
        return "The nexus of all possibilities — where code dreams begin."
    
    path_lower = path.lower()
    
    # Common folder archetypes
    if 'config' in path_lower:
        return "A shrine of configuration rituals and behavioral incantations."
    elif 'test' in path_lower:
        return "The proving grounds where logic faces its demons."
    elif 'util' in path_lower or 'tool' in path_lower:
        return "A toolbox of forgotten incantations and helper spirits."
    elif 'data' in path_lower:
        return "A vault of crystallized information and digital artifacts."
    elif 'doc' in path_lower:
        return "Archives of human understanding, possibly outdated."
    elif '__pycache__' in path_lower:
        return "The shadow realm where Python's compiled souls rest."
    elif 'output' in path_lower:
        return "The manifestation chamber where thoughts become reality."
    elif 'scanner' in path_lower:
        return "Eyes that pierce the veil of directory structures."
    elif 'writer' in path_lower:
        return "The scribe's chamber where data transforms into prose."
    
    # Analyze file types for generic archetype
    python_files = len([f for f in files if f["name"].endswith('.py')])
    config_files = len([f for f in files if f["name"].endswith(('.yaml', '.yml', '.json', '.ini'))])
    doc_files = len([f for f in files if f["name"].endswith(('.md', '.txt', '.rst'))])
    
    if python_files > config_files and python_files > doc_files:
        return "A nexus of computational alchemy and logical constructs."
    elif config_files > 0:
        return "A control room of parameters and behavioral switches."
    elif doc_files > 0:
        return "A library of encoded wisdom and textual mysteries."
    else:
        return "An enigmatic chamber of unknown purpose and digital whispers."

def format_file_size(size: int) -> str:
    """Format file size in a cosmic way"""
    if size == 0:
        return "void-sized"
    elif size < 1024:
        return f"{size}B"
    elif size < 1024 * 1024:
        return f"{size/1024:.1f}KB"
    elif size < 1024 * 1024 * 1024:
        return f"{size/(1024*1024):.1f}MB"
    else:
        return f"{size/(1024*1024*1024):.1f}GB"

def format_time_echo(modified: datetime) -> str:
    """Format modification time as temporal echo"""
    now = datetime.now()
    delta = now - modified
    
    if delta.days == 0:
        return "still humming in the void"
    elif delta.days == 1:
        return "last touched yesterday — echoing through time"
    elif delta.days < 7:
        return f"modified {delta.days} days ago — reverberating in the digital aether"
    elif delta.days < 30:
        weeks = delta.days // 7
        return f"altered {weeks} week{'s' if weeks > 1 else ''} past — distant cosmic whispers"
    else:
        months = delta.days // 30
        return f"crafted {months} month{'s' if months > 1 else ''} ago — ancient digital archaeology"

def infer_file_purpose(filename: str, tags: List[str] = []) -> str:
    """Generate dual-layer commentary: functional role + Edwardian flair"""
    
    # Base functional description
    functional_desc = ""
    edwardian_desc = ""
    
    # Tag-based descriptions (priority over filename)
    if "#workflow" in tags:
        functional_desc = "CI/CD workflow or automation configuration."
        edwardian_desc = "The orchestral conductor of digital symphonies."
    elif "#cache" in tags:
        functional_desc = "Compiled bytecode or cached artifacts."
        edwardian_desc = "Shadows of Python's industrial machinations."
    elif "#documentation" in tags:
        functional_desc = "Documentation or explanatory content."
        edwardian_desc = "Chronicles of human understanding, possibly outdated."
    elif "#validation_asset" in tags:
        functional_desc = "Test files or validation datasets."
        edwardian_desc = "The proving grounds where logic faces its demons."
    elif "#config" in tags:
        functional_desc = "Configuration or settings definition."
        edwardian_desc = "Sacred scrolls of behavioral incantations."
    elif "#composite_action" in tags:
        functional_desc = "Utility functions or reusable components."
        edwardian_desc = "Forgotten incantations of helper spirits."
    
    # Filename-based fallback
    if not functional_desc:
        if filename.endswith(".py"):
            functional_desc = "Python script — likely contains logic or automation."
            edwardian_desc = "Computational alchemy in serpentine script."
        elif filename.endswith(".md"):
            functional_desc = "Markdown file — documentation or notes."
            edwardian_desc = "Textile of formatted human thought."
        elif filename.endswith(".yaml") or filename.endswith(".yml"):
            functional_desc = "Configuration file — defines behavior or settings."
            edwardian_desc = "Architectural blueprints of digital behavior."
        elif filename.endswith(".json"):
            functional_desc = "Data or schema definition."
            edwardian_desc = "Crystallized data in structured notation."
        else:
            functional_desc = "Unclassified file — mysterious in nature."
            edwardian_desc = "An enigmatic artifact of unknown purpose."
    
    return f"{functional_desc} — {edwardian_desc}"
