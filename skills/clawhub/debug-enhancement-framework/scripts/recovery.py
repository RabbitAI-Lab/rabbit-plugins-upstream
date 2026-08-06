#!/usr/bin/env python3
"""
Error Recovery Module - Auto-healing and recovery strategies for skills.
"""

import os
import re
import shutil
import subprocess
import sys
import time
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

class RecoveryStrategies:
    """Collection of recovery strategies for common failures."""
    
    @staticmethod
    def restart_service(service_name: str, cmd: List[str]) -> RecoveryResult:
        """Restart a service that has crashed."""
        start = time.time()
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
    def cleanup_temp_files(patterns: List[str], directories: List[str]) -> RecoveryResult:
        """Clean up temporary files that may be causing issues."""
        start = time.time()
        cleaned = 0
        
        for directory in directories:
            for pattern in patterns:
                for filepath in Path(directory).glob(pattern):
                    try:
                        if filepath.is_file():
                            filepath.unlink()
                            cleaned += 1
                        elif filepath.is_dir():
                            shutil.rmtree(filepath)
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
        """Recreate a directory that may be corrupted."""
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
        """Restore from backup."""
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
            try:
                subprocess.run([
                    sys.executable, "-m", "pip", "install",
                    "--quiet", package
                ], check=True, capture_output=True)
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
    
    args = parser.parse_args()
    
    healer = AutoHealer("debug-enhancement-framework")
    
    if args.command == "heal":
        try:
            raise Exception(args.error_message)
        except Exception as e:
            result = healer.heal(e)
            print(f"Healing result: {result.action_taken}")
            print(f"Success: {result.success}")
            print(f"Message: {result.message}")
    
    elif args.command == "health":
        report = healer.get_health_report()
        print(f"Total attempts: {report['total_healing_attempts']}")
        print(f"Successful: {report['successful_healings']}")
        print(f"Success rate: {report['success_rate']:.1%}")
    
    elif args.command == "cleanup":
        skill = args.skill or "all"
        result = RecoveryStrategies.cleanup_temp_files(
            ["*.tmp", "*.cache", "__pycache__"],
            [f"/home/user/skills/{skill}"] if skill != "all" else ["/tmp"]
        )
        print(f"Cleanup result: {result.action_taken}")
        print(f"Message: {result.message}")
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
