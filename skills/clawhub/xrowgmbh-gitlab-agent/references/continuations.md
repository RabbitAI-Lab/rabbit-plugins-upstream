# Resume eligible work

Use this procedure in every execution cycle after gated discovery and the
changed-activity audit. Keep the discovery JSON array, the existing activity
acknowledgement checkpoint and a separate execution-state JSON file. An unchanged
item cursor says nothing about external dependency or pipeline availability.

## Select the next action

1. Run `{baseDir}/scripts/list-active-items.py` and inspect new owner/Maintainer
   instructions using the normal gates and fully paginated activity audit.
2. Run the controller below. It rereads current item state, access and assignment;
   reads explicit guards from GitLab; and returns `next`, `waiting`,
   `needs_recheck`, `excluded` and the updated execution state. Its `glab` calls
   are bounded reads, not writes. `--claim` persists scheduling history under a
   file lock using an atomic replacement. It never dispatches a pipeline itself.
3. Perform the selected action using the existing assignment, source, CI,
   deployment and review workflows. Revalidate their gates immediately before
   any external mutation; a plan is not execution authority or a CI-slot lease.
   Use one writer per MR/worktree. Do not dispatch concurrently from separate
   controllers based on an earlier capacity snapshot.
4. Replace the selected item's pending actions with its actual next steps using
   `--actions`. Keep unresolved steps pending, including after interruptions.
   Re-run the controller after each completed action or discovered wait and
   continue to the next runnable item. A blocked CI dispatch does not prevent
   independent source preparation on that item or useful work elsewhere.
5. Before ending as idle, run the controller with `--check-idle` instead of
   `--claim`. It exits `3` while any verified runnable action remains. End only
   when this check succeeds, the actual execution budget is nearly exhausted,
   or an explicit external condition prevents further safe work.
   `no_runnable_work` means no current action is runnable, not that open tickets
   are done. Complete final rediscovery/activity acknowledgement separately.

Use the actual job's timeout and remaining execution budget. Do not invent a
shorter ten- or fifteen-minute limit. A budget exit must preserve the next
continuation and its guards; it must not be reported as an idle queue.

Run from the agent workspace, replacing the absolute paths below with your
durable execution-state and current discovery files:

```bash
python3 {baseDir}/scripts/resume-work.py \
  --items /absolute/path/assigned.json \
  --state /absolute/path/execution-state.json \
  --claim
```

The first run gives eligible items without structured state an explicit
`assess-next-action` action. Read their acceptance criteria and current feedback,
then record concrete steps and guards. Bootstrap assessment does not mean the
ticket is unblocked or its implementation is complete. Existing records survive
temporarily failed lookups, exclusions and restarts; only fresh eligible items
can enter the executable plan.

Recording actions binds them to the current audited activity cursor. If that
cursor changes, the controller selects a fresh assessment instead of executing
the old plan. After the complete activity audit, use `--actions` to confirm or
replace the continuation. If the cursor is unchanged, external guards are still
refreshed; it never suppresses resumption.

Within a priority tier, the least recently selected continuation runs first.
An activity audit does not reset its age. Priority tiers remain unchanged. Pass
`--preempt <URL>` only for a new owner or active Maintainer instruction whose
authority and content you have just audited. Ineligible targets cannot re-enter
the plan through preemption. The read-only Work Queue's newest-first ordering
does not change.

## Record concrete guards

An actions file maps each currently eligible item URL to a nonempty array of
pending actions. `kind` is `assess`, `prepare`, `investigate`, `verify` or
`dispatch_ci`. The controller plans actions; it does not approve, merge, deploy
or infer that an acceptance criterion passed.

For example, save the following as `/absolute/path/actions.json`, using the
actual project, item, policy limit and prior work-root pipeline identifiers:

```json
{
  "https://gitlab.com/team/project/-/merge_requests/8": [
    {
      "id": "verify-corrected-head",
      "kind": "dispatch_ci",
      "guards": [
        {"kind": "project_ci_idle", "project_id": 42, "refs": ["main", "dev"]},
        {"kind": "agent_capacity", "limit": 2},
        {"kind": "pipeline_terminal", "project_id": 42, "pipeline_id": 9}
      ]
    },
    {"id": "prepare-independent-fix", "kind": "prepare", "guards": []}
  ]
}
```

```bash
python3 {baseDir}/scripts/resume-work.py \
  --items /absolute/path/assigned.json \
  --state /absolute/path/execution-state.json \
  --actions /absolute/path/actions.json \
  --claim
```

The dispatch remains waiting while either CI guard is false or the old root has
an active descendant. The independent preparation step can still be selected.
After the live conditions clear, the dispatch becomes runnable without any
change to the MR's notes or cursor. Do not add an unconditional preparation step
unless there is actual independent work authorized by the item.

| Guard | Required fields | Live condition |
|---|---|---|
| `issue_closed` | `project_id`, `iid` | Dependency issue is closed. Resume assessment, not deployment acceptance. |
| `mr_merged` | `project_id`, `iid` | Dependency MR is merged, not merely closed. Verify target inclusion before relying on its code. |
| `pipeline_terminal` | `project_id`, `pipeline_id` | Root and all reachable downstream pipelines are terminal. |
| `project_ci_idle` | `project_id`, `refs` | No active pipeline on the explicit branches. |
| `agent_capacity` | `limit` | Fresh global assigned-MR inventory is below the policy limit; targeted input cannot hide work roots, and children are not extra roots. |
| `activity_changed` | `baseline_cursor` | Item activity differs from the last fully audited baseline. Use an assessment action to read feedback, not an approval action. |

Take the limit and branch policy from the current project instructions, not an
old checkpoint. Add `pipeline_terminal` guards for every prior work-root
lifecycle that must drain. Unsupported external conditions need an explicit
assessment step; do not encode an unverified cached boolean or invent a guard.
For `review` or `need-human`, retain the actual human prerequisite. Independent
work may proceed, but a changed cursor or closed issue never grants approval.

## Handle incomplete checks

Exit `0` means the plan has no unknown checks. Exit `2` emits a partial JSON plan
with `needs_recheck`; independently verified actions may still be selected, but
the cycle must not claim no work remains. Exit `1` means controller/input/state
failure: preserve the existing state and diagnose it before execution.
With `--check-idle`, exit `3` means runnable work remains; exit `0` additionally
confirms no currently runnable action. This check does not mutate GitLab or
erase pending steps.

API errors, missing metadata, unknown guards, unsupported state and failed
checkpoint replacement are not successful checks. The controller does not
replace access, review, deployment, concurrency or Definition-of-Done gates.
