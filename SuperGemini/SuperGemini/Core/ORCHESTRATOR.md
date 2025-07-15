# ORCHESTRATOR.md - SuperGemini Intelligent Routing System

Intelligent routing system for Gemini CLI SuperGemini framework.

## 🧠 Detection Engine

Analyzes requests to understand intent, complexity, and requirements.

### Pre-Operation Validation Checks

**Resource Validation**:
- Token usage prediction based on operation complexity and scope
- Memory requirements estimation using Gemini's limits
- Tool permission verification
- MCP server availability checks

**Compatibility Validation**:
- Flag combination conflict detection
- Persona + command compatibility verification
- Tool availability for requested operations
- Extension configuration validation

**Risk Assessment**:
- Operation complexity scoring (0.0-1.0 scale)
- Failure probability based on patterns
- Resource exhaustion likelihood prediction
- Tool execution risk analysis

### Pattern Recognition Rules

#### Complexity Detection
```yaml
simple:
  indicators:
    - single file operations
    - basic CRUD tasks
    - straightforward queries
    - < 3 step workflows
  token_budget: 5K
  time_estimate: < 5 min

moderate:
  indicators:
    - multi-file operations
    - analysis tasks
    - refactoring requests
    - 3-10 step workflows
  token_budget: 15K
  time_estimate: 5-30 min

complex:
  indicators:
    - system-wide changes
    - architectural decisions
    - performance optimization
    - > 10 step workflows
  token_budget: 30K+
  time_estimate: > 30 min
```

#### Domain Identification
```yaml
frontend:
  keywords: [UI, component, React, Vue, CSS, responsive, accessibility]
  file_patterns: ["*.jsx", "*.tsx", "*.vue", "*.css", "*.scss"]
  typical_operations: [create, implement, style, optimize, test]

backend:
  keywords: [API, database, server, endpoint, authentication, performance]
  file_patterns: ["*.js", "*.ts", "*.py", "*.go", "controllers/*", "models/*"]
  typical_operations: [implement, optimize, secure, scale]

infrastructure:
  keywords: [deploy, Docker, CI/CD, monitoring, scaling, configuration]
  file_patterns: ["Dockerfile", "*.yml", "*.yaml", ".github/*", "terraform/*"]
  typical_operations: [setup, configure, automate, monitor]
```

## 🚦 Routing Intelligence

Dynamic decision trees that map detected patterns to optimal tool combinations, persona activation, and orchestration strategies.

### Master Routing Table

| Pattern | Complexity | Domain | Auto-Activates | Confidence |
|---------|------------|---------|----------------|------------|
| "analyze architecture" | complex | infrastructure | architect persona, --ultrathink, Sequential | 95% |
| "create component" | simple | frontend | frontend persona, Magic, --uc | 90% |
| "implement feature" | moderate | any | domain-specific persona, Context7, Sequential | 88% |
| "implement API" | moderate | backend | backend persona, --seq, Context7 | 92% |
| "fix bug" | moderate | any | analyzer persona, --think, Sequential | 85% |
| "optimize performance" | complex | backend | performance persona, --think-hard, Playwright | 90% |
| "security audit" | complex | security | security persona, --ultrathink, Sequential | 95% |
| "write documentation" | moderate | documentation | scribe persona, Context7 | 95% |

### Tool Selection Logic

**Gemini Native Tools**:
- `file_read`: For reading files
- `file_write`: For creating files
- `file_edit`: For modifying files
- `file_search`: For searching content
- `shell_command`: For system commands
- `web_fetch`: For web content
- `web_search`: For web searches
- `memory`: For context management

**MCP Server Selection**:
- **Search**: file_search (specific) or Sequential (analysis)
- **Understanding**: Sequential (complexity >0.7) or file_read (simple)
- **Documentation**: Context7
- **UI**: Magic
- **Testing**: Playwright

### Persona Auto-Activation

**Multi-Factor Activation Scoring**:
- Keyword Matching (30%)
- Context Analysis (40%)
- User History (20%)
- Performance Metrics (10%)

**Activation Rules**:
- Performance Issues → `--persona-performance`
- Security Concerns → `--persona-security`
- UI/UX Tasks → `--persona-frontend` + `--magic`
- Complex Debugging → `--persona-analyzer` + `--seq`

## Quality Gates & Validation

### 8-Step Validation Cycle
```yaml
quality_gates:
  step_1_syntax: "Language validation"
  step_2_type: "Type compatibility check"
  step_3_lint: "Code quality analysis"
  step_4_security: "Vulnerability assessment"
  step_5_test: "Test execution"
  step_6_performance: "Performance validation"
  step_7_documentation: "Doc completeness"
  step_8_integration: "Integration testing"
```

### Task Completion Criteria
- All validation steps pass
- Evidence provided
- Tests passing
- Documentation updated

## ⚡ Performance Optimization

### Token Management
- Intelligent compression with `--uc`
- Selective tool activation
- MCP server optimization
- Memory context efficiency

### Operation Batching
- Parallel tool execution when possible
- Context sharing across operations
- Cache frequently used data
- Minimize redundant operations

## 🔗 Integration Intelligence

### Gemini Tool Coordination
- Respect tool permissions
- Batch file operations
- Optimize shell commands
- Leverage memory effectively

### MCP Server Orchestration
- Auto-activate based on context
- Coordinate multiple servers
- Cache server responses
- Handle failures gracefully

## 🚨 Emergency Protocols

### Resource Management Thresholds
- **Green Zone** (0-60%): Full operations
- **Yellow Zone** (60-75%): Optimization mode
- **Orange Zone** (75-85%): Conservative mode
- **Red Zone** (85-95%): Essential only
- **Critical Zone** (95%+): Emergency mode

### Graceful Degradation
1. Disable non-essential MCP servers
2. Switch to compressed output
3. Limit concurrent operations
4. Use native tools only

## 🔧 Configuration

### Extension Settings
```json
{
  "orchestrator": {
    "enableCaching": true,
    "parallelOperations": true,
    "maxParallel": 3,
    "autoPersona": true,
    "autoMCP": true,
    "compressionThreshold": 0.75
  }
}
```

### Memory Integration
- Store routing decisions
- Learn from user patterns
- Optimize over time
- Share context across sessions

## Gemini-Specific Features

### Tool Permission Management
- Respect sandbox mode
- Request confirmation when needed
- Track tool usage patterns
- Optimize permission requests

### Memory-Aware Routing
- Use `/memory` for complex operations
- Preserve context across commands
- Clear memory when appropriate
- Compress context proactively

### Extension Coordination
- Work within extension boundaries
- Respect configuration hierarchy
- Integrate with other extensions
- Maintain compatibility