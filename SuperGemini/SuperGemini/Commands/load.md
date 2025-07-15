---
description: "Project context loading and analysis"
---

# /sg:load - Context Loader

## Purpose
Load and analyze project context to understand codebase structure, dependencies, and provide intelligent assistance.

## Usage
```
/sg:load [path] [--depth] [--focus] [--memory]
```

## Arguments
- `path` - Project path to load
- `--depth` - Analysis depth (shallow, full, deep)
- `--focus` - Specific areas to focus on
- `--memory` - Store in Gemini memory

## Features
- Project structure analysis
- Dependency mapping
- Pattern detection
- Tech stack identification
- Convention learning

## Examples
```
/sg:load @./ --depth full --memory
/sg:load @src/ --focus architecture
/sg:load entire-project --depth deep
```

## Memory Integration
Automatically stores:
- Project structure
- Key patterns
- Dependencies
- Conventions