#!/usr/bin/env python3
"""
SuperGemini Framework Management Hub
Unified entry point for all SuperGemini operations

Usage:
    SuperGemini.py install [options]
    SuperGemini.py update [options]
    SuperGemini.py uninstall [options]
    SuperGemini.py backup [options]
    SuperGemini.py --help
"""

import sys
import argparse
import subprocess
import json
from pathlib import Path
from typing import Dict, Callable

# Default installation directory for Gemini extensions
DEFAULT_INSTALL_DIR = Path.home() / ".gemini" / "extensions" / "supergem"

# Add the 'setup' directory to the Python import path
setup_dir = Path(__file__).parent / "setup"
sys.path.insert(0, str(setup_dir))

# Try to import utilities from the setup package
try:
    from setup.utils.ui import (
        display_header, display_info, display_success, display_error,
        display_warning, Colors
    )
    from setup.utils.logger import setup_logging, get_logger, LogLevel
except ImportError:
    # Provide minimal fallback functions and constants if imports fail
    class Colors:
        RED = YELLOW = GREEN = CYAN = RESET = ""

    def display_error(msg): print(f"[ERROR] {msg}")
    def display_warning(msg): print(f"[WARN] {msg}")
    def display_success(msg): print(f"[OK] {msg}")
    def display_info(msg): print(f"[INFO] {msg}")
    def display_header(title, subtitle): print(f"{title} - {subtitle}")
    def get_logger(): return None
    def setup_logging(*args, **kwargs): pass
    class LogLevel:
        ERROR = 40
        INFO = 20
        DEBUG = 10


def create_global_parser() -> argparse.ArgumentParser:
    """Create shared parser for global flags used by all commands"""
    global_parser = argparse.ArgumentParser(add_help=False)

    global_parser.add_argument("--verbose", "-v", action="store_true",
                               help="Enable verbose logging")
    global_parser.add_argument("--quiet", "-q", action="store_true",
                               help="Suppress all output except errors")
    global_parser.add_argument("--install-dir", type=Path, default=DEFAULT_INSTALL_DIR,
                               help=f"Target installation directory (default: {DEFAULT_INSTALL_DIR})")
    global_parser.add_argument("--dry-run", action="store_true",
                               help="Simulate operation without making changes")
    global_parser.add_argument("--force", action="store_true",
                               help="Force execution, skipping checks")
    global_parser.add_argument("--yes", "-y", action="store_true",
                               help="Automatically answer yes to all prompts")

    return global_parser


