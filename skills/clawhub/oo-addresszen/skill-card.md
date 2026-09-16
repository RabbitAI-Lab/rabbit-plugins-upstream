## Description:

AddressZen lets an agent search and retrieve AddressZen address data through an OOMOL-connected oo CLI account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect AddressZen connector schemas, autocomplete partial addresses, check key availability, and retrieve USA-formatted address records through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer one-liners that run shell code from a URL.

Mitigation: Do not let an agent run installer one-liners automatically; install the oo CLI only from a trusted, verified source and have the user confirm authentication and connection setup.

## Reference(s):

- [ClawHub AddressZen skill page](https://clawhub.ai/oomol/skills/oo-addresszen)
- [AddressZen homepage](https://addresszen.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented AddressZen connector actions; live action schemas should be inspected before payload construction.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
