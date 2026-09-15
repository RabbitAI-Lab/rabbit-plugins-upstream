## Description:

KIE.AI helps an agent inspect schemas and run available KIE.AI connector actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to check KIE.AI account credits and convert generated file URLs into temporary direct download URLs through their connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Install the oo CLI only from a trusted, inspectable source and verify the installer source, version, and integrity before running it.

## Reference(s):

- [KIE.AI homepage](https://kie.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kie-ai)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action runs return JSON responses with data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata, skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
