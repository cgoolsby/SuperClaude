---
description: "Multi-dimensional code and system analysis with intelligent routing"
---

# /sg:analyze - Code & System Analysis

## Purpose
Perform comprehensive analysis of code, systems, and architectures with intelligent persona activation and MCP coordination.

## Usage
```
/sg:analyze [target] [@path] [--focus domain] [--depth level] [--report format]
```

## Arguments
- `target` - What to analyze (file, module, system, architecture)
- `@path` - Specific path to analyze (uses Gemini's @ syntax)
- `--focus` - Analysis domain (performance, security, quality, architecture)
- `--depth` - Analysis depth (shallow, moderate, deep, exhaustive)
- `--report` - Output format (summary, detailed, actionable, markdown)

## Execution Flow
1. Determine analysis scope and complexity
2. Auto-activate analyzer persona and domain specialists
3. Engage Sequential MCP for structured analysis
4. Use Context7 for pattern recognition
5. Generate comprehensive analysis report
6. Store findings in memory for future reference

## Gemini CLI Integration
- Leverages `file_read` and `file_search` for code inspection
- Uses `shell_command` for static analysis tools
- Applies `/memory` for storing analysis context
- Integrates with native @ path syntax
- Respects file access permissions

## Auto-Activation Patterns
- **Performance Issues**: performance persona + Playwright MCP
- **Security Concerns**: security persona + Sequential MCP
- **Architecture Review**: architect persona + Context7 MCP
- **Code Quality**: refactorer persona + Sequential MCP

## Examples
```
/sg:analyze @src/ --focus security --depth deep
/sg:analyze user-auth-system --focus architecture
/sg:analyze ./api/endpoints.js --focus performance --report actionable
/sg:analyze entire-project --depth exhaustive --report markdown
```

## Wave Mode Support
For large-scale analysis, automatically enables wave mode when:
- Analyzing >20 files
- Multiple focus areas specified
- System-wide scope selected
- Exhaustive depth requested

## Memory Integration
Analysis results are automatically stored:
```
/memory add "Analysis: Security vulnerabilities found in auth.js"
/memory add "Recommendation: Update bcrypt to latest version"
```

## Quality Metrics
- Code complexity scores
- Security vulnerability count
- Performance bottleneck identification
- Maintainability index
- Test coverage gaps
- Documentation completeness

## Output Examples
### Summary Report
```
📊 Analysis Summary: user-service
- Complexity: Medium (Cyclomatic: 15)
- Security: 2 medium vulnerabilities
- Performance: 1 bottleneck identified
- Quality: 85/100 (Good)
```

### Actionable Report
```
🎯 Action Items:
1. Fix SQL injection risk in getUserById() [HIGH]
2. Add input validation to API endpoints [MEDIUM]
3. Optimize database query in findUsers() [LOW]
```