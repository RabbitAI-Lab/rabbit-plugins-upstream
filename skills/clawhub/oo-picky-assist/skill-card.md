## Description:

Helps agents check a Picky Assist account balance and send messages through a connected OOMOL account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using Picky Assist can ask an agent to check their account balance or submit text and public-URL media messages to recipients through their connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The one-time CLI installer executes downloaded code.

Mitigation: Review the oo CLI installer before running it.

Risk: Sending a message can contact unintended recipients or transmit unintended content.

Mitigation: Require clear confirmation of recipients, message content, and expected effect before sending.

## Reference(s):

- [Picky Assist on ClawHub](https://clawhub.ai/oomol/skills/oo-picky-assist)
- [Picky Assist](https://pickyassist.com/)
- [oo CLI documentation](https://cli.oomol.com/install-guide.md)
- [oo CLI source](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and action results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Message submission confirms acceptance for processing, not delivery.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
