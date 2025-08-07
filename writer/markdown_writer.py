import os
from typing import List, TextIO, Set, Tuple, Any
from scanner.interpreter import InterpretedEntry, calculate_folder_summary
from datetime import datetime, timedelta

def write_markdown(structure: List[InterpretedEntry], output_path: str) -> None:
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        write_header(f)
        write_root_overview(f, structure)
        write_folder_breakdown(f, structure)
        write_modular_summary(f, structure)
        write_extensibility_forecast(f)
        write_footer(f)

def write_header(f: TextIO) -> None:
    """Write the enhanced header with metadata"""
    f.write("# 🏛️ FileSage Directory Architecture Report\n\n")
    f.write("*A comprehensive transmission from the digital cosmos, decoded by Edward's enhanced neural networks.*\n\n")
    f.write(f"📅 **Generated:** {datetime.now().strftime('%B %d, %Y at %I:%M %p')}\n")
    f.write("🔮 **Version:** FileSage 2.0 - Enhanced Structure Analysis\n\n")
    f.write("---\n\n")

def write_root_overview(f: TextIO, structure: List[InterpretedEntry]) -> None:
    """Write root directory overview with high-level metrics"""
    f.write("## 🌟 Root Directory Overview\n\n")
    
    # Calculate total metrics
    total_folders = len(structure)
    total_files = sum(len(entry["files"]) for entry in structure)
    total_size = sum(sum(file["size"] for file in entry["files"]) for entry in structure)
    
    # Gather all tags
    all_file_tags: Set[str] = set()
    all_folder_tags: Set[str] = set()
    for entry in structure:
        all_folder_tags.update(entry.get("tags", []))
        for file in entry["files"]:
            all_file_tags.update(file.get("tags", []))
    
    f.write("| Metric | Value | Cosmic Significance |\n")
    f.write("|--------|-------|--------------------|\n")
    f.write(f"| � **Total Folders** | {total_folders} | Chambers of organized digital reality |\n")
    f.write(f"| 📄 **Total Files** | {total_files} | Artifacts of computational archaeology |\n")
    f.write(f"| 💾 **Total Size** | {format_folder_size(total_size)} | Digital mass in the virtual cosmos |\n")
    f.write(f"| 🏷️ **Unique Tags** | {len(all_file_tags | all_folder_tags)} | Categorical dimensions discovered |\n\n")
    
    # Show tag distribution
    if all_file_tags or all_folder_tags:
        f.write("### 🔖 System Tag Distribution\n\n")
        all_tags: Set[str] = all_file_tags | all_folder_tags
        for tag in sorted(all_tags):
            tag_count = sum(1 for entry in structure for file in entry["files"] if tag in file.get("tags", []))
            tag_count += sum(1 for entry in structure if tag in entry.get("tags", []))
            f.write(f"- `{tag}` — {tag_count} occurrences\n")
        f.write("\n")
    
    f.write("---\n\n")

def write_folder_breakdown(f: TextIO, structure: List[InterpretedEntry]) -> None:
    """Write detailed folder-by-folder breakdown"""
    f.write("## 📂 Folder-by-Folder Analysis\n\n")
    
    for entry in structure:
        folder_summary = calculate_folder_summary(entry["files"])
        
        f.write(f"### 📁 `{entry['path'] if entry['path'] != '.' else 'Root'}`\n\n")
        
        # Folder tags
        if entry.get("tags"):
            tag_str = " ".join(f"`{tag}`" for tag in entry["tags"])
            f.write(f"**Tags:** {tag_str}\n\n")
        
        # Archetype and description
        f.write(f"**Archetype:** *{entry['folder_archetype']}*\n\n")
        f.write(f"**Purpose:** {entry['description']}\n\n")
        
        # Folder metrics table
        folder_display = entry["path"] if entry["path"] != "." else "Root"
        f.write(f"#### 📊 {folder_display} Metrics\n\n")
        f.write("| Metric | Value |\n")
        f.write("|--------|-------|\n")
        f.write(f"| Files | {folder_summary['total_files']} |\n")
        f.write(f"| Size | {folder_summary['size_formatted']} |\n")
        f.write(f"| Avg. Chaos | {folder_summary['average_chaos']}/10.0 |\n\n")
        
        # List files with enhanced metadata
        if entry["files"]:
            folder_display = entry["path"] if entry["path"] != "." else "Root"
            f.write(f"#### 📄 {folder_display} Files\n\n")
            for file in entry["files"]:
                tags_str = ""
                if file.get("tags"):
                    tags_str = " " + " ".join(f"`{tag}`" for tag in file["tags"])
                
                f.write(f"**`{file['name']}`**{tags_str}\n\n")
                f.write(f"- {file['description']}\n")
                f.write(f"- Size: {format_file_size(file['size'])} | Chaos: {file['chaos_index']:.1f}/10.0\n")
                f.write(f"- Modified: {format_time_echo(file['modified'])}\n\n")
        else:
            f.write("*🌌 An empty void, waiting to be filled with digital dreams.*\n\n")
        
        f.write("---\n\n")

