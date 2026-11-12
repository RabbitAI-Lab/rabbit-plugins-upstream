## Description:

Routes Rotifer users through onboarding, Gene scaffolding, troubleshooting, registry search, fidelity upgrades, and Arena submissions using the Rotifer CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers working with Rotifer use this skill to learn core concepts, scaffold Genes, diagnose scores or compilation failures, search the registry, upgrade fidelity, and follow Arena rankings through the Rotifer CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security review reports that some install and submission commands may run without the promised user approval.

Mitigation: Review each command and its effects, and obtain explicit user approval before running commands that install software, send work to a service, publish, or overwrite files.

Risk: Security scan coverage was partial because some local references could not be resolved.

Mitigation: Review the relevant referenced instructions and commands before relying on them.

## Reference(s):

- [Rotifer Guide release on ClawHub](https://clawhub.ai/xiaoba-dev/skills/rotifer-guide)
- [Rotifer Protocol](https://rotifer.dev)
- [Rotifer documentation](https://rotifer.dev/docs)
- [Rotifer Protocol specification](https://github.com/rotifer-protocol/rotifer-spec)
- [Rotifer Playground repository (manifest link)](https://github.com/rotifer-protocol/rotifer-playground)
- [Rotifer Gene skills](https://clawhub.ai/skill/rotifer-gene)
- [Rotifer Arena skill](https://clawhub.ai/skill/rotifer-arena)
- [Rotifer Agent skill](https://clawhub.ai/skill/rotifer-agent)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include commands that install tools, read or write project files, query Rotifer services, or send work for generation or publication.]

## Skill Version(s):

1.2.12 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
