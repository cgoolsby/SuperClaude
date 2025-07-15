# RULES.md - SuperGemini Framework Actionable Rules

Simple actionable rules for Gemini CLI SuperGemini framework operation.

## Core Operational Rules

### Task Management Rules
- Use `/memory` to track complex operations and maintain context
- Execute tools with appropriate permissions and user confirmation
- Always validate before execution, verify after completion
- Run tests and linting before marking tasks complete
- Use `/sg:spawn` and `/sg:task` for complex multi-session workflows
- Maintain context across operations using Gemini's memory system

### File Operation Security
- Always use `file_read` before `file_write` or `file_edit` operations
- Use absolute paths only, prevent path traversal attacks
- Prefer batch operations when possible
- Never commit automatically unless explicitly requested
- Respect Gemini's sandboxing when enabled

### Framework Compliance
- Check package.json/requirements.txt before using libraries
- Follow existing project patterns and conventions
- Use project's existing import styles and organization
- Respect framework lifecycles and best practices
- Leverage Gemini's extension system appropriately

### Systematic Codebase Changes
- **MANDATORY**: Complete project-wide discovery before any changes
- Search ALL file types for ALL variations of target terms
- Document all references with context and impact assessment
- Plan update sequence based on dependencies and relationships
- Execute changes in coordinated manner following plan
- Verify completion with comprehensive post-change search
- Validate related functionality remains working
- Use `file_search` for comprehensive searches when scope uncertain

## Quick Reference

### Do
✅ Read before Write/Edit/Update
✅ Use absolute paths
✅ Batch operations when possible
✅ Validate before execution
✅ Check framework compatibility
✅ Auto-activate personas
✅ Preserve context using `/memory`
✅ Use quality gates (see ORCHESTRATOR.md)
✅ Complete discovery before codebase changes
✅ Verify completion with evidence
✅ Respect user confirmation requirements

### Don't
❌ Skip file_read operations
❌ Use relative paths
❌ Auto-commit without permission
❌ Ignore framework patterns
❌ Skip validation steps
❌ Mix user-facing content in config
❌ Override safety protocols
❌ Make reactive codebase changes
❌ Mark complete without verification
❌ Bypass tool confirmation when required

### Auto-Triggers
- Wave mode: complexity ≥0.7 + multiple domains
- Personas: domain keywords + complexity assessment  
- MCP servers: task type + performance requirements
- Quality gates: all operations apply 8-step validation
- Memory context: complex multi-step operations

## Gemini-Specific Rules

### Extension Integration
- All SuperGemini features operate through extension system
- Respect extension configuration in `gemini-extension.json`
- Commands use `/sg:` prefix to avoid conflicts
- MCP servers configured via extension settings

### Tool Execution
- Honor Gemini's tool permission model
- Request confirmation for destructive operations
- Use `shell_command` with caution
- Leverage `web_fetch` and `web_search` for external data

### Context Management
- GEMINI.md provides instructional context
- Use `/memory` for operation continuity
- Preserve context across chat sessions with `/chat save`
- Clear context judiciously with `/compress`

### Safety & Security
- Respect sandbox mode when active
- Follow Gemini's privacy settings
- Validate all external data sources
- Maintain audit trail for sensitive operations