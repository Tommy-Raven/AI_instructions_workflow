#!/usr/bin/env python3
"""
SSWG CLI — Canonical Implementation
Purpose: Scaffold for controlled repository interactions and PDL phase execution.
"""

import argparse
import subprocess
from pathlib import Path
from argparse import Namespace

CANONICAL_BRANCH = "canonical"


def run(cmd: str) -> int:
    """
    Execute a shell command and return the exit code.

    Args:
        cmd (str): Shell command to execute.

    Returns:
        int: Exit code from the executed command.
    """
    proc = subprocess.Popen(cmd, shell=True)
    proc.communicate()
    return proc.returncode


def cmd_phase(args: Namespace) -> None:
    """
    Execute a PDL phase (placeholder).

    Args:
        args (Namespace): Parsed CLI arguments containing 'name'.
    """
    print(f"[CLI] Executing PDL phase: {args.name}")


def cmd_add_artifact(args: Namespace) -> None:
    """
    Add a new artifact file (additive only).

    Args:
        args (Namespace): Parsed CLI arguments containing 'path' and 'content'.
    """
    path = Path(args.path)
    path.write_text(args.content, encoding="utf-8")
    run(f"git add {args.path}")
    run(f"git commit -m 'Add artifact: {args.path}'")
    print(f"[CLI] Artifact added: {args.path}")


def cmd_fork(args: Namespace) -> None:
    """
    Create a new branch/fork from current branch.

    Args:
        args (Namespace): Parsed CLI arguments containing 'name'.
    """
    run(f"git checkout -b {args.name}")
    print(f"[CLI] Branch created: {args.name}")


def cmd_request_merge(args: Namespace) -> None:
    """
    Request merge of a branch into the canonical branch.

    Args:
        args (Namespace): Parsed CLI arguments containing 'branch'.
    """
    target = CANONICAL_BRANCH
    run(f"git checkout {target}")
    run(f"git merge {args.branch}")
    print(f"[CLI] Merge completed: {args.branch} → {target}")


def build_parser() -> argparse.ArgumentParser:
    """
    Build the CLI argument parser with all SSWG commands.

    Returns:
        argparse.ArgumentParser: Configured CLI parser.
    """
    parser = argparse.ArgumentParser(prog="sswg")
    sub = parser.add_subparsers(dest="cmd")

    # Phase command
    phase = sub.add_parser("phase", help="Execute a PDL phase")
    phase.add_argument("name", help="Name of the PDL phase to execute")
    phase.set_defaults(func=cmd_phase)

    # Artifact command
    add = sub.add_parser("add-artifact", help="Add a new artifact (additive only)")
    add.add_argument("path", help="Path to the artifact file")
    add.add_argument("content", help="Content to write into the artifact")
    add.set_defaults(func=cmd_add_artifact)

    # Fork command
    fork = sub.add_parser("fork", help="Create a new branch/fork")
    fork.add_argument("name", help="Name of the new branch")
    fork.set_defaults(func=cmd_fork)

    # Merge request command
    merge = sub.add_parser("merge-request", help="Merge a branch into canonical")
    merge.add_argument("branch", help="Branch name to merge")
    merge.set_defaults(func=cmd_request_merge)

    return parser


def main() -> None:
    """
    Parse CLI arguments and execute the selected command.
    """
    parser = build_parser()
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()