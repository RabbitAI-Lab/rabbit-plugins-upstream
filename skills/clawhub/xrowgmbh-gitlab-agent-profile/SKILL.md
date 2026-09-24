---
name: "gitlab-agent-profile"
description: "Maintain the GitLab agent profile page and static contribution performance chart."
metadata: { "openclaw": { "requires": { "bins": ["glab", "python3"] }, "primaryEnv": "GITLAB_TOKEN" } }
---

# GitLab Agent Profile Skill

Use this skill to keep the GitLab Agent profile assets current with monthly contribution performance statistics.

Your profile's location is `https://<gitlab-instance>/<gitlab-username>/<gitlab-username>.git`.

## Goal

Maintain static profile assets for the agent with:

* Static SVG and WebP chart files showing the last 12 completed calendar months of merged merge requests, owner direct commits to each project's default branch, and contribution score.
* Categories for owner-authored work, agent-authored work with owner review/merge, agent-authored work without owner review/merge, and the combined total.
* A legend and bar labels with the exact counts behind the chart.
* A JSON proof file with public counted records sorted by date descending and anonymized monthly totals for private/internal activity.

## Daily update routine

* [ ] Check GitLab auth works
* [ ] Run `{baseDir}/scripts/update-profile-stats.py` helper.
* [ ] Verify the completed-month range, project coverage, and monthly counts/scores against the public records plus private monthly totals. API errors must leave the previous assets unpublished.
* [ ] Commit and push the assets in the `assets/` folder, if they changed.

## Inputs

The script accepts these environment variables:

* `GITLAB_AGENT_PROFILE_CHART_OUTPUT`: Static SVG chart file to update. Defaults to `assets/gitlab-agent-profile.svg`.
* `GITLAB_AGENT_PROFILE_WEBP_OUTPUT`: Static WebP chart file to update. Defaults to `assets/gitlab-agent-profile.webp`.
* `GITLAB_AGENT_PROFILE_RECORDS_OUTPUT`: JSON proof file to update. Defaults to `assets/gitlab-agent-profile-records.json`.
* `GITLAB_AGENT_PROFILE_WORKSPACE`: Workspace root used for relative output paths. Defaults to the current directory.
* `GITLAB_AGENT_PROFILE_ROOT_GROUP`: Group path to discover recursively, also used to expand short project names. Defaults to `xrow-public`.
* `GITLAB_AGENT_PROFILE_PROJECTS`: Optional space, comma, or newline separated project paths or names. When unset or blank, discover all accessible projects owned by the root group and its subgroups, including archived projects. Exclude projects merely shared into the group. A nonempty value overrides discovery.
* `GITLAB_AGENT_PROFILE_AGENT_USERNAME`: Agent username. Defaults to the authenticated `glab` user.
* `GITLAB_AGENT_PROFILE_OWNER_USERNAME`: Owner username. Defaults to `xrow`.
* `GITLAB_AGENT_PROFILE_MONTHS`: Positive number of completed calendar months to render. Defaults to `12`; always exclude the current in-progress month, using the process's local calendar.

Relative output values are resolved from `GITLAB_AGENT_PROFILE_WORKSPACE`.
Project names without `/` are expanded with `GITLAB_AGENT_PROFILE_ROOT_GROUP`, so `ci-tools` becomes `xrow-public/ci-tools`.

The proof file records project coverage and the completed-month period. Private/internal project names, titles, URLs, commit IDs, and reviewer details stay out of public output; their contributions are grouped by month, kind, and category in `private_monthly_totals`. Totals and contribution scores include both public and private activity. Empty repositories and disabled repository/MR features are reported in coverage. Other API or metadata failures stop collection rather than publishing partial totals.

## Classification

For merged merge requests:

* Owner: author username matches `GITLAB_AGENT_PROFILE_OWNER_USERNAME`.
* Agent + reviewer: author username matches `GITLAB_AGENT_PROFILE_AGENT_USERNAME` and the owner is a reviewer or merge user.
* Agent (autonomous): author username matches `GITLAB_AGENT_PROFILE_AGENT_USERNAME` and the owner is neither reviewer nor merge user.
* Merged total: sum of the three MR categories.
* Direct owner commits: commits on each project's default branch authored or committed by the owner that are not known MR merge/squash commits and do not start with `skip:`, `skip(...)`, `chore:`, `chore(...)`, `docs:`, `docs(...)`, or `revert`.
* MRs with `type::bug` or `type::feature` labels count toward MR totals and contribution score.
* If a merged MR has no type label, a Conventional Commit title beginning with `fix:`/`fix(...)` or `feat:`/`feat(...)` is used as a fallback type.
* MRs beginning with `skip:`, `skip(...)`, `chore:`, `chore(...)`, `docs:`, or `docs(...)` are never counted, even if they have a counted type label.
* MR contribution score: each counted MR starts at `1` point and is multiplied by its size factor.
* Size factor: `size::small` = `1`, `size::medium` = `2`, `size::large` = `3`, `size::xlarge` = `5`; missing size labels default to `1`.
* Direct owner commits count `0.2` point each.

The script ignores merge requests authored by other users. The legacy `direct_owner_main` JSON field and `owner_direct_main` category now represent direct commits on the project's default branch.

Run `python3 {baseDir}/scripts/test_profile_stats.py` to verify group pagination, explicit overrides, non-main branches, private-data redaction, and complete-month boundaries.

## Bootstrap

* [ ] Add this cron, if it existed and was enabled then leave it enabled.

```json
{
  "name": "GitLab Agent",
  "enabled": false,
  "deleteAfterRun": false,
  "schedule": {
    "kind": "every",
    "everyMs": 900000
  },
  "sessionTarget": "isolated",
  "wakeMode": "now",
  "payload": {
    "kind": "agentTurn",
    "message": "Read skill `gitlab-agent-profile` and run.",
    "thinking": "high",
    "timeoutSeconds": 3600,
    "model": "openai/gpt-5.6-sol"
  },
  "delivery": {
    "mode": "none",
    "bestEffort": false
  }
}
```
