## Description:

Use this skill for GenderAPI.io lookup requests, including searching and reading gender inference data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run GenderAPI.io lookup actions for likely gender inference from an email address, first name, or username without handling raw API credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes remote installer commands that execute directly in a local shell.

Mitigation: Install the oo CLI from a trusted, versioned source and verify checksums or signatures before executing installer content.

Risk: Gender inference output may be probabilistic or incomplete because the skill queries GenderAPI.io lookup actions.

Mitigation: Treat returned gender inference data as service-provided lookup results and review it before using it in downstream decisions.

## Reference(s):

- [GenderAPI.io homepage](https://www.genderapi.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-genderapi-io)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses include GenderAPI.io data and execution metadata when actions are run through the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
