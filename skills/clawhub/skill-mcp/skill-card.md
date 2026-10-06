## Description:

An example skill shipped with skill-mcp that demonstrates a SKILL.md file, a bundled reference, and a declared runnable script.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this example to inspect how an MCP-hosted skill declares a runnable script and to see the arguments, working directory, and environment variable names exposed during a test run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The diagnostic report exposes names of environment variables available to the script, which may reveal sensitive context.

Mitigation: Run only within the intended mcp-host fence and avoid using it in a shell with sensitive or revealing environment variable names.

Risk: A declared runnable script can execute arbitrary code if the host does not constrain it.

Mitigation: Review the declared script and use the host's approval and execution boundaries before running it.

## Reference(s):

- [MCP-host declaration reference](references/declaration.md)
- [Skill MCP ClawHub release](https://clawhub.ai/chrischall/skills/skill-mcp)

## Skill Output:

**Output Type(s):** [JSON diagnostic report, Guidance]

**Output Format:** [JSON from the diagnostic script; Markdown guidance in the skill documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The diagnostic report lists environment variable names, not their values.]

## Skill Version(s):

1.1.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
