#!/usr/bin/env python3
"""
Error Recovery Module - Auto-healing and recovery strategies for skills.
"""

import os
import re
import json
import shutil
import subprocess
import sys
import time
from functools import wraps   # BUG FIXED (v2.1.0): with_healing() used
                              # @wraps without importing it, so the
                              # documented decorator raised NameError
                              # on every use. Never covered by a test.
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional
from dataclasses import dataclass, field

# Import from debugger
sys.path.insert(0, str(Path(__file__).parent))
from debugger import (
    ErrorRecovery,
    ErrorClassifier, ClassifiedError, ErrorType,
    CircuitBreaker, CircuitBreakerError, setup_logging
)

logger = setup_logging(level=3)  # WARNING level

@dataclass
class RecoveryResult:
    success: bool
    action_taken: str
    message: str
    recovery_time: float = 0.0

# ============================================================================
# DESTRUCTIVE-CAPABILITY GATE (v2.1.0)
# ----------------------------------------------------------------------------
# The ClawHub security scan flagged this module for being able to "install
# packages, kill or restart processes, delete files ... without enough scoping
# or disclosure". All three were true and all three were reachable by default:
#
#   * _heal_dependency() ran `pip install <name>` where <name> came from a REGEX
#     over an ERROR MESSAGE. Anything that can influence an error string could
#     therefore choose a package to install - a supply-chain hazard, not merely
#     a scoping issue.
#   * restart_service() ran `pkill -f <pattern>`; a loose pattern kills
#     unrelated processes.
#   * cleanup_temp_files() deleted (fixed separately: now dry-run by default).
#
# These are legitimate self-healing actions, so they are kept - but they are now
# OPT-IN. Without the env var they refuse and say exactly how to enable them.
# ============================================================================

ALLOW_DESTRUCTIVE_ENV = "DEBUG_FRAMEWORK_ALLOW_DESTRUCTIVE"

# PEP 508-safe distribution name. Anything else is never passed to pip.
_SAFE_PACKAGE_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")


def destructive_allowed() -> bool:
    """True only when the operator explicitly opted in."""
    return os.environ.get(ALLOW_DESTRUCTIVE_ENV, "").strip().lower() in {"1", "true", "yes"}


def _refused(action: str, what: str) -> "RecoveryResult":
    return RecoveryResult(
        success=False,
        action_taken=f"{action}_refused",
        message=(f"Refused to {what}: this is a destructive action and "
                 f"{ALLOW_DESTRUCTIVE_ENV} is not set. Export "
                 f"{ALLOW_DESTRUCTIVE_ENV}=1 to permit it."),
    )


