## Description:

The example skill shipped with skill-mcp shows the SKILL.md shape, a bundled reference file, and a declared runnable script.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to check that skill-mcp is wired up and to understand the shape of an mcp-host declaration, including how a declared runnable script is exposed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The demo script prints the names of environment variables made visible to it.

Mitigation: Run it through the intended skill-mcp host with confirmation enabled, and avoid running it as a general local Node script in a shell containing sensitive ambient environment names.

Risk: A declared script is still arbitrary local code bounded by the host environment and registration controls.

Mitigation: Review declared scripts before deployment and rely on the host confirmation flow before execution.

## Reference(s):

- [mcp-host declaration block](references/declaration.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Markdown guidance and JSON script output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The declared script prints argv, cwd, visible environment variable names, and Node.js version; it does not print environment values.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
