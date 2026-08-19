## Description:

ablefy (ablefy.io) lets an agent search and read account, product, and pricing-plan data through the OOMOL oo CLI connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve ablefy account details, products, and pricing plans from an OOMOL-connected ablefy account. It is intended for read-focused connector workflows that inspect the live action schema before running oo CLI commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The trigger wording is broad and may route any ablefy-related request through this connector.

Mitigation: Install only when the intended agent should read ablefy account, product, and pricing-plan information through an OOMOL-connected account.

Risk: First-time use may require CLI installation, authentication, or ablefy connection setup.

Mitigation: Follow setup steps only after an oo CLI command fails with the matching installation, authentication, connection, or billing error.

## Reference(s):

- [ClawHub ablefy skill page](https://clawhub.ai/oomol/skills/oo-ablefy)
- [ablefy homepage](https://ablefy.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