class RecoveryStrategies:
    """Collection of recovery strategies for common failures."""
    
    @staticmethod
    def restart_service(service_name: str, cmd: List[str]) -> RecoveryResult:
        """Restart a service that has crashed.

        Gated: kills processes matching `service_name` with `pkill -f`, which is
        a pattern match and can hit unrelated processes.
        """
        start = time.time()
        if not destructive_allowed():
            return _refused("restart", f"pkill -f {service_name!r} and respawn it")
        try:
            subprocess.run(["pkill", "-f", service_name], 
                         capture_output=True, timeout=5)
            time.sleep(1)
        except Exception:
            pass
        
        try:
            subprocess.Popen(cmd, stdout=subprocess.DEVNULL, 
                           stderr=subprocess.DEVNULL)
            return RecoveryResult(
                success=True,
                action_taken="restart",
                message=f"Service {service_name} restarted",
                recovery_time=time.time() - start
            )
        except Exception as e:
            return RecoveryResult(
                success=False,
                action_taken="restart_failed",
                message=str(e),
                recovery_time=time.time() - start
            )
    
    @staticmethod
    def cleanup_temp_files(patterns: List[str], directories: List[str],
                           dry_run: bool = True) -> RecoveryResult:
        """Clean up temporary files that may be causing issues.

        SAFETY FIX (v2.1.0): this deleted unconditionally - `unlink()` on files
        and `shutil.rmtree()` on directories - and the CLI pointed it at bare
        `/tmp` when no skill was named. A consumer running the documented
        `recovery.py cleanup` could therefore destroy temporary files belonging
        to unrelated processes. Deletion is now OPT-IN: the default lists what
        WOULD be removed and touches nothing. Pass dry_run=False (CLI: --apply)
        to actually delete.
        """
        start = time.time()
        cleaned = 0
        candidates: List[str] = []

        # SCOPING FIX (v2.1.4): the gate previously lived only in the CLI, so a
        # direct library call with dry_run=False deleted files with the gate shut.
        # Reproduced. Enforce it where the deletion actually happens.
        if not dry_run and not destructive_allowed():
            return _refused("cleanup", "delete files")

        for directory in directories:
            base = Path(directory).expanduser().resolve()
            for pattern in patterns:
                for filepath in base.glob(pattern):
                    try:
                        resolved = filepath.resolve()
                        # never escape the directory we were asked to clean
                        if base not in resolved.parents and resolved != base:
                            continue
                        candidates.append(str(resolved))
                        if dry_run:
                            continue
                        if resolved.is_file():
                            resolved.unlink()
                            cleaned += 1
                        elif resolved.is_dir():
                            shutil.rmtree(resolved)
                            cleaned += 1
                    except Exception as e:
                        logger.warning(f"Could not remove {filepath}: {e}")
        
        return RecoveryResult(
            success=True,
            action_taken="cleanup",
            message=f"Cleaned {cleaned} files/directories",
            recovery_time=time.time() - start
        )
    
    @staticmethod
    def recreate_directory(path: str, permissions: int = 0o755) -> RecoveryResult:
        # Gated (v2.1.4): this rmtree()s an arbitrary directory before recreating it.
        """Recreate a directory that may be corrupted."""
        if not destructive_allowed():
            return _refused("recreate_directory", f"delete and recreate {path!r}")
        start = time.time()
        path_obj = Path(path)
        
        try:
            if path_obj.exists():
                shutil.rmtree(path_obj)
            path_obj.mkdir(parents=True, mode=permissions)
            return RecoveryResult(
                success=True,
                action_taken="recreate",
                message=f"Directory {path} recreated",
                recovery_time=time.time() - start
            )
        except Exception as e:
            return RecoveryResult(
                success=False,
                action_taken="recreate_failed",
                message=str(e),
                recovery_time=time.time() - start
            )
    
    @staticmethod
    def network_fallback(primary_url: str, fallback_urls: List[str]) -> str:
        """Try primary URL, fallback to alternatives on failure."""
        import urllib.request
        import urllib.error
        
        urls = [primary_url] + fallback_urls
        last_error = None
        
        for url in urls:
            try:
                req = urllib.request.Request(url)
                with urllib.request.urlopen(req, timeout=10) as response:
                    return response.read().decode()
            except Exception as e:
                last_error = e
                logger.warning(f"Fallback: {url} failed: {e}")
                continue
        
        raise last_error or Exception("All URLs failed")
    
    @staticmethod
    def rollback_to_backup(backup_path: str, target_path: str) -> RecoveryResult:
        # Gated (v2.1.4): this removes target_path and copies over it.
        """Restore from backup."""
        if not destructive_allowed():
            return _refused("rollback", f"replace {target_path!r} from a backup")
        start = time.time()
        
        backup = Path(backup_path)
        target = Path(target_path)
        
        if not backup.exists():
            return RecoveryResult(
                success=False,
                action_taken="rollback_failed",
                message=f"Backup not found: {backup_path}",
                recovery_time=time.time() - start
            )
        
        try:
            if target.exists():
                if target.is_dir():
                    shutil.rmtree(target)
                else:
                    target.unlink()
            
            if backup.is_dir():
                shutil.copytree(backup, target)
            else:
                shutil.copy2(backup, target)
            
            return RecoveryResult(
                success=True,
                action_taken="rollback",
                message=f"Restored from {backup_path}",
                recovery_time=time.time() - start
            )
        except Exception as e:
            return RecoveryResult(
                success=False,
                action_taken="rollback_failed",
                message=str(e),
                recovery_time=time.time() - start
            )

