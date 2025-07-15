# COMMANDS.md - SuperGemini Command Execution Framework

Command execution framework for Gemini CLI SuperGemini integration.

## Command System Architecture

### Core Command Structure
```yaml
---
command: "/sg:{command-name}"
category: "Primary classification"
purpose: "Operational objective"
wave-enabled: true|false
performance-profile: "optimization|standard|complex"
---
```

### Command Processing Pipeline
1. **Input Parsing**: `$ARGUMENTS` with `@<path>`, `!<command>`, `--<flags>`
2. **Context Resolution**: Auto-persona activation and MCP server selection
3. **Wave Eligibility**: Complexity assessment and wave mode determination
4. **Execution Strategy**: Tool orchestration and resource allocation
5. **Quality Gates**: Validation checkpoints and error handling

### Integration Layers
- **Gemini CLI**: Native slash command compatibility via extension
- **Persona System**: Auto-activation based on command context
- **MCP Servers**: Context7, Sequential, Magic, Playwright integration
- **Wave System**: Multi-stage orchestration for complex operations

## Wave System Integration

**Wave Orchestration Engine**: Multi-stage command execution with compound intelligence. Auto-activates on complexity ≥0.7 + files >20 + operation_types >2.

**Wave-Enabled Commands**:
- **Tier 1**: `/sg:analyze`, `/sg:build`, `/sg:implement`, `/sg:improve`
- **Tier 2**: `/sg:design`, `/sg:task`

### Development Commands

**`/sg:build $ARGUMENTS`**
```yaml
---
command: "/sg:build"
category: "Development & Deployment"
purpose: "Project builder with framework detection"
wave-enabled: true
performance-profile: "optimization"
---
```
- **Auto-Persona**: Frontend, Backend, Architect, Scribe
- **MCP Integration**: Magic (UI builds), Context7 (patterns), Sequential (logic)
- **Tool Orchestration**: [file_read, file_write, shell_command, web_fetch]
- **Arguments**: `[target]`, `@<path>`, `!<command>`, `--<flags>`

**`/sg:implement $ARGUMENTS`**
```yaml
---
command: "/sg:implement"
category: "Development & Implementation"
purpose: "Feature and code implementation with intelligent persona activation"
wave-enabled: true
performance-profile: "standard"
---
```
- **Auto-Persona**: Frontend, Backend, Architect, Security (context-dependent)
- **MCP Integration**: Magic (UI components), Context7 (patterns), Sequential (complex logic)
- **Tool Orchestration**: [file_read, file_write, file_edit, shell_command]
- **Arguments**: `[feature-description]`, `--type component|api|service|feature`, `--framework <name>`, `--<flags>`


### Analysis Commands

**`/sg:analyze $ARGUMENTS`**
```yaml
---
command: "/sg:analyze"
category: "Analysis & Investigation"
purpose: "Multi-dimensional code and system analysis"
wave-enabled: true
performance-profile: "complex"
---
```
- **Auto-Persona**: Analyzer, Architect, Security
- **MCP Integration**: Sequential (primary), Context7 (patterns), Magic (UI analysis)
- **Tool Orchestration**: [file_read, file_search, shell_command]
- **Arguments**: `[target]`, `@<path>`, `!<command>`, `--<flags>`

**`/sg:troubleshoot [symptoms] [flags]`** - Problem investigation | Auto-Persona: Analyzer, QA | MCP: Sequential, Playwright

**`/sg:explain [topic] [flags]`** - Educational explanations | Auto-Persona: Mentor, Scribe | MCP: Context7, Sequential


### Quality Commands

**`/sg:improve [target] [flags]`**
```yaml
---
command: "/sg:improve"
category: "Quality & Enhancement"
purpose: "Evidence-based code enhancement"
wave-enabled: true
performance-profile: "optimization"
---
```
- **Auto-Persona**: Refactorer, Performance, Architect, QA
- **MCP Integration**: Sequential (logic), Context7 (patterns), Magic (UI improvements)
- **Tool Orchestration**: [file_read, file_edit, shell_command]
- **Arguments**: `[target]`, `@<path>`, `!<command>`, `--<flags>`


**`/sg:cleanup [target] [flags]`** - Project cleanup and technical debt reduction | Auto-Persona: Refactorer | MCP: Sequential

### Additional Commands

**`/sg:document [target] [flags]`** - Documentation generation | Auto-Persona: Scribe, Mentor | MCP: Context7, Sequential

**`/sg:estimate [target] [flags]`** - Evidence-based estimation | Auto-Persona: Analyzer, Architect | MCP: Sequential, Context7

**`/sg:task [operation] [flags]`** - Long-term project management | Auto-Persona: Architect, Analyzer | MCP: Sequential

**`/sg:test [type] [flags]`** - Testing workflows | Auto-Persona: QA | MCP: Playwright, Sequential

**`/sg:git [operation] [flags]`** - Git workflow assistant | Auto-Persona: DevOps, Scribe, QA | MCP: Sequential

**`/sg:design [domain] [flags]`** - Design orchestration | Auto-Persona: Architect, Frontend | MCP: Magic, Sequential, Context7

### Meta & Orchestration Commands

**`/sg:index [query] [flags]`** - Command catalog browsing | Auto-Persona: Mentor, Analyzer | MCP: Sequential

**`/sg:load [path] [flags]`** - Project context loading | Auto-Persona: Analyzer, Architect, Scribe | MCP: All servers

**Iterative Operations** - Use `--loop` flag with improvement commands for iterative refinement

**`/sg:spawn [mode] [flags]`** - Task orchestration | Auto-Persona: Analyzer, Architect, DevOps | MCP: All servers

## Command Execution Matrix

### Performance Profiles
```yaml
optimization: "High-performance with caching and parallel execution"
standard: "Balanced performance with moderate resource usage"
complex: "Resource-intensive with comprehensive analysis"
```

### Command Categories
- **Development**: build, implement, design
- **Analysis**: analyze, troubleshoot, explain
- **Quality**: improve, cleanup
- **Testing**: test
- **Documentation**: document
- **Planning**: estimate, task
- **Version-Control**: git
- **Meta**: index, load, spawn

### Wave-Enabled Commands
6 commands: `/sg:analyze`, `/sg:build`, `/sg:design`, `/sg:implement`, `/sg:improve`, `/sg:task`

## Tool Mapping

### Gemini CLI Native Tools
- `file_read` - Read file contents
- `file_write` - Write new files
- `file_edit` - Edit existing files
- `file_search` - Search within files
- `shell_command` - Execute shell commands
- `web_fetch` - Fetch web content
- `web_search` - Search the web
- `memory` - Manage context memory

### MCP Server Tools
- **Context7**: Documentation and pattern lookup
- **Sequential**: Complex reasoning and analysis
- **Magic**: UI component generation
- **Playwright**: Browser automation and testing