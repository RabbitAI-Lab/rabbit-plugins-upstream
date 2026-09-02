## Description:

Unified backlog lifecycle management and task tracking across session TODOs, local checklist files, and issue trackers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to capture, triage, synchronize, create, comment on, and prune backlog items across local markdown trackers and external issue trackers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mutate local backlog files and external issue tracker state.

Mitigation: Use it only in workspaces where those edits and tracker mutations are intended, and review dry-run or summary output before applying changes.

Risk: Plane create and update failures may trigger Kubernetes/Django shell fallback using local cluster credentials or SSH configuration.

Mitigation: Disable or remove the fallback for normal use, or require explicit approval and tightly scoped credentials before allowing it.

Risk: Issue tracker operations depend on configured API tokens and workspace profiles.

Mitigation: Provide least-privilege tokens and confirm the target workspace, project, and tracker file before running create, sync, or prune workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/backlog)
- [Changelog](CHANGELOG.md)
- [Comment topic guide](comment.md)
- [Create topic guide](create.md)
- [Prune topic guide](prune.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May edit local backlog files and call configured issue tracker APIs when invoked with the relevant workflows.]

## Skill Version(s):

0.2.0 (source: server release metadata, target metadata, and changelog released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
