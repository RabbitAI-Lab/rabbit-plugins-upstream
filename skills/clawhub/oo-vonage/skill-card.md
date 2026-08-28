## Description:

Operate Vonage through an OOMOL-connected account for balance lookup, SMS delivery record retrieval, SMS record listing, and SMS sending.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate a connected Vonage account through the OOMOL connector, including reading account balance and SMS delivery records or sending SMS after payload confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: send_sms is a real Vonage account action that can contact recipients or incur costs.

Mitigation: Confirm the recipient, message body, and expected effect with the user before allowing the action.

Risk: The skill depends on OOMOL-mediated access to the user's Vonage account.

Mitigation: Install and use the skill only when the user trusts OOMOL to mediate account access.

## Reference(s):

- [Vonage homepage](https://www.vonage.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires confirmation before send_sms write actions; OOMOL mediates access to the connected Vonage account.]

## Skill Version(s):

1.0.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
