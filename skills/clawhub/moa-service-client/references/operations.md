# MOA Operations and Failure Playbook

Use this reference for a first production run, an end-to-end acceptance test, a model-routing change, or a failed workflow. Ordinary callers that only consume an already stable service can follow `AGENT_GUIDE.md` without administering models.

## Validated production baseline

The following route completed the full ten-invocation workflow against `biwin-cowork` commit `2225aea7cb6c4df549aa84abe7f731ef6778a32a` on run `MOA-7` with zero retries:

| Route | Model |
| --- | --- |
| Agent A (`research_a`, `design_a`) | `glm-5.2` |
| Agent B (`research_b`, `design_b`) | `qwen3.8-max` |
| Agent C (`research_c`, `design_c`) | `deepseek-v4-pro` |
| Research Merge | `gpt-5.5` |
| Project Analysis | `gpt-5.5` |
| Judge | `gpt-5.5` |
| Cases | `gpt-5.5` |

This is a known-good baseline, not a permanent model requirement. A route change is allowed, but it invalidates this evidence and needs a new end-to-end run.

The successful run reached `READY_FOR_REVIEW` in about 28 minutes, produced all six standard artifacts, and recorded ten successful `attempt-1` invocations. Its package hash was `910bdce1b1e400f0a032d2aac494738ad01337b2416b9a04aa7a4e6bfb9ed29b`.

## Operator preflight after deployment or routing changes

1. Run `python scripts/moa_client.py doctor`. Require `/ready` to report `db`, `repo_cache`, and `claude_code` ready, with `runnerBackend=claude-code` for a production-model test.
2. Refresh and inspect the model catalog only when authorized:

   ```text
   python scripts/moa_client.py models --refresh
   ```

   Model catalog contents are in-memory and may be empty immediately after a Pod restart until refreshed. Confirm every routed model appears in the refreshed catalog.
3. Run a fixed test for each distinct routed model:

   ```text
   python scripts/moa_client.py fixed-test --model <model-name>
   ```

   This catches unavailable aliases and basic gateway failures, but it is not a formal-Profile compatibility test.
4. Submit a real but bounded design using a fixed repository commit. Persist the new `designId`; do not judge a changed route by an older run because model routing is snapshotted when a run is created.
5. Poll through the entire workflow. Research success alone is insufficient; require `READY_FOR_REVIEW`, six artifacts, verified hashes, and `retries=0` for the cleanest acceptance evidence.

## Current stage budgets

These are server-side hard ceilings, not expected durations:

| Stage | Budget | Timeout retry |
| --- | ---: | --- |
| Research A/B/C | 60 minutes per parallel path | No |
| Research Merge | 20 minutes | No |
| Project Analysis | 24 minutes | No |
| Design A/B/C | 90 minutes per parallel path | No |
| Judge | 30 minutes | No |
| Cases | 24 minutes | No |

Spawn failure, abnormal process exit, and output/schema errors may still retry once. Use `python scripts/moa_client.py runs <designId>` to inspect sanitized invocation IDs, models, durations, retry count, exit codes, and error categories.

## Evidence-based failure handling

### Repository preparation failure

- `REPO_UNREACHABLE`, clone/fetch errors, or commit mismatch happen before model work.
- Verify the exact URL and SHA, then test from the MOA Pod/network, not only from the caller's workstation.
- A caller-side `git ls-remote` proves caller reachability only.
- Do not keep resubmitting the same repository when the Pod cannot clone it.

### Timeout

- `TIMEOUT` now ends at `attempt-1`; it does not receive another identical time budget.
- Compare actual duration with the effective stage budget shown by the admin overview.
- Increase only the stage demonstrated to be too short. Do not multiply all budgets without evidence.

### Immediate non-zero exit

If one route exits non-zero twice within a few seconds while peer routes run normally:

1. Refresh the model catalog and confirm the alias exists.
2. Run the fixed model test.
3. Remember that a passing fixed test uses a tool-free low-effort Profile without the formal output Schema. It does not eliminate incompatibility with `effort=high`, tools, or `--json-schema`.
4. Switch only the failing route to a known-compatible model, save the complete seven-route configuration, and create a new run.

Observed example: `kimi-k2.7-code` passed the fixed `CC_SERVICE_OK` test but both formal `research_c` attempts exited with code 1 in about three seconds. Replacing Agent C with `deepseek-v4-pro` produced successful Research and Design outputs in the next full run.

### Format or schema failure

- The service may retry once using the stage retry Prompt.
- If attempt 2 fails, retain `parseFailed`/`validationFailed` evidence and do not treat partial output as an official artifact.

## Success record

For a defensible handoff, report:

- `designId`, version, terminal status, wall-clock duration, and `packageHash`;
- exact repository names, URLs, and commit SHAs;
- stage/model/duration table and retry count;
- artifact names, URLs, and verified SHA-256 values;
- any catalog refresh or routing change performed before the run.

Do not report summed invocation duration as wall-clock duration: Research and Design lanes run in parallel.
