## Description:

The example skill shipped with skill-mcp shows the SKILL.md shape, a bundled reference file, and a declared runnable script.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this demo skill to check that skill-mcp is wired up and to see how a skill can declare a bundled reference file and a runnable script.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The declared script returns environment variable names visible to it, which may reveal sensitive operational context.

Mitigation: Run the demo in a constrained test environment and grant only environment variables that are acceptable to expose by name.

Risk: The bundled runnable script is still executable code and depends on the host environment for containment.

Mitigation: Review the script before running it and rely on host approval, timeout, and sandbox controls during execution.

## Reference(s):

- [mcp-host declaration block](references/declaration.md)

## Skill Output:

**Output Type(s):** [guidance, code, configuration, shell commands]

**Output Format:** [Markdown guidance with inline code and JSON output from the declared Node script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The script reports argv, working directory, Node version, and environment variable names; it does not print environment variable values.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
