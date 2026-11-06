## Description:

Coordinates local multi-agent workflows through a shared blackboard, permission scoring, token-budget checks, and persistent project context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jovancoding](https://clawhub.ai/user/jovancoding)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to coordinate work in a shared local workspace, track tasks and budgets, maintain project context, and score advisory permission requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A file-link flaw can redirect changes or deletions to unintended files within the skill's data area.

Mitigation: Keep the workspace private and trusted and back up coordination state. Before sharing it with less-trusted users or agents, fix pending-file handling to reject links and enforce directory boundaries for both writes and deletion.

Risk: Sensitive material may persist in audit logs or project notes, and reused context may need review.

Mitigation: Keep secrets out of logs and project notes, review reused context, and require independent authorization for sensitive actions.

## Reference(s):

- [Network AI on ClawHub](https://clawhub.ai/jovancoding/skills/network-ai)
- [Network AI homepage](https://network-ai.org)

## Skill Output:

**Output Type(s):** [Guidance, JSON, Markdown, Files]

**Output Format:** [Text guidance and local JSON or Markdown coordination records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local workspace state persists between explicit invocations; permission scores are advisory.]

## Skill Version(s):

6.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