class AutoHealer:
    """Automatic healing for common skill failures."""
    
    def __init__(self, skill_name: str, config: Optional[dict] = None):
        self.skill_name = skill_name
        self.config = config or {}
        self.logger = setup_logging()
        self.recovery = ErrorRecovery(self.logger)
        self.recovery_history: List[Dict[str, Any]] = []
    
    def heal(self, exception: Exception, context: dict = None) -> RecoveryResult:
        """Attempt to heal from an exception."""
        classified = ErrorClassifier.classify(exception, context)
        
        self.logger.info(f"Healing {classified.error_type.value}: {exception}")
        
        strategies = {
            ErrorType.NETWORK: self._heal_network,
            ErrorType.RESOURCE: self._heal_resource,
            ErrorType.CONFIGURATION: self._heal_configuration,
            ErrorType.DEPENDENCY: self._heal_dependency,
        }
        
        strategy = strategies.get(classified.error_type, self._heal_generic)
        result = strategy(classified, context)
        
        self.recovery_history.append({
            "timestamp": time.time(),
            "error": str(exception),
            "error_type": classified.error_type.value,
            "result": result.action_taken,
            "success": result.success
        })
        
        return result
    
    def _heal_network(self, error: ClassifiedError, context: dict) -> RecoveryResult:
        """Heal network issues."""
        return RecoveryStrategies.cleanup_temp_files(
            ["*.tmp", "*.cache"],
            ["/tmp", "/home/user/.cache"]
        )
    
    def _heal_resource(self, error: ClassifiedError, context: dict) -> RecoveryResult:
        """Heal resource issues (disk space, memory)."""
        result = RecoveryStrategies.cleanup_temp_files(
            ["*.tmp", "*.log", "__pycache__"],
            ["/tmp", "/home/user"]
        )
        
        if not result.success:
            RecoveryStrategies.cleanup_temp_files(
                ["*"],
                ["/tmp/skill-debug-state"]
            )
        
        return result
    
    def _heal_configuration(self, error: ClassifiedError, context: dict) -> RecoveryResult:
        """Heal configuration issues."""
        config_file = f"/home/user/skills/{self.skill_name}/config.json"
        backup_file = f"/home/user/skills/{self.skill_name}/config.json.backup"
        
        if os.path.exists(backup_file):
            return RecoveryStrategies.rollback_to_backup(backup_file, config_file)
        
        default_config = self.config.get("defaults", {})
        try:
            with open(config_file, "w") as f:
                import json
                json.dump(default_config, f, indent=2)
            return RecoveryResult(
                success=True,
                action_taken="reset_config",
                message="Configuration reset to defaults"
            )
        except Exception as e:
            return RecoveryResult(
                success=False,
                action_taken="config_reset_failed",
                message=str(e)
            )
    
    def _heal_dependency(self, error: ClassifiedError, context: dict) -> RecoveryResult:
        """Heal dependency issues."""
        match = re.search(r"No module named ['\"]([^'\"]+)['\"]", str(error.message))
        if match:
            package = match.group(1)
            if not destructive_allowed():
                return _refused("reinstall", f"pip install {package!r}")
            if not _SAFE_PACKAGE_RE.match(package):
                # the name came from a regex over an error message; never hand an
                # unvalidated string to pip
                return RecoveryResult(
                    success=False,
                    action_taken="reinstall_rejected",
                    message=(f"Refused to install {package!r}: the name was parsed "
                             f"out of an error message and is not a safe "
                             f"distribution name."),
                )
            try:
                subprocess.run([
                    sys.executable, "-m", "pip", "install",
                    "--quiet", "--", package
                ], check=True, capture_output=True, timeout=300)
                return RecoveryResult(
                    success=True,
                    action_taken="reinstall",
                    message=f"Reinstalled {package}"
                )
            except Exception as e:
                return RecoveryResult(
                    success=False,
                    action_taken="reinstall_failed",
                    message=str(e)
                )
        
        return RecoveryResult(
            success=False,
            action_taken="no_action",
            message="Could not identify missing dependency"
        )
    
    def _heal_generic(self, error: ClassifiedError, context: dict) -> RecoveryResult:
        """Generic healing attempt."""
        self.logger.error(f"Generic healing attempted: {error.message}")
        return RecoveryResult(
            success=False,
            action_taken="logged",
            message="Error logged for manual review"
        )
    
    def get_health_report(self) -> dict:
        """Get health report of the healing system."""
        total = len(self.recovery_history)
        successful = sum(1 for r in self.recovery_history if r["success"])
        
        return {
            "skill": self.skill_name,
            "total_healing_attempts": total,
            "successful_healings": successful,
            "success_rate": successful / total if total > 0 else 0,
            "recent_attempts": self.recovery_history[-10:]
        }

