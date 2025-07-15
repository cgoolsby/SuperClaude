---
description: "Comprehensive testing workflows with intelligent test generation"
---

# /sg:test - Testing Workflows

## Purpose
Create, run, and manage tests with intelligent test generation and comprehensive coverage analysis.

## Usage
```
/sg:test [type] [target] [--coverage] [--watch] [--generate]
```

## Arguments
- `type` - Test type (unit, integration, e2e, performance, security)
- `target` - What to test (file, module, feature, all)
- `--coverage` - Generate coverage report
- `--watch` - Run in watch mode
- `--generate` - Auto-generate test cases

## Execution Process
1. Analyze code to understand testing needs
2. Auto-activate QA persona
3. Generate or run appropriate tests
4. Use Playwright for E2E tests
5. Report results and coverage
6. Store test context in memory

## Test Types
- **Unit**: Component and function testing
- **Integration**: Module interaction testing
- **E2E**: User workflow testing with Playwright
- **Performance**: Load and stress testing
- **Security**: Vulnerability testing

## Examples
```
/sg:test unit @src/utils/ --coverage
/sg:test e2e user-login --generate
/sg:test integration api --watch
/sg:test performance /endpoints --coverage
```

## MCP Integration
- **Playwright**: E2E and browser testing
- **Sequential**: Test strategy planning
- **Context7**: Testing best practices

## Auto-Generation
When using `--generate`:
- Analyzes code structure
- Identifies test scenarios
- Creates comprehensive test cases
- Includes edge cases
- Adds meaningful assertions