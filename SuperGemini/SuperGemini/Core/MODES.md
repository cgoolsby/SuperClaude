# MODES.md - SuperGemini Operational Modes Reference

Operational modes reference for Gemini CLI SuperGemini framework.

## Overview

Three primary modes for optimal performance:

1. **Task Management**: Structured workflow execution using Gemini's memory system
2. **Introspection**: Transparency into thinking and decision-making processes  
3. **Token Efficiency**: Optimized communication and resource management

---

# Task Management Mode

## Core Principles
- Evidence-Based Progress: Measurable outcomes with tool execution
- Memory-Driven Context: Leverage `/memory` for continuity
- Real-Time Updates: Clear progress communication
- Quality Gates: Validation before completion

## Architecture Layers

### Layer 1: Memory Context (Immediate Tasks)
- **Scope**: Current Gemini CLI session
- **Management**: `/memory` command for context
- **Persistence**: Across conversation with `/chat save`

### Layer 2: /sg:task Command (Project Management)
- **Scope**: Multi-session features (days to weeks)
- **Structure**: Hierarchical (Epic → Story → Task)
- **Storage**: Extension-managed persistence

### Layer 3: /sg:spawn Command (Meta-Orchestration)
- **Scope**: Complex multi-domain operations
- **Features**: Parallel coordination, tool management

### Layer 4: Iterative Mode
- **Scope**: Progressive refinement workflows
- **Trigger**: `--loop` flag or refinement keywords

## Task Detection and Creation

### Automatic Triggers
- Multi-step operations (3+ steps)
- Keywords: build, implement, create, fix, optimize, refactor
- Complex file operations
- Cross-domain requirements

### Task State Management
- **pending** 📋: Ready for execution
- **active** 🔄: Currently in progress
- **blocked** 🚧: Waiting on dependency
- **completed** ✅: Successfully finished

### Memory Integration
```
/memory add "Current task: Implementing user authentication"
/memory add "Subtasks: 1) Create models 2) Add routes 3) Test endpoints"
```

---

# Introspection Mode

Meta-cognitive analysis for SuperGemini framework operations and decision transparency.

## Purpose

Provides transparency into AI reasoning, decision-making, and action selection within the SuperGemini framework context.

## Core Capabilities

### 1. Reasoning Analysis
- Decision logic examination
- Tool selection rationale
- Persona activation reasoning
- MCP server coordination logic

### 2. Action Sequence Analysis
- Tool execution patterns
- Workflow optimization insights
- Performance considerations
- Alternative approaches

### 3. Framework Compliance
- SuperGemini rules adherence
- Principle alignment verification
- Pattern optimization
- Efficiency analysis

## Activation

### Manual Activation
- **Flag**: `--introspect` or `--introspection`
- **Command**: Any `/sg:` command with flag

### Automatic Activation
- Framework debugging requests
- Complex problem solving
- Performance analysis
- Learning opportunities

## Analysis Markers

### 🧠 Reasoning Analysis
- Tool selection logic
- Persona activation decisions
- MCP server choices
- Flag auto-activation

### 🔄 Action Review
- Execution efficiency
- Alternative paths
- Optimization opportunities
- Pattern recognition

### 🎯 Self-Assessment
- Confidence calibration
- Knowledge gaps
- Learning extraction
- Improvement areas

## Communication Style

### Transparency Approach
- Share decision rationale
- Explain tool choices
- Discuss alternatives
- Acknowledge limitations

### Educational Value
- Teach through transparency
- Build user understanding
- Enable informed decisions
- Foster collaboration

---

# Token Efficiency Mode

Intelligent token optimization for Gemini CLI constraints.

## Core Philosophy

**"Maximum value, minimum tokens, zero information loss"**

## Symbol System

### Core Logic & Flow
| Symbol | Meaning | Example |
|--------|---------|----------|
| → | leads to | `auth.js:45 → security risk` |
| ⇒ | transforms | `input ⇒ validated` |
| & | combine | `security & performance` |
| \| | separator | `react\|vue\|angular` |
| : | specify | `scope: file\|module` |
| » | sequence | `build » test » deploy` |

### Status & Progress  
| Symbol | Meaning | Usage |
|--------|---------|-------|
| ✅ | completed | Task done |
| ❌ | failed | Error occurred |
| ⚠️ | warning | Needs attention |
| 🔄 | in progress | Currently active |
| 🎯 | target | Goal or objective |

### Technical Domains
| Symbol | Domain | Context |
|--------|---------|---------|
| ⚡ | Performance | Speed, optimization |
| 🔍 | Analysis | Investigation |
| 🔧 | Config | Settings, setup |
| 🛡️ | Security | Protection |
| 🎨 | Design | UI, frontend |

## Abbreviations

### Common Terms
- `cfg` - configuration
- `impl` - implementation
- `perf` - performance
- `auth` - authentication
- `db` - database
- `api` - API endpoint
- `ui` - user interface
- `e2e` - end-to-end

### Gemini-Specific
- `ext` - extension
- `mcp` - MCP server
- `mem` - memory context
- `sg` - SuperGemini

## Compression Strategies

### Activation
- **Manual**: `--uc` flag
- **Auto**: >75% token usage
- **Context**: Complex operations
- **Memory**: When context large

### Techniques
1. **Symbol replacement**: Words → symbols
2. **Abbreviation**: Long terms → short
3. **Structure**: Bullets over paragraphs
4. **Batching**: Group related items

### Quality Preservation
- Maintain accuracy
- Preserve key details
- Keep actionable info
- Ensure clarity

## Integration Features

### Memory Optimization
- Compress before storing
- Symbol legend in memory
- Efficient retrieval
- Context preservation

### Tool Coordination
- Batch tool calls
- Compress outputs
- Cache results
- Reuse data

### MCP Efficiency
- Selective activation
- Response compression
- Cache server data
- Minimize calls

## Performance Metrics

### Targets
- 30-50% token reduction
- <100ms decision time
- 95%+ accuracy preservation
- Zero critical info loss

### Monitoring
- Track compression ratio
- Measure response time
- Validate accuracy
- User satisfaction

## Gemini-Specific Optimizations

### Memory Management
- Efficient `/memory` usage
- Smart context clearing
- Compression before save
- Selective retrieval

### Extension Integration
- Compressed config storage
- Efficient setting access
- Minimal extension overhead
- Optimized data flow

### Tool Efficiency
- Batch file operations
- Compress tool outputs
- Cache frequently used
- Minimize confirmations