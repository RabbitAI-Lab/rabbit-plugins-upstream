## Description:

The example skill shipped with skill-mcp shows the SKILL.md shape, a bundled reference file, and a declared runnable script.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this example to understand the SKILL.md layout, bundled references, and the mcp-host declaration for a runnable script.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The demo reporting script shows the names of environment variables it receives, which can reveal what services or integrations exist.

Mitigation: Install only when that disclosure is acceptable, and avoid granting unnecessary environment variables to the hosted script.

Risk: A declared runnable script is still arbitrary local code bounded by the host environment.

Mitigation: Review the declared script and run it only under the host's normal sandboxing and permission controls.

## Reference(s):

- [mcp-host declaration block](references/declaration.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/skill-mcp)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline command examples; the declared Node script emits JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The reporting script prints arguments, working directory, Node version, and environment variable names, not environment values.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
