---
description: "Feature and code implementation with intelligent persona activation and MCP integration"
---

# /sg:implement - Feature Implementation

## Purpose
Implement features, components, and code functionality with intelligent expert activation and comprehensive development support for Gemini CLI.

## Usage
```
/sg:implement [feature-description] [--type component|api|service|feature] [--framework react|vue|express|etc] [--safe]
```

## Arguments
- `feature-description` - Description of what to implement
- `--type` - Implementation type (component, api, service, feature, module)
- `--framework` - Target framework or technology stack
- `--safe` - Use conservative implementation approach
- `--iterative` - Enable iterative development with validation steps
- `--with-tests` - Include test implementation
- `--documentation` - Generate documentation alongside implementation

## Execution
1. Analyze implementation requirements and detect technology context
2. Auto-activate relevant personas (frontend, backend, security, etc.)
3. Coordinate with MCP servers (Magic for UI, Context7 for patterns, Sequential for complex logic)
4. Generate implementation code with best practices
5. Apply security and quality validation
6. Provide testing recommendations and next steps

## Gemini CLI Integration
- Uses `file_write` and `file_edit` for code generation and modification
- Leverages `file_read` and `file_search` for codebase analysis
- Applies `/memory` for implementation progress tracking
- Coordinates with MCP servers for specialized functionality
- Auto-activates appropriate personas based on implementation type
- Respects Gemini's tool permission model

## Auto-Activation Patterns
- **Frontend**: UI components, React/Vue/Angular development → Magic MCP
- **Backend**: APIs, services, database integration → Context7 MCP
- **Security**: Authentication, authorization, data protection → Sequential MCP
- **Architecture**: System design, module structure → Sequential + Context7
- **Performance**: Optimization, scalability considerations → Playwright MCP

## Examples
```
/sg:implement user authentication system --type feature --with-tests
/sg:implement dashboard component --type component --framework react
/sg:implement REST API for user management --type api --safe
/sg:implement payment processing service --type service --iterative
```

## Memory Integration
The command automatically stores implementation context in memory:
- Current implementation status
- Design decisions made
- Dependencies identified
- Next steps planned

## Quality Gates
1. Syntax validation
2. Type safety checks
3. Security assessment
4. Performance impact analysis
5. Test coverage verification
6. Documentation completeness

## Flag Compatibility
- Works with all thinking flags (`--think`, `--think-hard`, `--ultrathink`)
- Supports compression (`--uc`) for large implementations
- Compatible with wave mode (`--wave-mode`) for complex features
- Integrates with loop mode (`--loop`) for iterative refinement