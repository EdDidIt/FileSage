# Contributing to FileSage

*Welcome, fellow cosmic architect! Your contributions help expand FileSage's understanding of digital universes.*

## 🌟 Philosophy

FileSage embodies a unique philosophy: **structure with soul, analysis with artistry**. When contributing, please maintain this balance of practical functionality and poetic interpretation.

## 🚀 Getting Started

### Development Setup

```bash
git clone https://github.com/yourusername/FileSage.git
cd FileSage
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Running Tests

```bash
python -m pytest tests/
```

### Code Style

- Follow PEP 8 for Python code
- Use type hints where appropriate
- Maintain the cosmic commentary style in docstrings
- Keep functions focused and modular

## 🏗️ Architecture

FileSage follows a modular architecture:

- `scanner/walker.py` - Directory traversal and file discovery
- `scanner/interpreter.py` - Semantic analysis and archetype generation  
- `scanner/edwardizer.py` - Cosmic commentary layer
- `writer/markdown_writer.py` - Report generation
- `config/` - Configuration management

## 🎯 Contribution Types

### 🔍 Scanner Enhancements

Add new file type detection or improve existing patterns

Example: Adding support for Rust projects

```python
# In walker.py tagging logic
if fname.endswith('.rs') or 'cargo.toml' in fname.lower():
    tags.append('#rust_source')
```

### 🧠 Interpreter Extensions

Expand archetype generation or improve semantic analysis

Example: New folder archetype

```python
# In interpreter.py generate_folder_archetype()
elif 'rust' in path_lower or any('cargo' in f.name.lower() for f in files):
    return "A forge where Rust's memory-safe incantations are crafted."
```

### ✍️ Writer Formats

Create new output formats or enhance existing ones

Potential formats:

- HTML reports with interactive features
- JSON output for programmatic use
- Custom templates for different project types

### 🎨 Cosmic Commentary

Enhance the poetic interpretation system

Add new cosmic comments to `edwardizer.py` or improve existing ones while maintaining the mystical tone.

## 📋 Contribution Process

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/stellar-enhancement`
3. **Develop** your enhancement following the architecture patterns
4. **Test** your changes: `python main.py` on various project types
5. **Document** your changes in CHANGELOG.md
6. **Commit** with cosmic flair: `git commit -am 'Add stellar Rust project detection'`
7. **Push** to your branch: `git push origin feature/stellar-enhancement`
8. **Open** a Pull Request with detailed description

## 🏷️ System Tags

When adding new file type detection, use or extend these tags:

- `#workflow` - CI/CD, automation, orchestration
- `#documentation` - READMEs, guides, explanatory content
- `#config` - Settings, configuration, behavioral parameters
- `#validation_asset` - Tests, validation datasets, QA
- `#cache` - Compiled bytecode, cached artifacts
- `#composite_action` - Utilities, helpers, reusable components

### Adding New Tags

If you need a new tag category:

1. Add it to the tagging logic in `walker.py`
2. Update descriptions in `interpreter.py`
3. Include it in the modular summary in `markdown_writer.py`
4. Document it in README.md

## 🧪 Testing Guidelines

### Manual Testing

Test FileSage on diverse project types:

- Python projects (Django, Flask, FastAPI)
- JavaScript/Node.js projects
- Documentation repositories
- Multi-language projects
- Projects with complex CI/CD setups

### Automated Testing

When adding features, include tests that verify:

- File detection accuracy
- Tag assignment correctness
- Report generation completeness

## 🌌 Code of Conduct

- **Be respectful** - We're all exploring the digital cosmos together
- **Be constructive** - Feedback should help improve the cosmic understanding
- **Be patient** - Some mysteries take time to unravel
- **Maintain the mystique** - Keep the balance of function and poetry

## 💡 Ideas for Future Enhancements

### High Priority

- Semantic import analysis
- Interactive HTML reports
- Template system for different project types
- Plugin architecture

### Cosmic Visions

- Visual dependency graphs
- AI-powered archetype generation
- Integration with static site generators
- Real-time directory monitoring

## 📞 Getting Help

- **Issues**: Use GitHub Issues for bugs and feature requests
- **Discussions**: GitHub Discussions for general questions and ideas
- **Documentation**: Check docs/ folder for architecture details

## 🏆 Recognition

Contributors who maintain the cosmic balance of functionality and artistry will be recognized in:

- README.md acknowledgments
- CHANGELOG.md feature credits
- Cosmic commentary within the codebase itself

---

> "In contributing to FileSage, you become part of the eternal quest to bring both order and wonder to the chaos of code."

Thank you for helping FileSage evolve! ✨
