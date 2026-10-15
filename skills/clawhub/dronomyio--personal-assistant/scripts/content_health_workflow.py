#!/usr/bin/env python3
"""Content-health watchdog as a long-running Temporal workflow.

No external scheduler: one durable workflow runs forever, checks the health
of the assistant's content feeds itself, adapts its own check cadence, and
performs deterministic backfills. Query it any time for live status.

Feeds checked
-------------
* surveillance : latest Bloomberg Surveillance digest (surveillance-YYYY-MM-DD.md)
                 for the most recent expected weekday episode.
* us_brief     : us/latest.json freshness (brief engine output).
* india_brief  : india/latest.json freshness.
* job_status   : per-job ok/failed/last_run from the jobs' status.json --
                 catches failing or silently-stopped jobs, and reconciles
                 jobs whose last run failed but whose output has since
                 recovered (no false alarms).

Adaptive scheduling (the workflow owns its timing)
--------------------------------------------------
* all healthy            -> sleep HEALTHY_INTERVAL_SEC (default 3600)
* quiet hours 01:00-05:00 local and healthy -> QUIET_INTERVAL_SEC (default 10800)
* today's episode not yet posted (before POSTING_CUTOFF_HOUR local)
                         -> "pending", re-check in 60 min, no alert
* stale (with retries left) -> run backfill activities, re-check STALE_RETRY_SEC
* stale past MAX_STALE_RETRIES, or needs an agent (digest distillation)
                         -> "needs_attention": record one alert, back off to
                            HEALTHY_INTERVAL_SEC (no hot loop)

Backfills (deterministic, safe to re-run)
-----------------------------------------
* surveillance transcript fetch via surveillance_fetch.py (idempotent script).
* brief engine re-run via brief_engine.py --market <us|india> (best effort,
  BRIEF_BACKFILL_ENABLED=1).

Anything needing an LLM (digest distillation, news analysis) is surfaced as
needs_attention in the status file and queryable alerts -- never silently
dropped, never hot-looped.

Configuration: environment variables (see references/temporal-setup.md).
Stdlib + temporalio only.

Usage:
    python content_health_workflow.py worker   # run the worker (systemd does this)
    python content_health_workflow.py start    # start the watchdog workflow (idempotent)
    python content_health_workflow.py status   # query live status
    python content_health_workflow.py alerts   # query active alerts
    python content_health_workflow.py stop     # signal the workflow to stop
"""

import argparse
import asyncio
import json
import os
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.common import RetryPolicy
from temporalio.service import RPCError, RPCStatusCode
from temporalio.worker import Worker

def _script_dir() -> Path:
    # The workflow sandbox re-imports this module and blocks Path.resolve();
    # fall back to the unresolved parent there (paths are only used by
    # activities, which run outside the sandbox).
    try:
        return Path(__file__).resolve().parent
    except Exception:  # noqa: BLE001
        return Path(__file__).parent


def _home_dir() -> Path:
    try:
        return Path.home()
    except Exception:  # noqa: BLE001
        return Path(__file__).parent


SCRIPT_DIR = _script_dir()
_HOME = _home_dir()
TASK_QUEUE = os.environ.get("CONTENT_TASK_QUEUE", "content-health")
ADDRESS = os.environ.get("TEMPORAL_ADDRESS", "localhost:7233")
WORKFLOW_ID = os.environ.get("CONTENT_WORKFLOW_ID", "content-health-watchdog")

HEALTHY_INTERVAL_SEC = int(os.environ.get("HEALTHY_INTERVAL_SEC", "3600"))
QUIET_INTERVAL_SEC = int(os.environ.get("QUIET_INTERVAL_SEC", "10800"))
STALE_RETRY_SEC = int(os.environ.get("STALE_RETRY_SEC", "900"))
MAX_STALE_RETRIES = int(os.environ.get("MAX_STALE_RETRIES", "8"))
POSTING_CUTOFF_HOUR = int(os.environ.get("POSTING_CUTOFF_HOUR", "18"))  # episode expected by 18:00 local
BRIEF_STALE_HOURS = float(os.environ.get("BRIEF_STALE_HOURS", "8"))
BRIEF_BACKFILL_ENABLED = os.environ.get("BRIEF_BACKFILL_ENABLED", "1") == "1"
TIMEZONE = os.environ.get("TIMEZONE", "America/Los_Angeles")
ITERATIONS_BEFORE_CONTINUE = int(os.environ.get("ITERATIONS_BEFORE_CONTINUE", "500"))

