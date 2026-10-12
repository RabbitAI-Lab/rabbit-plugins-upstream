## Description:

An example skill shipped with skill-mcp that shows a skill declaration, a bundled reference, and a runnable reporting script.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers can inspect the example skill and its declaration reference to learn how to declare a runnable script and test its execution context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reported environment variable names may disclose local setup details in tool output.

Mitigation: Review the report before sharing it and avoid exposing environment details to unintended recipients.

Risk: Running a declared script executes code under the host's permissions.

Mitigation: Inspect the script and its requested permissions before approving execution.

## Reference(s):

- [ClawHub skill-mcp release](https://clawhub.ai/chrischall/skills/skill-mcp)
- [MCP host declaration reference](references/declaration.md)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Text]

**Output Format:** [Markdown guidance and a JSON execution-context report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report includes arguments, working directory, environment variable names, and Node.js version; it does not print variable values.]

## Skill Version(s):

1.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
