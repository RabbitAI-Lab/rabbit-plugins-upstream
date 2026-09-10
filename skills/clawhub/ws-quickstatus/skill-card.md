## Description:

Quick workspace health check: lists workspace contents, git status, recent memory notes, and deliverable outputs in one pass.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace operators use this skill to quickly orient in a workspace at task start, verify deliverable output, and check for uncommitted changes before wrapping up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Status output can expose sensitive workspace filenames from memory notes, deliverable directories, or git status.

Mitigation: Review output before sharing it outside the workspace, especially in client, incident, or private task contexts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/ws-quickstatus)
- [DESCRIPTION.md](references/DESCRIPTION.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Plain text workspace status summary on stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No external services required; may include workspace filenames and git status details.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
