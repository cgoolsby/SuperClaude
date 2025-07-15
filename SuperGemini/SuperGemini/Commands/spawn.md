---
description: "Meta-orchestration for complex multi-domain operations"
---

# /sg:spawn - Task Orchestration

## Purpose
Orchestrate complex, multi-domain operations by coordinating multiple tasks, tools, and personas intelligently.

## Usage
```
/sg:spawn [operation] [--mode] [--parallel] [--checkpoint]
```

## Arguments
- `operation` - Complex operation to orchestrate
- `--mode` - Execution mode (sequential, parallel, adaptive)
- `--parallel` - Number of parallel operations
- `--checkpoint` - Save progress checkpoints

## Features
- Multi-task coordination
- Intelligent delegation
- Progress tracking
- Error recovery
- Resource optimization

## Examples
```
/sg:spawn "refactor entire codebase" --mode adaptive
/sg:spawn "security audit" --parallel 3 --checkpoint
/sg:spawn "performance optimization" --mode sequential
```

## Orchestration
- Breaks down complex tasks
- Assigns to specialists
- Coordinates execution
- Aggregates results