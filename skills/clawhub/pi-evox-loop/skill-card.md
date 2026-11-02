## Description:

Adds an experience-inheritance workflow that recalls validated fixes, records useful hits, and helps coding agents save new fixes for later tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use it with coding agents to reuse validated fixes across tasks, record newly useful repairs, and optionally run controlled experiments that measure their effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reused or imported fixes may contain misleading guidance or instructions that have not been adequately screened.

Mitigation: Require manual approval, inspect each imported field, and do not automatically trust remote pools.

Risk: Export bundles and experiment files may contain private task or session information.

Mitigation: Inspect complete export bundles for sensitive information; run experiments in a disposable copy with a separate experience store.

Risk: Host integrations and optional dependencies can affect the agent environment.

Mitigation: Back up host integrations before use and upgrade the optional Pi dependency.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project documentation](https://github.com/stwhwing/pi-evox-lab)
- [Quickstart guide](https://github.com/stwhwing/pi-evox-lab/blob/main/examples/quickstart.md)
- [Security and license guide](https://github.com/stwhwing/pi-evox-lab/blob/main/docs/security-and-license.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Numbered Markdown fix lists, CLI guidance, configuration examples, and experiment reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recall output depends on the available validated fixes; controlled experiment reports are optional.]

## Skill Version(s):

0.35.0 (source: server release metadata, SKILL.md, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
