# 🧠 FileSage - Enhanced Cosmic Code Scanner

FileSage is a whimsical project analyzer that scans any directory and generates a modular, annotated structure report. Inspired by Radical Edward, it blends technical insight with cosmic commentary, now enhanced with temporal echoes, entropy indices, and folder archetypes.

## ✨ Enhanced Features

### 🌌 **Temporal Echoes**

- File modification timestamps with cosmic interpretations
- Examples: "still humming in the void", "echoing through time", "ancient digital archaeology"

### ⚖️ **Cosmic Weight**

- File sizes formatted with Edward's flair
- From "void-sized" to gigabytes, all measured in cosmic terms

### 🏛️ **Folder Archetypes**

- Context-aware folder descriptions based on purpose and contents
- Examples: "A shrine of configuration rituals", "The shadow realm where Python's compiled souls rest"

### 🌀 **Entropy Index (Chaos Ratings)**

- Mathematical chaos ratings (0.0-10.0) for each file
- Based on size, naming patterns, file type, and other complexity factors
- Accompanied by Edward's cosmic commentary scaled to chaos level

### 🛸 **Smart Filtering**

- Configurable ignore patterns via `config/settings.yaml`
- Automatically skips system folders like `__pycache__`, `.venv`, `.git`

### 📊 **Folder Metrics**

- Per-folder summaries with file count, total size, and average chaos index
- Empty folders get special "void" treatment

## Usage

```bash
python main.py
# Enter directory path when prompted
# Find your cosmic report in output/[ProjectName]_structure.md
```

## Example Output

```markdown
## 📂 scanner
Folder at scanner — A node in the cosmic lattice.

> *Eyes that pierce the veil of directory structures.*

- `walker.py` — Python script — 2.2KB — still humming in the void — 🕊️ Chaos Index: 1.5 — serene as a digital meditation.
- `interpreter.py` — Python script — 6.1KB — still humming in the void — 🌿 Chaos Index: 1.5 — grows in perfect algorithmic harmony.

*📊 Folder metrics: 4 files, 11.5KB total, average chaos: 1.5*
```

## Configuration

Edit `config/settings.yaml` to customize behavior:

```yaml
edward_mode: true
verbosity: high
ignore_patterns:
  - __pycache__
  - .git
  - node_modules
  - .venv
  - venv
  - env
```

## Architecture

- **`scanner/`**: Core analysis modules
  - `walker.py`: Directory traversal with metadata collection
  - `interpreter.py`: File purpose detection and chaos calculation
  - `edwardizer.py`: Cosmic commentary generation
- **`writer/`**: Output formatting
- **`config/`**: Settings and configuration
- **`output/`**: Generated reports

No modes, no dilution. Edward speaks in one voice: cosmic, chaotic, and unapologetically brilliant.