def write_modular_summary(f: TextIO, structure: List[InterpretedEntry]) -> None:
    """Write system-wide modular summary"""
    f.write("## 🧬 Modular System Summary\n\n")
    
    # Categorize by tags
    workflows: List[Any] = []
    documentation: List[Any] = []
    configs: List[Any] = []
    validation: List[Any] = []
    cache: List[Any] = []
    utilities: List[Any] = []
    
    for entry in structure:
        for file_info in entry["files"]:
            file_entry: Any = {"path": entry["path"], "file": file_info}
            tags = file_info.get("tags", [])
            
            if "#workflow" in tags:
                workflows.append(file_entry)
            if "#documentation" in tags:
                documentation.append(file_entry)
            if "#config" in tags:
                configs.append(file_entry)
            if "#validation_asset" in tags:
                validation.append(file_entry)
            if "#cache" in tags:
                cache.append(file_entry)
            if "#composite_action" in tags:
                utilities.append(file_entry)
    
    categories: List[Tuple[str, List[Any], str]] = [
        ("🔄 Workflow & CI/CD", workflows, "Automation and continuous integration orchestration"),
        ("📚 Documentation", documentation, "Knowledge repositories and explanatory artifacts"),
        ("⚙️ Configuration", configs, "Behavioral parameters and system settings"),
        ("🧪 Validation & Testing", validation, "Quality assurance and verification protocols"),
        ("💾 Cache & Compiled", cache, "Optimization artifacts and compiled bytecode"),
        ("🛠️ Utilities & Tools", utilities, "Helper functions and composite actions")
    ]
    
    for title, items, description in categories:
        if items:
            f.write(f"### {title}\n\n")
            f.write(f"{description}\n\n")
            for item in items[:5]:  # Limit to 5 items per category
                path_display = f"{item['path']}/" if item['path'] != '.' else ""
                f.write(f"- `{path_display}{item['file']['name']}` — {item['file']['description'].split(' — ')[0]}\n")
            if len(items) > 5:
                f.write(f"- *...and {len(items) - 5} more files*\n")
            f.write("\n")
    
    f.write("---\n\n")

def write_extensibility_forecast(f: TextIO) -> None:
    """Write extensibility and future expansion notes"""
    f.write("## 🚀 Galactic Expansion Forecast\n\n")
    f.write("*Guidelines for extending FileSage's cosmic reach and analytical powers.*\n\n")
    
    f.write("### 🏗️ Adding New Modules\n\n")
    f.write("- **Scanner Enhancements:** Add new file type detection in `scanner/walker.py`\n")
    f.write("- **Interpreter Extensions:** Expand archetype generation in `scanner/interpreter.py`\n")
    f.write("- **Writer Formats:** Create new output formats in `writer/` directory\n\n")
    
    f.write("### 📁 Recommended Folder Conventions\n\n")
    f.write("```text\n")
    f.write("project_root/\n")
    f.write("├── .github/workflows/     # CI/CD automation\n")
    f.write("├── config/               # Configuration files\n")
    f.write("├── docs/                 # Documentation\n")
    f.write("├── scanner/              # Core analysis engine\n")
    f.write("├── writer/               # Output formatters\n")
    f.write("├── utils/                # Utility functions\n")
    f.write("├── tests/                # Validation assets\n")
    f.write("└── output/               # Generated reports\n")
    f.write("```\n\n")
    
    f.write("### 🔮 Future Enhancements\n\n")
    f.write("- **Semantic Analysis:** Import relationship mapping\n")
    f.write("- **Dependency Visualization:** ASCII or Mermaid diagrams\n")
    f.write("- **Code Quality Metrics:** Cyclomatic complexity analysis\n")
    f.write("- **Interactive Filtering:** Tag-based report customization\n\n")
    
    f.write("---\n\n")

def write_footer(f: TextIO) -> None:
    """Write footer with metadata"""
    f.write("## 🌌 Transmission Complete\n\n")
    f.write("*This report was generated by FileSage's enhanced analytical engine.*\n")
    f.write("*May your directories remain structured and your chaos indices balanced.*\n\n")
    f.write("---\n\n")
    f.write(f"*Report generated on {datetime.now().strftime('%B %d, %Y')} by FileSage 2.0*\n")

def format_folder_size(total_size: int) -> str:
    """Format total folder size"""
    if total_size < 1024:
        return f"{total_size}B"
    elif total_size < 1024 * 1024:
        return f"{total_size/1024:.1f}KB"
    elif total_size < 1024 * 1024 * 1024:
        return f"{total_size/(1024*1024):.1f}MB"
    else:
        return f"{total_size/(1024*1024*1024):.1f}GB"

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
    delta: timedelta = now - modified
    
    if delta.days == 0:
        return "still humming in the void"
    elif delta.days == 1:
        return "last touched yesterday — echoing through time"
    elif delta.days < 7:
        return f"modified {delta.days} days ago — reverberating in the digital aether"
    elif delta.days < 30:
        weeks: int = delta.days // 7
        return f"altered {weeks} week{'s' if weeks > 1 else ''} past — distant cosmic whispers"
    else:
        months: int = delta.days // 30
        return f"crafted {months} month{'s' if months > 1 else ''} ago — ancient digital archaeology"
