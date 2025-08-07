# Changelog

All notable changes to FileSage will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-08-07

### 🚀 Major Enhancement Release - "Cosmic Documentation Artistry"

This release transforms FileSage from a simple directory scanner into a comprehensive digital archaeology tool.

### Added

- **System Tag Classification**: Automatic categorization with `#workflow`, `#documentation`, `#config`, `#validation_asset`, `#cache`, and `#composite_action` tags
- **Dual-Layer Commentary**: Each file receives both functional description and Edwardian mystique interpretation
- **Enhanced Chaos Index**: Now considers file size, age, and semantic tags for complexity scoring
- **Root Directory Overview**: High-level metrics including total files, folders, size, and tag distribution
- **Folder-by-Folder Analysis**: Detailed breakdown with archetype generation and folder metrics
- **Modular System Summary**: Files grouped by functional tags for easy navigation
- **Temporal Echoes**: Poetic interpretation of file modification timestamps
- **Galactic Expansion Forecast**: Extensibility guidelines and future development recommendations
- **Structured Markdown Output**: Professional tables, headers, and organized sections
- **Folder Archetype Generation**: Each directory receives a mystical personality description

### Enhanced

- **File Type Detection**: Expanded recognition of CI/CD files, documentation, cache files, and utilities
- **Size Formatting**: Cosmic file size representation from bytes to GB
- **Metadata Collection**: Enhanced file information including tags, chaos indices, and temporal data
- **Report Structure**: Complete restructure with overview, analysis, summary, and forecast sections

### Technical Improvements

- Added `tags` field to `FileMetadata` and `DirectoryEntry` TypedDicts
- Enhanced `calculate_chaos_index()` with age and tag-based factors
- New `calculate_folder_summary()` function for aggregated metrics
- Modular report generation with separate functions for each section
- Improved error handling and type annotations

## [1.0.0] - Previous Version

### Initial Release

- Basic directory traversal and file listing
- Simple chaos index calculation based on file size and name patterns
- Edwardian cosmic commentary system
- Basic Markdown report generation
- Configuration support via YAML

---

> "Every version is a step deeper into the cosmic understanding of code architecture."
