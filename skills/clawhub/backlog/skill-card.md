## Description:

Unified backlog lifecycle management and task tracking across session TODOs, workspace checklist files, and issue trackers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to capture, triage, synchronize, prioritize, prune, and comment on backlog items across local markdown work plans and external issue trackers such as Plane.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can manage Plane tracker data and local backlog files.

Mitigation: Install and run it only where that level of backlog mutation is intended, and review proposed file or tracker changes before applying them.

Risk: The scanner reports automatic privileged Kubernetes/Django-shell fallbacks that can bypass normal Plane API permissions and mutate tracker data.

Mitigation: Run without kubectl exec or SSH access unless an operator explicitly approves that path, and prefer removing or disabling the K3s/Django-shell fallbacks.

Risk: Plane API credentials may permit issue, intake, comment, synchronization, or update workflows.

Mitigation: Use least-privilege Plane API credentials scoped to the intended workspace and project.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/backlog)
- [Backlog skill definition](artifact/SKILL.md)
- [Create Plane issue and intake guide](artifact/create.md)
- [Comment on Plane issue guide](artifact/comment.md)
- [Prune P2/P3 backlog guide](artifact/prune.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, JSON, API calls, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update local backlog files and create or update Plane issues/comments when invoked with configured credentials.]

## Skill Version(s):

0.4.1 (source: server release metadata and CHANGELOG, released 2026-09-24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
