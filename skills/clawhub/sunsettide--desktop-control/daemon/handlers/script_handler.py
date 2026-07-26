"""
Handler wrappers for script execution.

Supports:
  - script_run:      Submit a script for async execution (returns immediately)
  - script_run_sync: Execute a script synchronously (blocks until done)
  - script_status:   Query progress of a running script
  - script_results:  Get full results of a completed script
  - script_cancel:   Request cancellation of a running script
"""
from daemon.script_engine.engine import (
    execute_script,
    execute_script_async,
    get_script_status,
    get_script_results,
    cancel_script,
    shutdown_task_manager,
)


def handle_script_run(params):
    """Submit a script for async execution. Returns immediately.

    Params:
        script: dict with 'steps' list and optional 'variables' dict

    Returns:
        {"task_id": "...", "status": "running", "total_steps": N}
    """
    script = params.get("script")
    if not script:
        raise ValueError(
            "Missing required parameter 'script' for script_run. "
            "Provide a script object with 'steps' array."
        )
    steps = script.get("steps", [])
    if not steps:
        raise ValueError("Script must contain at least one step.")

    result = execute_script_async(script)
    return result


def handle_script_run_sync(params):
    """Execute a script synchronously. Blocks until done.

    Params:
        script: dict with 'steps' list and optional 'variables' dict

    Returns:
        {"status": "completed"|"error", "results": {...}}
    """
    script = params.get("script")
    if not script:
        raise ValueError(
            "Missing required parameter 'script' for script_run_sync. "
            "Provide a script object with 'steps' array."
        )
    steps = script.get("steps", [])
    if not steps:
        raise ValueError("Script must contain at least one step.")

    result = execute_script(script)
    return result


def handle_script_status(params):
    """Query the current progress of a running script task.

    Params:
        task_id: the task id from script_run

    Returns:
        {"task_id": "...", "status": "running"|"completed"|"error"|"cancelled",
         "progress": N, "total": M, "error": "..." (if errored),
         "failed_at": "..." (if errored)}
    """
    task_id = params.get("task_id")
    if not task_id:
        raise ValueError("Missing required parameter 'task_id' for script_status.")

    status = get_script_status(task_id)
    if status is None:
        raise ValueError(f"Script task '{task_id}' not found.")
    return status


def handle_script_results(params):
    """Get the full results of a completed script task.

    Params:
        task_id: the task id from script_run

    Returns:
        For a completed task: {"status": "completed"|"error",
            "results": {step_id: result}, ...}
        For a running task: {"status": "running", "progress": N, "total": M}
    """
    task_id = params.get("task_id")
    if not task_id:
        raise ValueError("Missing required parameter 'task_id' for script_results.")

    results = get_script_results(task_id)
    if results is None:
        raise ValueError(f"Script task '{task_id}' not found.")
    return results


def handle_script_cancel(params):
    """Request cancellation of a running script.

    Params:
        task_id: the task id from script_run

    Returns:
        {"task_id": "...", "cancelled": True|False}
    """
    task_id = params.get("task_id")
    if not task_id:
        raise ValueError("Missing required parameter 'task_id' for script_cancel.")

    ok = cancel_script(task_id)
    return {"task_id": task_id, "cancelled": ok}
