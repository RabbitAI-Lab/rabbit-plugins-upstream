## Description:

The skill-mcp example skill shows the SKILL.md shape, a bundled reference file, and a declared runnable script.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to check that skill-mcp is wired up and to understand how a skill declares an mcp-host runnable script and related reference material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled demo script prints the names of environment variables visible to its host, which can reveal runtime details even without exposing values.

Mitigation: Run or install it only where reporting environment variable names is acceptable, and avoid granting unnecessary environment access.

Risk: The declared local Node.js script is still executable code, even though the scan found no hidden network, persistence, or destructive behavior.

Mitigation: Review the declared script and host permissions before deployment, and keep execution bounded by the host environment.

## Reference(s):

- [mcp-host declaration block](references/declaration.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/skill-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline command examples; the bundled report script returns JSON text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The demo script reports argv, cwd, Node.js version, and environment variable names, not values.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
