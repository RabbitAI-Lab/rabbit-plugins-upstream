## Description:

Generate a project-local verify-<app> skill on top of e2e, so any coding agent can launch the app, check it is worth driving, exercise a feature the way a user does, keep evidence, and bug bash it. Writes the skill, a feature map with one explore charter per feature, and proves it once. Use for /create-verification-skill, "make a verification skill for this repo", or when a project has no scripted way to prove UI behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[e2e](https://clawhub.ai/user/e2e)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to create a project-specific verification recipe that helps coding agents launch an app, exercise its user-facing features, preserve evidence, and bug bash the result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verification exercises real app actions, and screenshots, traces, or model inputs may contain sensitive app data.

Mitigation: Use a test instance and dedicated test accounts, and keep saved evidence and model inputs within the app's privacy requirements.

Risk: Setup may install dependencies or change MCP configuration, while the external e2e implementation has not been verified.

Mitigation: Review and pin downloaded dependencies, inspect the sibling e2e skill before setup, and review MCP configuration changes.

## Reference(s):

- [e2e](https://e2e.com)

## Skill Output:

**Output Type(s):** [Files, Markdown, Configuration instructions, Code, Shell commands]

**Output Format:** [Project-local Markdown files, configuration, test code, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a verification skill and feature map with exploratory charters, then runs one proof when the project supports it.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
