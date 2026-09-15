## Description:

Recurly (recurly.com) skill for reading, creating, and updating Recurly data through OOMOL instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Recurly accounts, plans, and subscriptions through an OOMOL-connected account. It supports schema-first read actions and controlled write workflows for billing-related Recurly data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts directly.

Mitigation: Download and verify the OOMOL installer through a trusted, versioned method before installation.

Risk: Write actions can change Recurly billing, account, plan, or subscription data.

Mitigation: Fetch the live action schema and confirm the exact payload and expected effect with the user before running any write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-recurly)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Recurly homepage](https://recurly.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
