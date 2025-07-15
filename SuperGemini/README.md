# SuperGemini 🚀

A framework that extends Gemini CLI with specialized commands, personas, and MCP server integration.

## What is SuperGemini?

SuperGemini enhances Gemini CLI by adding:
- 🛠️ **16 specialized `/sg:` commands** for common development tasks
- 🎭 **11 AI personas** that activate based on context
- 🔧 **4 MCP servers** for documentation, reasoning, UI, and testing
- 📋 **Smart task management** using Gemini's memory system
- ⚡ **Token optimization** for efficient conversations

## Installation

```bash
# Clone the repository
git clone [repository-url]
cd SuperGemini

# Install with Python
python3 SuperGemini.py install --quick

# Or minimal installation
python3 SuperGemini.py install --minimal
```

SuperGemini installs as a Gemini extension to `~/.gemini/extensions/supergem/`

## Key Features

### Commands
All commands use the `/sg:` prefix to avoid conflicts:
- `/sg:implement` - Feature implementation with intelligent assistance
- `/sg:analyze` - Comprehensive code analysis
- `/sg:build` - Smart project building
- `/sg:test` - Testing workflows
- `/sg:improve` - Code quality enhancement
- And 11 more specialized commands

### Smart Personas
AI specialists that automatically activate:
- 🏗️ **architect** - System design and architecture
- 🎨 **frontend** - UI/UX and accessibility
- ⚙️ **backend** - APIs and infrastructure
- 🔍 **analyzer** - Debugging and investigation
- 🛡️ **security** - Security analysis
- And 6 more domain experts

### MCP Integration
Leverages Gemini's native MCP support:
- **Context7** - Library documentation
- **Sequential** - Complex reasoning
- **Magic** - UI component generation
- **Playwright** - Browser automation

## How It Works

1. **Extension System** - Operates through Gemini's extension mechanism
2. **Context Files** - GEMINI.md provides framework instructions
3. **Memory Integration** - Uses `/memory` for task continuity
4. **Tool Coordination** - Optimizes Gemini's native tools

## Quick Start

After installation, restart Gemini CLI and try:

```bash
# Implement a feature
/sg:implement user authentication system --type feature

# Analyze code
/sg:analyze @src/ --focus security

# Build project
/sg:build app --env production --optimize
```

## Configuration

SuperGemini can be configured via:
- `~/.gemini/extensions/supergem/gemini-extension.json` - Extension settings
- `~/.gemini/settings.json` - User preferences
- `.gemini/settings.json` - Project-specific settings

## Differences from SuperClaude

- Uses `/sg:` prefix for commands (vs `/sc:` in SuperClaude)
- Leverages Gemini's native MCP support
- Integrates with Gemini's memory system
- Works through extension system (not direct file installation)
- Respects Gemini's tool permission model

## Requirements

- Gemini CLI installed and configured
- Python 3.6+ for installation
- npm/npx for MCP servers

## Contributing

SuperGemini is open for contributions! Areas of interest:
- Additional commands
- New personas
- MCP server integrations
- Documentation improvements

## License

MIT License - See LICENSE file for details

---

*Built to enhance Gemini CLI with intelligent development assistance* 🎯