BRIEFS_DIR = Path(os.environ.get("BRIEFS_DIR", str(_HOME / "briefs")))
SURVEILLANCE_DIR = Path(os.environ.get("SURVEILLANCE_DIR", str(BRIEFS_DIR / "us")))
SURVEILLANCE_FETCH_SCRIPT = Path(
    os.environ.get("SURVEILLANCE_FETCH_SCRIPT", str(SCRIPT_DIR / "surveillance_fetch.py"))
)
BRIEF_ENGINE_SCRIPT = Path(
    os.environ.get("BRIEF_ENGINE_SCRIPT", str(SCRIPT_DIR / "brief_engine.py"))
)
STATUS_FILE = Path(
    os.environ.get("HEALTH_STATUS_FILE", str(BRIEFS_DIR / "content-health-status.json"))
)
JOB_STATUS_FILE = Path(
    os.environ.get("JOB_STATUS_FILE", str(BRIEFS_DIR.parent / "news-assistant" / "status.json"))
)

# Per-job expected reporting intervals (hours). Lenient on purpose: the
# file-freshness checks above are the tight ones; this catches jobs that
# fail or go silent.
JOB_EXPECTED_HOURS = {
    "surveillance_brief": 26,
    "market_brief_us": 10,
    "market_brief_india": 10,
    "site_monitor": 26,
}
DEFAULT_JOB_EXPECTED_HOURS = 26
JOB_ALERT_WINDOW_HOURS = 24  # only alert on failures/silence within this window


# ---------------------------------------------------------------- activities

@activity.defn
async def get_time_info() -> dict:
    """Wall-clock info. Lives in an activity: workflows must stay deterministic."""
    tz = ZoneInfo(TIMEZONE)
    now = datetime.now(tz)
    return {
        "iso": now.isoformat(),
        "date": now.strftime("%Y-%m-%d"),
        "weekday": now.weekday(),  # 0=Mon
        "hour": now.hour,
        "quiet_hours": 1 <= now.hour < 5,
    }


def _most_recent_weekday(today) -> str:
    d = today
    while d.weekday() >= 5:  # Sat/Sun -> roll back to Friday
        d -= timedelta(days=1)
    return d.isoformat()


@activity.defn
async def check_surveillance(time_info: dict) -> dict:
    """Is there a digest (and transcript) for the most recent expected episode?"""
    tz = ZoneInfo(TIMEZONE)
    now = datetime.now(tz)
    expected = _most_recent_weekday(now.date())
    is_today = expected == time_info["date"]

    digest = SURVEILLANCE_DIR / f"surveillance-{expected}.md"
    transcript = SURVEILLANCE_DIR / f"surveillance-{expected}.transcript.md"
    result = {
        "feed": "surveillance",
        "expected_date": expected,
        "digest_present": digest.exists(),
        "transcript_present": transcript.exists(),
        "state": "healthy",
        "detail": "",
    }
    if digest.exists():
        return result
    if transcript.exists():
        result["state"] = "needs_attention"
        result["detail"] = (
            f"transcript for {expected} fetched but no digest -- "
            "distillation needs an agent run"
        )
        return result
    if is_today and now.hour < POSTING_CUTOFF_HOUR:
        result["state"] = "pending"
        result["detail"] = f"today's episode not posted yet (before {POSTING_CUTOFF_HOUR}:00 local)"
        return result
    result["state"] = "stale"
    result["detail"] = f"no digest or transcript for expected episode {expected}"
    return result


@activity.defn
async def backfill_surveillance_transcript() -> dict:
    """Run the idempotent transcript fetcher. Returns what it found."""
    if not SURVEILLANCE_FETCH_SCRIPT.exists():
        return {"ok": False, "detail": f"fetch script not found: {SURVEILLANCE_FETCH_SCRIPT}"}
    try:
        p = subprocess.run(
            [sys.executable, str(SURVEILLANCE_FETCH_SCRIPT), "--out-dir", str(SURVEILLANCE_DIR)],
            capture_output=True, text=True, timeout=600,
        )
        out = (p.stdout or "") + (p.stderr or "")
        return {"ok": p.returncode == 0, "detail": out.strip()[-500:]}
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "detail": f"fetch failed: {e}"}


