---
description: "Project builder with framework detection and optimization"
---

# /sg:build - Project Builder

## Purpose
Intelligently build, compile, and package projects with framework detection, optimization, and quality validation.

## Usage
```
/sg:build [target] [--env environment] [--optimize level] [--validate]
```

## Arguments
- `target` - What to build (app, component, library, docker, all)
- `--env` - Target environment (development, staging, production)
- `--optimize` - Optimization level (none, standard, aggressive)
- `--validate` - Run validation checks before build
- `--watch` - Enable watch mode for development
- `--parallel` - Use parallel builds when possible

## Execution Process
1. Detect project type and build system
2. Auto-activate appropriate personas
3. Configure build for target environment
4. Execute build with optimization
5. Validate output and report results
6. Store build artifacts and metrics

## Gemini CLI Integration
- Uses `file_read` to analyze project configuration
- Executes builds via `shell_command`
- Monitors progress and captures output
- Stores build context in `/memory`
- Respects sandbox restrictions

## Framework Detection
Automatically detects and configures for:
- **Frontend**: React, Vue, Angular, Svelte
- **Backend**: Node.js, Python, Go, Java
- **Mobile**: React Native, Flutter
- **Infrastructure**: Docker, Kubernetes

## Build Optimization
### Development
- Fast rebuilds
- Source maps enabled
- No minification
- Hot module replacement

### Production
- Code splitting
- Tree shaking
- Minification
- Asset optimization
- Bundle analysis

## Examples
```
/sg:build app --env production --optimize aggressive
/sg:build component --watch
/sg:build docker --env staging --validate
/sg:build all --parallel --env production
```

## MCP Integration
- **Context7**: Build configuration patterns
- **Magic**: UI component builds
- **Sequential**: Complex build orchestration
- **Playwright**: Post-build testing

## Quality Gates
1. Pre-build validation
2. Dependency security check
3. Build process monitoring
4. Output verification
5. Performance benchmarking
6. Artifact validation

## Memory Context
```
/memory add "Build configuration: Production with aggressive optimization"
/memory add "Build duration: 2m 34s"
/memory add "Bundle size: 245KB (gzipped)"
```

## Build Metrics
- Build duration
- Bundle sizes
- Asset optimization
- Cache utilization
- Error tracking
- Performance impact