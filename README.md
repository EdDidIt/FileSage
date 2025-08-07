# 🏛️ FileSage 2.0 - Cosmic Directory Architecture Analysis

*A comprehensive directory analyzer that transcends mere file listing and enters the realm of digital archaeology.*

FileSage doesn't just scan your project structure—it **interprets** it, providing dual-layer commentary that combines functional clarity with Edwardian mystique. Think of it as having a space poet document your codebase.

## ✨ Features

### 🧠 Intelligence Upgrade

- **Tag-based semantic parsing**: Automatically categorizes files with system tags (`#workflow`, `#documentation`, `#config`, etc.)
- **Dual-layer commentary**: Each file gets both functional description and cosmic interpretation
- **Enhanced Chaos Index**: File complexity scoring based on size, age, type, and behavioral patterns

### 📊 Comprehensive Analysis

- **Root Directory Overview**: High-level metrics and tag distribution
- **Folder-by-Folder Breakdown**: Detailed analysis with archetype generation
- **Modular System Summary**: Files grouped by function and purpose
- **Temporal Echoes**: Poetic interpretation of modification timestamps

### 🎨 Beautiful Output

- **Structured Markdown Reports**: Clean tables, headers, and organized sections
- **Cosmic File Sizing**: Elegant size formatting from bytes to GB
- **Archetype Generation**: Each folder gets a mystical personality description
- **Extensibility Forecast**: Guidelines for future development

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/yourusername/FileSage.git
cd FileSage
pip install -r requirements.txt
```

### Basic Usage

```bash
python main.py
# Enter the directory path you want to analyze when prompted
```

### Example Output

FileSage generates comprehensive reports like this:

```markdown
# 🏛️ FileSage Directory Architecture Report

## 🌟 Root Directory Overview
| Metric | Value | Cosmic Significance |
|--------|-------|--------------------|
| 📁 **Total Folders** | 6 | Chambers of organized digital reality |
| 📄 **Total Files** | 17 | Artifacts of computational archaeology |
| 💾 **Total Size** | 50.3KB | Digital mass in the virtual cosmos |

### 🔖 System Tag Distribution
- `#workflow` — 3 occurrences
- `#documentation` — 7 occurrences  
- `#config` — 2 occurrences
```

## 📁 Project Structure

```text
FileSage/
├── main.py                    # Entry point - cosmic command center
├── requirements.txt           # Dependencies manifest
├── config/
│   └── settings.yaml          # Configuration rituals
├── scanner/
│   ├── walker.py              # Directory traversal engine
│   ├── interpreter.py         # Semantic analysis and archetype generation
│   └── edwardizer.py          # Cosmic commentary layer
├── writer/
│   └── markdown_writer.py     # Report generation engine
├── docs/
│   ├── README.md              # Project documentation
│   ├── architecture.md        # System architecture overview
│   └── manifesto.md           # Philosophical foundations
└── output/
    └── *.md                   # Generated structure reports
```

## 🏷️ System Tags

FileSage automatically categorizes files with semantic tags:

- `#workflow` - CI/CD, automation, and orchestration files
- `#documentation` - READMEs, guides, and explanatory content  
- `#config` - Settings, configuration, and behavioral parameters
- `#validation_asset` - Tests, validation datasets, quality assurance
- `#cache` - Compiled bytecode, cached artifacts, optimization files
- `#composite_action` - Utilities, helpers, and reusable components

## 🎯 Configuration

Customize FileSage behavior via `config/settings.yaml`:

```yaml
ignore_patterns:
  - "__pycache__"
  - ".git"
  - "node_modules"
  - ".pytest_cache"
```

## 🌌 Philosophy

FileSage embodies a unique philosophy: **structure with soul, analysis with artistry**. It's not just documenting code—it's celebrating the creative act of building software.

Every directory becomes a "chamber of organized digital reality," every file an "artifact of computational archaeology." This isn't just whimsy—it's a recognition that our codebases are living, evolving systems worthy of poetic interpretation.

## 🚀 Galactic Expansion Forecast

### Adding New Features

- **Scanner Enhancements**: Extend file type detection in `scanner/walker.py`
- **Interpreter Extensions**: Add new archetypes in `scanner/interpreter.py`  
- **Writer Formats**: Create new output formats in `writer/` directory

### Future Visions

- **Semantic Analysis**: Import relationship mapping
- **Visual Graphs**: Mermaid.js integration for dependency visualization
- **Interactive Reports**: Clickable, collapsible HTML output
- **Plugin Architecture**: User-defined tags and custom archetypes

## 🤝 Contributing

FileSage welcomes contributions from fellow cosmic architects! Whether you're adding new file type detection, creating custom archetypes, or expanding the poetic commentary system—all contributions that maintain the balance of functionality and mystique are appreciated.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/cosmic-enhancement`)
3. Commit your changes (`git commit -am 'Add new stellar functionality'`)
4. Push to the branch (`git push origin feature/cosmic-enhancement`)
5. Open a Pull Request with cosmic commentary

## 📜 License

MIT License - May your code be ever structured and your chaos indices balanced.

## 🌟 Acknowledgments

Born from the intersection of practical need and creative expression, FileSage represents the belief that developer tools can be both functional and beautiful, analytical and artistic.

---

> "In the vast cosmos of code, every directory tells a story. FileSage simply helps you hear it."