@activity.defn
async def check_brief(market: str) -> dict:
    """Is <market>/latest.json fresh?"""
    latest = BRIEFS_DIR / market / "latest.json"
    result = {"feed": f"{market}_brief", "state": "healthy", "detail": "", "age_hours": None}
    if not latest.exists():
        result["state"] = "stale"
        result["detail"] = f"{latest} does not exist"
        return result
    age_h = (datetime.now().timestamp() - latest.stat().st_mtime) / 3600
    result["age_hours"] = round(age_h, 1)
    if age_h > BRIEF_STALE_HOURS:
        result["state"] = "stale"
        result["detail"] = f"latest.json is {age_h:.1f}h old (threshold {BRIEF_STALE_HOURS}h)"
    return result


@activity.defn
async def backfill_brief(market: str) -> dict:
    """Best-effort re-run of the brief engine (data refresh; analysis still
    comes from the scheduled brief runs)."""
    if not BRIEF_BACKFILL_ENABLED:
        return {"ok": False, "detail": "BRIEF_BACKFILL_ENABLED=0"}
    if not BRIEF_ENGINE_SCRIPT.exists():
        return {"ok": False, "detail": f"engine not found: {BRIEF_ENGINE_SCRIPT}"}
    try:
        p = subprocess.run(
            [sys.executable, str(BRIEF_ENGINE_SCRIPT), "--market", market],
            capture_output=True, text=True, timeout=900,
        )
        out = (p.stdout or "") + (p.stderr or "")
        return {"ok": p.returncode == 0, "detail": out.strip()[-500:]}
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "detail": f"engine run failed: {e}"}


def _parse_iso(s) -> datetime | None:
    try:
        dt = datetime.fromisoformat(str(s).replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=ZoneInfo(TIMEZONE))
        return dt
    except Exception:  # noqa: BLE001
        return None


@activity.defn
async def check_job_status(surveillance_state: dict) -> dict:
    """Read the jobs' status.json: flag failed runs and jobs gone silent.

    Reconciles false alarms: a job whose last run failed but whose output
    has since recovered (e.g. surveillance digest backfilled) is reported
    healthy with a note, not an alert.
    """
    result = {"feed": "job_status", "state": "healthy", "detail": "", "jobs": {}}
    try:
        data = json.loads(JOB_STATUS_FILE.read_text())
    except Exception as e:  # noqa: BLE001
        result["state"] = "needs_attention"
        result["detail"] = f"cannot read {JOB_STATUS_FILE}: {e}"
        return result
    now = datetime.now(ZoneInfo(TIMEZONE))
    for key, val in data.items():
        if key in ("_note", "jobs") or not isinstance(val, dict):
            continue
        last_run = _parse_iso(val.get("last_run"))
        res = str(val.get("result", "")).lower()
        summary = str(val.get("summary", ""))[:200]
        age_h = (now - last_run).total_seconds() / 3600 if last_run else None
        expected_h = JOB_EXPECTED_HOURS.get(key, DEFAULT_JOB_EXPECTED_HOURS)
        state, detail = "healthy", ""
        if res == "failed":
            if key == "surveillance_brief" and surveillance_state.get("digest_present"):
                detail = (f"last run failed but digest for "
                          f"{surveillance_state.get('expected_date')} now exists (recovered)")
            elif age_h is not None and age_h <= JOB_ALERT_WINDOW_HOURS:
                state = "needs_attention"
                detail = f"failed {age_h:.1f}h ago: {summary}"
            else:
                detail = f"old failure ({age_h:.1f}h ago, outside alert window)" if age_h else "old failure"
        elif age_h is not None and age_h > expected_h:
            state = "needs_attention"
            detail = f"no run in {age_h:.1f}h (expected every ~{expected_h}h)"
        result["jobs"][key] = {
            "state": state,
            "result": res,
            "age_hours": round(age_h, 1) if age_h is not None else None,
            "detail": detail,
        }
    if any(j["state"] == "needs_attention" for j in result["jobs"].values()):
        result["state"] = "needs_attention"
    return result


@activity.defn
async def write_status(status: dict) -> dict:
    """Persist the health snapshot where dashboards and humans can read it."""
    try:
        STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
        STATUS_FILE.write_text(json.dumps(status, indent=2))
        return {"ok": True, "path": str(STATUS_FILE)}
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "detail": str(e)}


