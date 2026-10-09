## Description:

Helps agents coordinate multi-agent work through a local shared blackboard, permission checks, budget guards, and persistent project context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jovancoding](https://clawhub.ai/user/jovancoding)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to coordinate tasks in a shared workspace, manage advisory permission grants and token budgets, and retain local project context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local coordination and audit files may expose task data or grant tokens to other workspace users.

Mitigation: Restrict access to the skill's data directory and shared blackboard to trusted users.

Risk: Permission justifications and project context can persist sensitive information locally.

Mitigation: Do not include secrets or personal information in justifications or project context.

Risk: Advisory grant tokens do not authenticate access to sensitive external services.

Mitigation: Use independent authentication and authorization for databases, payments, email, and exports.

## Reference(s):

- [Network-AI homepage](https://network-ai.org)
- [Network-AI on ClawHub](https://clawhub.ai/jovancoding/skills/network-ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Text and Markdown guidance with Python command examples and structured local state]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maintains local coordination, grant, audit, and project-context files.]

## Skill Version(s):

5.15.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
