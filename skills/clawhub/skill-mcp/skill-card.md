## Description:

The example skill shipped with skill-mcp shows the SKILL.md shape, a bundled reference file, and a declared runnable script.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to inspect the structure of a skill-mcp skill and test a declared local script in a scoped host setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The declared script prints environment variable names in tool output, which can expose sensitive deployment details in some environments.

Mitigation: Run it only in a scoped host registration and avoid unrestricted shells when environment variable names should remain private.

Risk: The artifact states that a declared script is still arbitrary code bounded by the host running it.

Mitigation: Review the script before use and run it with least privilege, read-only skill files, and only approved environment variables.

## Reference(s):

- [mcp-host declaration reference](references/declaration.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/skill-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with an optional JSON report from the declared Node script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The script reports argv, working directory, Node version, and environment variable names, not environment variable values.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