# ---------------------------------------------------------------- workflow

@workflow.defn
class ContentHealthWorkflow:
    """One long-running workflow. It decides when to check next -- no cron."""

    def __init__(self) -> None:
        self._stop = False
        self._alerts: list = []
        self._alert_keys: set = set()
        self._stale_counts: dict = {}
        self._iteration = 0

    @workflow.signal
    def stop(self) -> None:
        self._stop = True

    @workflow.query
    def get_status(self) -> dict:
        return getattr(self, "_status", {"state": "starting"})

    @workflow.query
    def get_alerts(self) -> list:
        return list(self._alerts)

    def _record_alert(self, key: str, text: str) -> None:
        if key in self._alert_keys:
            return
        self._alert_keys.add(key)
        self._alerts.append({"key": key, "text": text})
        self._alerts = self._alerts[-50:]

    @workflow.run
    async def run(self, params: dict) -> None:
        self._alerts = params.get("prior_alerts", [])
        self._alert_keys = {a["key"] for a in self._alerts}
        retry_policy = RetryPolicy(maximum_attempts=3)
        while not self._stop:
            self._iteration += 1
            ti = await workflow.execute_activity(
                get_time_info, schedule_to_close_timeout=timedelta(seconds=60),
                retry_policy=retry_policy,
            )
            surv, us, india = await asyncio.gather(
                workflow.execute_activity(
                    check_surveillance, ti, schedule_to_close_timeout=timedelta(seconds=120),
                    retry_policy=retry_policy),
                workflow.execute_activity(
                    check_brief, "us", schedule_to_close_timeout=timedelta(seconds=120),
                    retry_policy=retry_policy),
                workflow.execute_activity(
                    check_brief, "india", schedule_to_close_timeout=timedelta(seconds=120),
                    retry_policy=retry_policy),
            )
            js = await workflow.execute_activity(
                check_job_status, surv, schedule_to_close_timeout=timedelta(seconds=120),
                retry_policy=retry_policy,
            )
            feeds = {"surveillance": surv, "us_brief": us, "india_brief": india,
                     "job_status": js}
            actions_taken = []

            # --- deterministic remediation where possible
            if surv["state"] == "stale":
                key = f"surv-{surv['expected_date']}"
                count = self._stale_counts.get(key, 0)
                if count < MAX_STALE_RETRIES:
                    self._stale_counts[key] = count + 1
                    r = await workflow.execute_activity(
                        backfill_surveillance_transcript,
                        schedule_to_close_timeout=timedelta(seconds=660),
                        retry_policy=RetryPolicy(maximum_attempts=2),
                    )
                    actions_taken.append(f"surveillance transcript backfill: ok={r['ok']}")
                else:
                    self._record_alert(key, f"Surveillance {surv['expected_date']} still missing after "
                                           f"{MAX_STALE_RETRIES} backfill retries: {surv['detail']}")
            elif surv["state"] == "needs_attention":
                self._record_alert(f"surv-distill-{surv['expected_date']}", surv["detail"])
            else:
                self._stale_counts.pop(f"surv-{surv['expected_date']}", None)

            for market, chk in (("us", us), ("india", india)):
                if chk["state"] == "stale":
                    key = f"brief-{market}-{ti['date']}"
                    count = self._stale_counts.get(key, 0)
                    if count < MAX_STALE_RETRIES:
                        self._stale_counts[key] = count + 1
                        r = await workflow.execute_activity(
                            backfill_brief, market,
                            schedule_to_close_timeout=timedelta(seconds=960),
                            retry_policy=RetryPolicy(maximum_attempts=2),
                        )
                        actions_taken.append(f"{market} brief backfill: ok={r['ok']}")
                    else:
                        self._record_alert(key, f"{market} brief stale: {chk['detail']}")
                else:
                    self._stale_counts.pop(f"brief-{market}-{ti['date']}", None)

            # Failing or silent jobs -> one alert each (no automated fix exists).
            if js["state"] == "needs_attention":
                for jk, jv in js["jobs"].items():
                    if jv["state"] == "needs_attention":
                        self._record_alert(f"job-{jk}-{ti['date']}",
                                           f"Job '{jk}': {jv['detail']}")

            # --- adaptive next-check interval (the workflow's own scheduling)
            states = {f["state"] for f in feeds.values()}
            retrying = any(
                self._stale_counts.get(k, 0) > 0
                for k in list(self._stale_counts)
            )
            if retrying:
                next_sleep = STALE_RETRY_SEC
                cadence = f"stale-retry ({STALE_RETRY_SEC}s)"
            elif "needs_attention" in states:
                next_sleep = HEALTHY_INTERVAL_SEC
                cadence = f"attention-backoff ({HEALTHY_INTERVAL_SEC}s)"
            elif ti["quiet_hours"] and states == {"healthy"}:
                next_sleep = QUIET_INTERVAL_SEC
                cadence = f"quiet-hours ({QUIET_INTERVAL_SEC}s)"
            elif "pending" in states and states <= {"healthy", "pending"}:
                next_sleep = HEALTHY_INTERVAL_SEC
                cadence = f"pending ({HEALTHY_INTERVAL_SEC}s)"
            else:
                next_sleep = HEALTHY_INTERVAL_SEC
                cadence = f"healthy ({HEALTHY_INTERVAL_SEC}s)"

            self._status = {
                "checked_at": ti["iso"],
                "iteration": self._iteration,
                "feeds": feeds,
                "cadence": cadence,
                "next_check_in_sec": next_sleep,
                "actions_taken": actions_taken,
                "alerts": list(self._alerts),
                "workflow": "ContentHealthWorkflow",
            }
            await workflow.execute_activity(
                write_status, self._status,
                schedule_to_close_timeout=timedelta(seconds=60),
                retry_policy=retry_policy,
            )

            # Bound history size: continue as new periodically, carrying alerts.
            if self._iteration >= ITERATIONS_BEFORE_CONTINUE:
                workflow.continue_as_new(ContentHealthWorkflow.run, {"prior_alerts": self._alerts[-50:]})

            await asyncio.sleep(next_sleep)


