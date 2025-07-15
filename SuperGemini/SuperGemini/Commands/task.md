---
description: "Long-term project and task management"
---

# /sg:task - Project Management

## Purpose
Manage long-term projects and complex features across multiple sessions with hierarchical task organization.

## Usage
```
/sg:task [action] [task-spec] [--priority] [--dependencies]
```

## Arguments
- `action` - Task action (create, update, list, complete, plan)
- `task-spec` - Task specification or ID
- `--priority` - Task priority (high, medium, low)
- `--dependencies` - Define task dependencies

## Features
- Hierarchical organization
- Progress tracking
- Dependency management
- Time estimation
- Resource allocation

## Structure
- **Epic**: Large features
- **Story**: User stories
- **Task**: Specific work items
- **Subtask**: Detailed steps

## Examples
```
/sg:task create "Epic: User Management System" --priority high
/sg:task plan "authentication-feature" --dependencies
/sg:task list --status active
/sg:task complete task-123
```

## Memory Persistence
Tasks persist across sessions using Gemini's memory system.