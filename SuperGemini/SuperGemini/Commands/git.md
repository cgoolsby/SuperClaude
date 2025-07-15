---
description: "Git workflow automation and assistance"
---

# /sg:git - Git Workflow Assistant

## Purpose
Streamline git workflows with intelligent commit messages, branch management, and collaboration features.

## Usage
```
/sg:git [operation] [--message] [--branch] [--squash]
```

## Arguments
- `operation` - Git operation (commit, pr, merge, rebase, branch)
- `--message` - Commit/PR message generation
- `--branch` - Branch operations
- `--squash` - Squash commits intelligently

## Features
- Smart commit messages
- PR description generation
- Branch strategy guidance
- Conflict resolution help
- History cleanup

## Examples
```
/sg:git commit --message auto
/sg:git pr --message "Feature: User authentication"
/sg:git branch --strategy feature-flow
/sg:git rebase --squash --interactive
```

## Integration
- Analyzes changes for messages
- Follows conventional commits
- Integrates with workflows