# ---------------------------------------------------------------- entrypoints

async def _client() -> Client:
    return await Client.connect(ADDRESS)


async def run_worker() -> None:
    client = await _client()
    worker = Worker(
        client,
        task_queue=TASK_QUEUE,
        workflows=[ContentHealthWorkflow],
        activities=[
            get_time_info, check_surveillance, backfill_surveillance_transcript,
            check_brief, backfill_brief, check_job_status, write_status,
        ],
    )
    print(f"worker on {ADDRESS}, task queue '{TASK_QUEUE}'", flush=True)
    await worker.run()


async def start_workflow() -> None:
    from temporalio.client import WorkflowExecutionStatus
    client = await _client()
    try:
        handle = client.get_workflow_handle(WORKFLOW_ID)
        desc = await handle.describe()
        if desc.status == WorkflowExecutionStatus.RUNNING:
            print(f"workflow {WORKFLOW_ID} already running")
            return
        print(f"previous run is {desc.status.name}; starting a new one")
    except RPCError as e:
        if e.status != RPCStatusCode.NOT_FOUND:
            raise
    handle = await client.start_workflow(
        ContentHealthWorkflow.run, {"prior_alerts": []},
        id=WORKFLOW_ID, task_queue=TASK_QUEUE,
    )
    print(f"started {WORKFLOW_ID} ({handle.id})")


async def query_status() -> None:
    client = await _client()
    handle = client.get_workflow_handle(WORKFLOW_ID)
    print(json.dumps(await handle.query(ContentHealthWorkflow.get_status), indent=2))


async def query_alerts() -> None:
    client = await _client()
    handle = client.get_workflow_handle(WORKFLOW_ID)
    print(json.dumps(await handle.query(ContentHealthWorkflow.get_alerts), indent=2))


async def stop_workflow() -> None:
    client = await _client()
    handle = client.get_workflow_handle(WORKFLOW_ID)
    await handle.signal(ContentHealthWorkflow.stop)
    print(f"signalled stop to {WORKFLOW_ID}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Content-health Temporal watchdog")
    ap.add_argument("cmd", choices=["worker", "start", "status", "alerts", "stop"])
    args = ap.parse_args()
    cmds = {"worker": run_worker, "start": start_workflow, "status": query_status,
            "alerts": query_alerts, "stop": stop_workflow}
    asyncio.run(cmds[args.cmd]())


if __name__ == "__main__":
    main()
