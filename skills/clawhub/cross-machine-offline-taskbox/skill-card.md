## Description:

Helps users manage and synchronize offline tasks across machines and process queued tasks with a local Ollama model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); skill documentation and theory all rights reserved

## Use Case:

Developers and other users can queue tasks locally, exchange JSON sync packages between machines, and process queued work with a locally installed Ollama model when offline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Task details, including secrets, may remain in the local taskbox and exported sync packages.

Mitigation: Do not add sensitive details unless local storage and sharing the exported packages are acceptable.

Risk: Broad trigger words may activate this skill outside its intended taskbox workflow.

Mitigation: Invoke it for specific offline taskbox or local-worker requests rather than generic trigger words.

## Reference(s):

- [Cross-Machine Offline Taskbox on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/cross-machine-offline-taskbox)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Plain text or Markdown with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task results can be stored in a local JSON taskbox and included in exported sync packages.]

## Skill Version(s):

2.2.4 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
