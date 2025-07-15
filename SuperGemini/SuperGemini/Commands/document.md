---
description: "Professional documentation generation with intelligent content creation"
---

# /sg:document - Documentation Generation

## Purpose
Generate comprehensive, well-structured documentation with intelligent content creation and multi-format support.

## Usage
```
/sg:document [target] [--type format] [--style guide] [--lang language]
```

## Arguments
- `target` - What to document (api, component, project, function)
- `--type` - Documentation format (markdown, jsdoc, wiki, readme)
- `--style` - Style guide (technical, user-friendly, tutorial)
- `--lang` - Language for documentation (en, es, fr, etc.)

## Features
- Auto-generates from code analysis
- Includes examples and use cases
- Cross-references related docs
- Maintains consistency
- Supports internationalization

## Examples
```
/sg:document @src/api/ --type markdown --style technical
/sg:document entire-project --type readme
/sg:document components --style user-friendly --lang es
```

## MCP Integration
- **Context7**: Documentation patterns
- **Sequential**: Content organization
- **Scribe persona**: Professional writing