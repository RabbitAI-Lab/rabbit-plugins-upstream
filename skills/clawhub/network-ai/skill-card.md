## Description:

Coordinates local multi-agent workflows through a shared blackboard, budget checks, advisory permission grants, and persistent project context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jovancoding](https://clawhub.ai/user/jovancoding)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to coordinate agents in a trusted local workspace, track task budgets, share results, and carry project context between sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent project context may carry misleading instructions into later agent sessions.

Mitigation: Use a trusted local workspace and review project context before injecting it into agent prompts.

Risk: Locally stored grant tokens could be mistaken for authenticated authorization.

Mitigation: Treat grants as advisory; require separate identity checks and approval for sensitive actions.

Risk: Justifications and stored context may retain personal data or secrets on disk.

Mitigation: Avoid putting secrets or personal data in these fields and restrict access to the local data directory.

Risk: The optional server command may install an unverified package version.

Mitigation: Do not run it unless the package version is pinned and independently verified.

## Reference(s):

- [Network-AI ClawHub release](https://clawhub.ai/jovancoding/skills/network-ai)
- [Network-AI homepage](https://network-ai.org)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Files]

**Output Format:** [Markdown guidance and local command-line output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local blackboard and project-context files can persist between sessions.]

## Skill Version(s):

5.15.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
