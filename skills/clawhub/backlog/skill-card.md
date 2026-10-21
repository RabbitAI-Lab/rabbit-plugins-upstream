## Description:

Helps developers triage, prioritize, synchronize, and record work across session tasks, local checklists, and issue trackers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and teams use this skill to organize backlog work, update local plans, and create or synchronize issues in a shared tracker.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured Kubernetes or SSH fallback can directly modify the Plane backend.

Mitigation: Prefer REST-only operation; avoid granting production kubeconfig or SSH access unless backend administration is explicitly intended.

Risk: Plane API tokens permit changes to shared backlog data.

Mitigation: Review workspace profile and token settings before use, and authorize remote changes only for the intended workspace.

## Reference(s):


## Skill Output:

**Output Type(s):** [Markdown, Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance, task summaries, and issue updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update local checklist files and, when configured, remote Plane issues.]

## Skill Version(s):

0.5.0 (source: ClawHub release and CHANGELOG; bundled frontmatter says 0.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
