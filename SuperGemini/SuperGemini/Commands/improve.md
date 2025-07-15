---
description: "Evidence-based code enhancement with intelligent optimization"
---

# /sg:improve - Code Enhancement

## Purpose
Improve code quality, performance, and maintainability through evidence-based analysis and intelligent refactoring.

## Usage
```
/sg:improve [target] [@path] [--focus area] [--strategy approach] [--validate]
```

## Arguments
- `target` - What to improve (file, module, component, system)
- `@path` - Specific path using Gemini's @ syntax
- `--focus` - Improvement area (performance, security, quality, readability)
- `--strategy` - Approach (refactor, optimize, modernize, simplify)
- `--validate` - Run validation before and after improvements

## Execution Flow
1. Analyze current state and identify issues
2. Auto-activate relevant personas (refactorer, performance, security)
3. Generate improvement plan with Sequential MCP
4. Apply improvements incrementally
5. Validate changes and measure impact
6. Document improvements in memory

## Auto-Activation
- Code quality issues → refactorer persona
- Performance problems → performance persona
- Security concerns → security persona
- Architecture issues → architect persona

## Examples
```
/sg:improve @src/api/ --focus performance --validate
/sg:improve authentication --focus security
/sg:improve ./components --strategy modernize
/sg:improve entire-codebase --focus quality --strategy refactor
```

## Wave Mode Support
Automatically enables for:
- System-wide improvements
- Multiple focus areas
- Large codebases (>50 files)

## Quality Metrics
- Before/after comparison
- Performance benchmarks
- Security score improvement
- Maintainability index
- Test coverage changes