def with_healing(healer: AutoHealer):
    """Decorator to add automatic healing to functions."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                result = healer.heal(e, {"function": func.__name__})
                if result.success:
                    try:
                        return func(*args, **kwargs)
                    except Exception as retry_error:
                        raise retry_error
                raise
        return wrapper
    return decorator

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Error Recovery Module CLI")
    subparsers = parser.add_subparsers(dest="command")
    
    heal_parser = subparsers.add_parser("heal", help="Attempt to heal an error")
    heal_parser.add_argument("error_message", help="Error message to heal")
    
    subparsers.add_parser("health", help="Show healing health report")
    
    cleanup_parser = subparsers.add_parser("cleanup", help="Clean up temporary files")
    cleanup_parser.add_argument("--skill", help="Skill name to clean up")
    cleanup_parser.add_argument("--apply", action="store_true",
                                help="Actually delete. Without this the command is a DRY RUN.")
    
    args = parser.parse_args()
    
    healer = AutoHealer("debug-enhancement-framework")
    
    # SKILL.md documents "All emit JSON on stdout" - honour that contract so a
    # calling agent can parse the result instead of scraping prose (v2.1.0).
    if args.command == "heal":
        try:
            raise Exception(args.error_message)
        except Exception as e:
            result = healer.heal(e)
            print(json.dumps({"action_taken": result.action_taken,
                              "success": result.success,
                              "message": result.message}, indent=2))
            return 0 if result.success else 1

    elif args.command == "health":
        report = healer.get_health_report()
        print(json.dumps(report, indent=2, default=str))
        return 0

    elif args.command == "cleanup":
        # SAFETY (v2.1.0): never default to bare /tmp, and never delete without
        # --apply. The old default deleted *.tmp/*.cache/__pycache__ from /tmp,
        # which belongs to every process on the box, not to this skill.
        skill = args.skill
        target = (Path(__file__).resolve().parent.parent if not skill
                  else Path.home() / "skills" / skill)
        # --apply is a real deletion, so it passes the same gate as the other
        # destructive actions (v2.1.3). Dry runs need no permission.
        apply = bool(args.apply)
        gated_out = apply and not destructive_allowed()
        if gated_out:
            apply = False
        result = RecoveryStrategies.cleanup_temp_files(
            ["**/*.tmp", "**/*.cache", "**/__pycache__"],
            [str(target)],
            dry_run=not apply,
        )
        print(json.dumps({
            "dry_run": not apply,
            "target": str(target),
            "action_taken": result.action_taken,
            "message": result.message,
            "gated": gated_out,
            "hint": (f"--apply ignored: set {ALLOW_DESTRUCTIVE_ENV}=1 to permit deletion"
                     if gated_out else
                     (None if apply else "re-run with --apply to delete")),
        }, indent=2))
        return 0
    
    else:
        parser.print_help()

if __name__ == "__main__":
    raise SystemExit(main() or 0)
