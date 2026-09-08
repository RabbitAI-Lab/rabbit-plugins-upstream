## Description:

Track per-project Claude usage estimates and local GPU budgets, preview admission, atomically reserve capacity, and reconcile actual usage with a local dashboard.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use Butler to manage local project budgets, preview token and GPU admission, reserve GPU capacity before launch, and reconcile measured usage after work completes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing from a floating command or unreviewed remote source can make the executed skill differ from the reviewed release.

Mitigation: Install from a reviewed commit or local clone, and inspect the repository before using network-based installation.

Risk: The skill can handle sensitive local budgeting state, transcripts, local process data, and optional SSH-collected usage evidence.

Mitigation: Use a dedicated private BUTLER_ROOT, keep the dashboard on loopback, avoid running as root, and enable transcript, process, or SSH collection only for machines and data you control.

Risk: Admission checks are advisory and missing GPU limits are not a cap.

Mitigation: Configure explicit limits from budget-owner authority, reserve with a stable idempotency key before launch, and reconcile actual terminal usage afterwards.

Risk: Cached provider usage can be stale and Claude weighted-token estimates are not actual Codex quota.

Mitigation: Report unavailable or stale evidence as such, and do not treat cached utilization or local estimates as fresh provider quota.

## Reference(s):

- [Butler README](README.md)
- [Accounting contract](references/accounting.md)
- [Butler ClawHub skill page](https://clawhub.ai/antreasantoniou/skills/butler-agent-skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local files under a user-selected BUTLER_ROOT; the skill itself does not launch compute, bill a provider, or enforce provider-side budget caps.]

## Skill Version(s):

1.0.0 (source: release metadata and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
