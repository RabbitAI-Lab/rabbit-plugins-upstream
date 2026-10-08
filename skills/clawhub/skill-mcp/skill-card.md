## Description:

Provides a sample skill declaration, reference guide, and runnable script for exploring skill-mcp.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers can inspect an example skill declaration and run its diagnostic script to see which arguments and environment-variable names reach the script.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the demo script exposes the names of environment variables visible to it in the tool result.

Mitigation: Run through the intended skill_run path with confirmation and a scoped environment; avoid direct execution in a sensitive shell.

## Reference(s):

- [skill-mcp on ClawHub](https://clawhub.ai/chrischall/skills/skill-mcp)
- [Declaration block reference](artifact/references/declaration.md)

## Skill Output:

**Output Type(s):** [Guidance, JSON]

**Output Format:** [Markdown guidance and optional JSON runtime diagnostics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Diagnostics include arguments, working directory, Node.js version, and environment-variable names, not their values.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
