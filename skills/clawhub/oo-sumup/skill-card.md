## Description:

SumUp helps an agent operate a connected SumUp account through OOMOL's oo CLI for checkout, customer, and payment-instrument workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect SumUp action schemas and run approved checkout and customer operations through an OOMOL-connected SumUp account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask the agent to install the oo CLI with a shell installer when the command is missing.

Mitigation: Verify the oo CLI installation source before running the one-time installer.

Risk: Write actions can create checkouts, create customers, or update customer profiles in SumUp.

Mitigation: Require a clear payload and confirmation of the expected effect before running any write action.

Risk: The deactivate checkout action changes SumUp state and can prevent a pending checkout from being processed.

Mitigation: Confirm the exact target checkout and obtain explicit approval before running destructive actions.

Risk: The skill relies on OOMOL as the broker for the user's SumUp connection.

Mitigation: Install only when the user accepts OOMOL's role in brokering SumUp access.

## Reference(s):

- [ClawHub SumUp Skill](https://clawhub.ai/oomol/skills/oo-sumup)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [SumUp Homepage](https://www.sumup.com)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands target the oo CLI and may include connector schema inspection, connector execution, setup, authentication, and SumUp connection guidance.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
