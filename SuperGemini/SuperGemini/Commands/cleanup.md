---
description: "Project cleanup and technical debt reduction"
---

# /sg:cleanup - Code Cleanup

## Purpose
Clean up code, reduce technical debt, and improve project organization through systematic refactoring.

## Usage
```
/sg:cleanup [target] [--type cleanup-type] [--aggressive] [--preserve]
```

## Arguments
- `target` - What to clean (project, dependencies, code, assets)
- `--type` - Cleanup type (unused, duplicate, deprecated, all)
- `--aggressive` - More thorough cleanup
- `--preserve` - Files/patterns to preserve

## Features
- Removes unused code
- Eliminates duplicates
- Updates deprecated patterns
- Optimizes imports
- Cleans dependencies

## Examples
```
/sg:cleanup project --type unused --aggressive
/sg:cleanup @src/ --type duplicate
/sg:cleanup dependencies --preserve "legacy/*"
```