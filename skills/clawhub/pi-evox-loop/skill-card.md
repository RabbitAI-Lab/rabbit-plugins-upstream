## Description:

Adds an experience-inheritance workflow for coding agents to recall reviewed fixes, record when they help, and save new fixes after non-obvious failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to carry reviewed fixes between coding-agent tasks, capture useful fixes after failures, and optionally measure their effect with controlled experiments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored or recalled fixes may contain unreviewed guidance that affects later tasks.

Mitigation: Review recalled fixes before applying them, keep host security rules in force, and approve only fixes you have checked.

Risk: Workspace cleanup and automatic approval behavior may have effects beyond the immediate task.

Mitigation: Inspect the proposed cleanup targets and approval settings before running setup, reset, or deposit commands.

Risk: Sharing features can expose selected fixes, and scanner coverage is partial.

Mitigation: Keep sharing disabled unless needed, review and sanitize fixes before sharing, and assess optional dependencies before enabling integrations.

## Reference(s):

- [Pi EvoX Loop project repository](https://github.com/stwhwing/pi-evox-lab)
- [Pi coding agent](https://github.com/earendil-works/pi)
- [Evolver](https://github.com/EvoMap/evolver)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance, shell commands, code examples, and optional experiment reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.39.0 (source: SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
