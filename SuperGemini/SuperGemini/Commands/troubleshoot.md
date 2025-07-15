---
description: "Intelligent problem investigation and root cause analysis"
---

# /sg:troubleshoot - Problem Investigation

## Purpose
Systematically investigate and resolve issues through intelligent root cause analysis and evidence-based debugging.

## Usage
```
/sg:troubleshoot [symptoms] [--depth level] [--focus area] [--interactive]
```

## Arguments
- `symptoms` - Description of the problem
- `--depth` - Investigation depth (quick, thorough, exhaustive)
- `--focus` - Specific area (performance, errors, behavior, integration)
- `--interactive` - Step-by-step guided troubleshooting

## Process
1. Gather symptoms and context
2. Activate analyzer persona
3. Form hypotheses with Sequential
4. Test theories systematically
5. Identify root cause
6. Provide solution and prevention

## Examples
```
/sg:troubleshoot "API returns 500 errors intermittently" --depth thorough
/sg:troubleshoot "App crashes on startup" --focus errors --interactive
/sg:troubleshoot "Slow page load times" --focus performance
```