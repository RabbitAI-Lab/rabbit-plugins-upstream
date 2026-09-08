## Description:

The example skill shipped with skill-mcp - shows the SKILL.md shape, a bundled reference file, and a declared runnable script.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this demonstration skill to check that skill-mcp is wired up, inspect the mcp-host declaration shape, and run a local diagnostic script showing the execution fence's arguments, working directory, and environment variable names.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The diagnostic script output can reveal host details such as argument values, working directory, environment variable names, and runtime version.

Mitigation: Run the skill only when that diagnostic output is needed, and keep the script environment limited to the documented fixed host set and explicitly granted variables.

Risk: The mcp-host declaration narrows what may run, but it does not make a declared script inherently safe.

Mitigation: Review the declared script before enabling it, and rely on host registration, read-only skill files, and bounded write locations such as MCP_DATA_DIR or TMPDIR.

## Reference(s):

- [mcp-host declaration block reference](references/declaration.md)
- [skill-mcp ClawHub page](https://clawhub.ai/chrischall/skills/skill-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with inline shell command examples and JSON diagnostic output from the declared script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The diagnostic script reports argument values, working directory, environment variable names, and Node.js version; it avoids printing environment variable values.]

## Skill Version(s):

0.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
