## Description:

The example skill shipped with skill-mcp shows the SKILL.md shape, a bundled reference file, and a declared runnable script.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect the structure of a ClawHub skill with an mcp-host declaration and a declared Node.js script.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the demo script may reveal environment variable names visible to the script.

Mitigation: Run it under the intended mcp-host fence or another sanitized environment when variable names could reveal sensitive infrastructure details.

## Reference(s):

- [mcp-host declaration block](references/declaration.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with YAML and command examples; the declared script emits JSON when run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The declared report script prints argument, working directory, Node.js version, and environment variable names visible to it.]

## Skill Version(s):

0.2.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