def create_parser():
    """Create the main CLI parser and attach subcommand parsers"""
    global_parser = create_global_parser()

    parser = argparse.ArgumentParser(
        prog="SuperGemini",
        description="SuperGemini Framework Management Hub - Unified CLI",
        epilog="""
Examples:
  SuperGemini.py install --dry-run
  SuperGemini.py update --verbose
  SuperGemini.py backup --create
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[global_parser]
    )

    parser.add_argument("--version", action="version", version="SuperGemini v1.0.0")

    subparsers = parser.add_subparsers(
        dest="operation",
        title="Operations",
        description="Framework operations to perform"
    )

    return parser, subparsers, global_parser


def setup_global_environment(args: argparse.Namespace):
    """Set up logging and shared runtime environment based on args"""
    # Determine log level
    if args.quiet:
        level = LogLevel.ERROR
    elif args.verbose:
        level = LogLevel.DEBUG
    else:
        level = LogLevel.INFO

    # Define log directory unless it's a dry run
    log_dir = args.install_dir / "logs" if not args.dry_run else None
    setup_logging("supergem_hub", log_dir=log_dir, console_level=level)

    # Log startup context
    logger = get_logger()
    if logger:
        logger.debug(f"SuperGemini.py called with operation: {getattr(args, 'operation', 'None')}")
        logger.debug(f"Arguments: {vars(args)}")


def get_operation_modules() -> Dict[str, str]:
    """Return supported operations and their descriptions"""
    return {
        "install": "Install SuperGemini framework components",
        "update": "Update existing SuperGemini installation",
        "uninstall": "Remove SuperGemini installation",
        "backup": "Backup and restore operations"
    }


def load_operation_module(name: str):
    """Try to dynamically import an operation module"""
    try:
        return __import__(f"setup.operations.{name}", fromlist=[name])
    except ImportError as e:
        logger = get_logger()
        if logger:
            logger.error(f"Module '{name}' failed to load: {e}")
        return None


def register_operation_parsers(subparsers, global_parser) -> Dict[str, Callable]:
    """Register subcommand parsers and map operation names to their run functions"""
    operations = {}
    for name, desc in get_operation_modules().items():
        module = load_operation_module(name)
        if module and hasattr(module, 'register_parser') and hasattr(module, 'run'):
            module.register_parser(subparsers, global_parser)
            operations[name] = module.run
        else:
            # If module doesn't exist, register a stub parser for now
            parser = subparsers.add_parser(name, help=desc, parents=[global_parser])
            if name == "install":
                parser.add_argument("--quick", action="store_true",
                                    help="Quick installation with recommended components")
                parser.add_argument("--minimal", action="store_true",
                                    help="Minimal installation (core framework only)")
                parser.add_argument("--profile", type=str,
                                    help="Installation profile (quick, minimal, developer)")
                parser.add_argument("--list-components", action="store_true",
                                    help="List available components")
            operations[name] = create_simple_operation(name)
    return operations


def create_simple_operation(op_name: str):
    """Create a simple operation function for demonstration"""
    def operation(args: argparse.Namespace) -> int:
        if op_name == "install":
            return simple_install(args)
        elif op_name == "uninstall":
            return simple_uninstall(args)
        elif op_name == "update":
            display_info(f"Update operation not yet implemented")
            return 0
        elif op_name == "backup":
            display_info(f"Backup operation not yet implemented")
            return 0
        return 1
    return operation


def simple_install(args: argparse.Namespace) -> int:
    """Simple installation implementation"""
    display_header("SuperGemini Framework v1.0", "Installation")
    
    if args.list_components:
        display_info("Available components:")
        display_info("  - core: Core framework files (GEMINI.md and supporting docs)")
        display_info("  - commands: 16 specialized /sg: commands")
        display_info("  - mcp: MCP server configurations")
        display_info("  - personas: AI persona system")
        return 0
    
    # Create installation directory
    install_dir = args.install_dir
    if not args.dry_run:
        install_dir.mkdir(parents=True, exist_ok=True)
        display_success(f"Created installation directory: {install_dir}")
    else:
        display_info(f"[DRY RUN] Would create: {install_dir}")
    
    # Create gemini-extension.json
    extension_config = {
        "name": "supergem",
        "version": "1.0.0",
        "contextFileName": "GEMINI.md",
        "description": "SuperGemini - Enhanced Gemini CLI with specialized commands and personas",
        "mcpServers": {
            "context7": {
                "command": "npx",
                "args": ["@context-labs/context-mcp"]
            },
            "sequential": {
                "command": "npx",
                "args": ["@modelcontextprotocol/server-sequential-thinking"]
            }
        }
    }
    
    extension_file = install_dir / "gemini-extension.json"
    if not args.dry_run:
        with open(extension_file, 'w') as f:
            json.dump(extension_config, f, indent=2)
        display_success("Created gemini-extension.json")
    else:
        display_info("[DRY RUN] Would create gemini-extension.json")
    
    # Copy framework files
    source_dir = Path(__file__).parent / "SuperGemini"
    if not args.dry_run:
        # In a real implementation, we would copy files here
        display_info("Installing framework files...")
        # For now, just create GEMINI.md
        gemini_md = install_dir / "GEMINI.md"
        gemini_md.write_text("# SuperGemini Entry Point\n\n@COMMANDS.md\n@FLAGS.md\n@PRINCIPLES.md\n@RULES.md\n@MCP.md\n@PERSONAS.md\n@ORCHESTRATOR.md\n@MODES.md\n")
        display_success("Installed GEMINI.md")
    else:
        display_info("[DRY RUN] Would install framework files")
    
    display_success("\nSuperGemini installation complete!")
    display_info(f"\nInstalled to: {install_dir}")
    display_info("\nTo use SuperGemini, restart Gemini CLI and the framework will be automatically loaded.")
    
    return 0


def simple_uninstall(args: argparse.Namespace) -> int:
    """Simple uninstallation implementation"""
    display_header("SuperGemini Framework", "Uninstallation")
    
    install_dir = args.install_dir
    if install_dir.exists():
        if not args.dry_run:
            import shutil
            shutil.rmtree(install_dir)
            display_success(f"Removed {install_dir}")
        else:
            display_info(f"[DRY RUN] Would remove: {install_dir}")
    else:
        display_warning(f"Installation directory not found: {install_dir}")
    
    return 0


def main() -> int:
    """Main entry point"""
    try:
        parser, subparsers, global_parser = create_parser()
        operations = register_operation_parsers(subparsers, global_parser)
        args = parser.parse_args()

        # No operation provided? Show help
        if not args.operation:
            if not args.quiet:
                display_header("SuperGemini Framework v1.0", "Unified CLI for all operations")
                print(f"{Colors.CYAN}Available operations:{Colors.RESET}")
                for op, desc in get_operation_modules().items():
                    print(f"  {op:<12} {desc}")
                print(f"\nUse 'SuperGemini.py <operation> --help' for more information")
            return 0

        # Set up environment (logging, etc.)
        setup_global_environment(args)

        # Run the operation
        run_func = operations.get(args.operation)
        if run_func:
            return run_func(args)
        else:
            display_error(f"Unknown operation: {args.operation}")
            return 1

    except KeyboardInterrupt:
        display_warning("\nOperation cancelled by user")
        return 130
    except Exception as e:
        display_error(f"Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())