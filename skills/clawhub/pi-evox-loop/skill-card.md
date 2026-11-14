## Description:

Adds an experience-inheritance workflow that recalls validated fixes, records when they help, and guides agents to save new fixes for later tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the skill with coding agents to recall relevant, reviewed fixes at the start of a task and record useful fixes after resolving non-obvious failures. It also supports optional controlled experiments for measuring whether experience reuse helps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security scan is suspicious and only partially inspected the package.

Mitigation: Review the release security guidance and package contents, and defer installation until the reported concerns are resolved.

Risk: Automatic approval could allow newly generated fixes to be reused without a human review step.

Mitigation: Leave automatic approval disabled and inspect fixes before approving them for future recall.

Risk: Optional dependency, provider, or sharing settings may expose task or repository information or add dependency risk.

Mitigation: Review provider and optional integration settings before enabling them, share only intentionally, and keep sensitive task or repository data out of shared or external workflows.

## Reference(s):

- [ClawHub release](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project homepage](https://github.com/stwhwing/pi-evox-lab)
- [Security and license guidance](https://github.com/stwhwing/pi-evox-lab/blob/main/docs/security-and-license.md)
- [Quickstart](https://github.com/stwhwing/pi-evox-lab/blob/main/examples/quickstart.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell commands, code examples, and structured fix records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task-dependent; may create or update local experience records when the user chooses to save a fix.]

## Skill Version(s):

0.41.0 (source: server release metadata, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
