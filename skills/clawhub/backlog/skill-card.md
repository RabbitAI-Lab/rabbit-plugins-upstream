## Description:

Manages development backlogs across session tasks, workspace checklists, and issue trackers, including triage, synchronization, pruning, and issue updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and project teams use this skill to track and prioritize work across local checklists and shared issue trackers, create or comment on issues, and keep backlog status current.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: When normal API access fails, automatic privileged fallbacks may change Plane data directly through Kubernetes or SSH.

Mitigation: Use only in an approved workspace; avoid production kubeconfig or SSH access unless the fallback is explicitly intended and supervised.

Risk: Issue creation, comments, updates, and local tracker edits can change shared or workspace records.

Mitigation: Review intended tracker changes and target workspace before allowing write operations.

## Reference(s):

- [Backlog skill](https://clawhub.ai/drumrobot/skills/backlog)
- [Issue creation guide](create.md)
- [Comment guide](comment.md)
- [Pruning guide](prune.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown summaries and checklist updates; commands and JSON issue results when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update local tracker files and create or modify Plane issues.]

## Skill Version(s):

0.4.2 (source: server release; artifact CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
