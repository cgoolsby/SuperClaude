---
description: "Evidence-based project estimation"
---

# /sg:estimate - Project Estimation

## Purpose
Provide accurate, evidence-based estimations for tasks, features, and projects using historical data and complexity analysis.

## Usage
```
/sg:estimate [what] [--breakdown] [--confidence] [--factors]
```

## Arguments
- `what` - What to estimate (feature, project, task, refactor)
- `--breakdown` - Show detailed breakdown
- `--confidence` - Include confidence intervals
- `--factors` - List affecting factors

## Features
- Complexity analysis
- Historical comparison
- Risk assessment
- Time/effort estimation
- Resource requirements

## Examples
```
/sg:estimate "user authentication system" --breakdown
/sg:estimate @backlog.md --confidence high
/sg:estimate refactor-database --factors
```