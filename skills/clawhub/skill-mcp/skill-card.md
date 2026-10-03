## Description:

A diagnostic example skill that shows how to declare a runnable script and inspect the runtime context it receives.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this example to check that skill-mcp can run a declared script and to learn how to write an mcp-host declaration. The diagnostic script reports its arguments, working directory, environment variable names, and Node.js version.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The diagnostic output reveals names of environment variables passed to the script.

Mitigation: Avoid running it in a host configuration that passes broad or sensitive environment metadata.

## Reference(s):

- [mcp-host declaration reference](references/declaration.md)
- [skill-mcp on ClawHub](https://clawhub.ai/chrischall/skills/skill-mcp)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [JSON diagnostic report and Markdown instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report lists environment variable names, not their values; diagnostic logs go to stderr.]

## Skill Version(s):

1.1.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
