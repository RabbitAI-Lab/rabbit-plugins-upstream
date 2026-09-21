## Description:

Unified backlog lifecycle management and task tracking for session TODOs, workspace checklists, and issue trackers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to triage, prioritize, synchronize, prune, create, and comment on backlog work across local task files and external issue trackers such as Plane.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mutate Plane tracker data and includes automatic Kubernetes/Django-shell fallbacks that may bypass normal Plane API authorization.

Mitigation: Install only in controlled Plane/K3s environments; withhold kubectl, ssh, and kubeconfig access from ordinary agent sessions, require operator confirmation for fallback paths, and prefer scoped Plane API tokens.

Risk: Backlog automation can change local task files or external issue states if run with broad credentials.

Mitigation: Review planned changes before execution, use dry-run or verification steps where available, and grant only project-scoped tracker permissions.

## Reference(s):

- [Backlog skill page](https://clawhub.ai/drumrobot/skills/backlog)
- [Skill definition](artifact/SKILL.md)
- [Create guide](artifact/create.md)
- [Comment guide](artifact/comment.md)
- [Prune guide](artifact/prune.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, script outputs, and JSON responses from tracker operations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update local backlog files or Plane tracker records when configured with credentials and execution access.]

## Skill Version(s):

0.4.0 (source: server release metadata and CHANGELOG, released 2026-09-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
