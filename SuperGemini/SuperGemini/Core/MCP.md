# MCP.md - SuperGemini MCP Server Integration

Model Context Protocol (MCP) server integration for SuperGemini framework, leveraging Gemini CLI's native MCP support.

## Overview

SuperGemini integrates four specialized MCP servers through Gemini's extension system, providing enhanced capabilities for documentation, reasoning, UI generation, and testing.

## Integrated MCP Servers

### Context7 (`--c7` / `--context7`)
**Purpose**: Official library documentation and framework patterns
- Auto-activates for external library usage
- Provides up-to-date documentation
- Framework-specific best practices

### Sequential Thinking (`--seq` / `--sequential`)
**Purpose**: Complex multi-step analysis and reasoning
- Structured problem-solving
- Chain-of-thought reasoning
- Deep architectural analysis

### Magic UI (`--magic`)
**Purpose**: Modern UI component generation
- React/Vue/Angular components
- Responsive design patterns
- Accessibility-first approach

### Playwright (`--play` / `--playwright`)
**Purpose**: Browser automation and E2E testing
- Cross-browser testing
- Performance monitoring
- Visual regression testing

## Configuration

MCP servers are configured in `gemini-extension.json`:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["@context-labs/context-mcp"]
    },
    "sequential": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-sequential-thinking"]
    },
    "magic": {
      "command": "npx",
      "args": ["@magicui/cli"]
    },
    "playwright": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-playwright"]
    }
  }
}
```

## Auto-Activation Patterns

### Context7
- Import statements detected
- Framework questions
- Documentation requests
- Library-specific queries

### Sequential
- Complex debugging scenarios
- Architectural decisions
- Multi-step problems
- Any `--think` flags

### Magic
- UI component requests
- Frontend development
- Design system queries
- Component generation

### Playwright
- Testing workflows
- E2E test creation
- Performance testing
- Browser automation

## Integration with SuperGemini Commands

### Development Commands
- `/sg:build`: Uses Context7 for patterns, Magic for UI
- `/sg:implement`: All servers based on implementation type
- `/sg:design`: Magic primary, Context7 for patterns

### Analysis Commands
- `/sg:analyze`: Sequential primary, Context7 secondary
- `/sg:troubleshoot`: Sequential for root cause analysis
- `/sg:explain`: Context7 for documentation

### Quality Commands
- `/sg:improve`: Sequential for analysis, Context7 for patterns
- `/sg:test`: Playwright primary, Sequential for test design
- `/sg:cleanup`: Sequential for analysis

## Performance Optimization

### Caching Strategy
- Context7: Cache documentation for session
- Sequential: Reuse reasoning chains
- Magic: Store component templates
- Playwright: Cache test results

### Resource Management
- Selective server activation
- Lazy loading of servers
- Automatic cleanup on completion
- Token usage optimization

## Flag Control

### Enable Specific Servers
- `--c7` or `--context7`: Enable Context7
- `--seq` or `--sequential`: Enable Sequential
- `--magic`: Enable Magic UI
- `--play` or `--playwright`: Enable Playwright

### Bulk Control
- `--all-mcp`: Enable all servers
- `--no-mcp`: Disable all servers
- `--no-[server]`: Disable specific server

## Best Practices

### Server Selection
1. Use minimum required servers
2. Let auto-activation handle common cases
3. Override when specific needs arise
4. Monitor token usage with multiple servers

### Error Handling
- Graceful fallback to native tools
- Clear error messages for failures
- Retry logic for transient issues
- User notification of degraded mode

### Performance Tips
- Batch server requests when possible
- Use caching for repeated queries
- Disable unused servers with flags
- Monitor response times

## Troubleshooting

### Common Issues
1. **Server not starting**: Check npm/npx availability
2. **Slow responses**: Reduce concurrent servers
3. **Token limits**: Use `--no-mcp` for simple tasks
4. **Connection errors**: Verify network access

### Debug Mode
Enable MCP debugging:
```bash
gemini --debug-mcp
```

View active servers:
```bash
/mcp
```

## Native Gemini Integration

SuperGemini leverages Gemini CLI's native MCP support:
- No custom protocol implementation needed
- Automatic server lifecycle management
- Built-in error handling and recovery
- Seamless tool integration

This approach ensures maximum compatibility and stability while extending Gemini's capabilities through the standard extension system.