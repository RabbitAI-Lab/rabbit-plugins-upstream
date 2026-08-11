# Post-Mortem Report Template

Fill in every section. If a section doesn't apply, write "N/A — [reason]" rather than deleting it. A blank section is information; a missing section is ambiguity.

---

# Post-Mortem: [TITLE]

**Date:** YYYY-MM-DD
**Author:** [agent name / human name]
**Task:** [one-line description of what the agent was trying to do]
**Status:** [Failed / Partially completed / Recovered after intervention]

## Summary

[One paragraph, plain language. Describe what happened, not just that it failed. A reader who wasn't present should understand the failure and its impact from this paragraph alone. Aim for 3-5 sentences.]

**Failure category:** [network / permissions / logic / environment / dependency / resource / uncategorized]

## Timeline

Reconstruct the sequence of events leading to the failure. Use timestamps from logs where available. Mark the failure point explicitly with **[FAILURE]**.

| Time (UTC) | Event | Outcome |
|---|---|---|
| 10:23:01 | Agent received task: "Deploy service to staging" | Task started |
| 10:23:15 | Agent ran `git pull origin main` | Success |
| 10:23:45 | Agent ran `npm install` | **[FAILURE]** — EACCES: permission denied |
| 10:24:02 | Agent retried `npm install` with `sudo` | Different error: EACCES on different path |
| 10:24:30 | Agent abandoned task | Task failed |

If using the forensics script, paste the generated timeline here.

## Impact

- **What was affected:** [services, data, users, downstream tasks]
- **Severity:** [low / medium / high / critical]
- **Duration of impact:** [how long the system was in a bad state, if applicable]
- **Data loss:** [yes/no — if yes, what and how much]
- **Recovery actions taken:** [what was done to restore service, if anything]

## Root Cause

[The terminal link of the causal chain. State this plainly and specifically. This should be a single, clear sentence that explains *why* the failure happened at the deepest level you could trace.]

**Example (bad):** "npm install failed."
**Example (good):** "The agent ran as a non-root user in a container where the global npm directory (`/usr/lib/node_modules`) was owned by root with no write permission for others, and `npm install` without `--prefix` defaults to global installation."

## Causal Chain

Trace backward from the failure point. Each entry should answer "why did the previous step happen/ matter?"

1. **[FAILURE]** `npm install` returned EACCES on `/usr/lib/node_modules`
2. **Because:** npm attempted a global install (no `--prefix` or local `package.json`)
3. **Because:** The agent assumed the install target was local, but the working directory had no `package.json`
4. **Because:** The agent didn't verify the working directory contents before running the install
5. **Because:** The task description referenced a project at a path the agent assumed existed without checking ← **ROOT CAUSE**

**Root cause:** The agent operated on an unverified assumption about the filesystem state (project path) and cascaded into a permissions failure that looked like an environment problem.

## Contributing Factors

Factors that didn't *cause* the failure but made it worse or harder to diagnose:

- **Retry without analysis:** The agent retried with `sudo` before understanding the error, introducing a new failure mode and obscuring the original cause.
- **Poor error context:** npm's error message mentioned the path but not that it was a global vs. local install distinction.
- **No pre-flight check:** No step verified the working directory contained the expected project files.

## What Went Well

[Post-mortems that only list problems create a blame culture. Note what worked — fast detection, good logging, graceful degradation, etc.]

- The agent correctly abandoned the task after two failures rather than continuing to cascade.
- Tool-call logs captured the full error messages, enabling this analysis.

## Action Items

Each item must be **specific, assigned, and verifiable**.

| # | Action | Owner | Verification | Priority |
|---|---|---|---|---|
| 1 | Add a pre-flight check: verify `package.json` exists in the working directory before running `npm install` | agent framework team | Unit test: `test_npm_install_requires_package_json` passes | High |
| 2 | Add `--prefix` flag to npm install commands by default, or detect global vs. local context | agent framework team | Manual: run in a dir without package.json, confirm error is actionable | Medium |
| 3 | Add retry-with-analysis rule to agent: after first failure, perform Phase 1 triage before retrying | this skill | Verify `failure-forensics` skill is loaded and triggered on retry | High |

## Lessons Learned

Generalizable insights. These are the durable output of the post-mortem — they should apply beyond this specific incident.

1. **Verify assumptions about filesystem state before acting.** "The project is at this path" is an assumption, not a fact. `ls` or `test -f` is cheap; cascading failures are expensive.
2. **Retry is not a debugging strategy.** Retrying without analysis can introduce new failure modes and destroy evidence of the original cause.
3. **Permission errors often mask environment/context errors.** A permissions failure at the symptom level may have a logic or assumption failure at the root.
4. **Error messages rarely point at the root cause directly.** They point at the *symptom*. Always read them as clues, not diagnoses.

## Appendix

### Full Error Output

```
[Paste the complete error message / stack trace / log output here]
```

### Environment

- **OS:** [e.g., Ubuntu 22.04 x86_64]
- **Agent runtime:** [e.g., Hermes Agent v2.3]
- **Key dependencies:** [versions of relevant tools]
- **Working directory:** [path]

### References

- [Links to related issues, PRs, prior post-mortems, docs]
