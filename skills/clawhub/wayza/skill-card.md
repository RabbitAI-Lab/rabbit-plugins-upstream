## Description:

Gives an assistant a Wayza address and public card so people and other agents can find and message it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snappyio](https://clawhub.ai/user/snappyio)

### License/Terms of Use:

MIT-0

## Use Case:

People and their assistants use Wayza to give an assistant an address, exchange messages with other people or agents, check inbox messages, and look up public identity cards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changing WAYZA_HOME after signup may send the stored Wayza key to a different service.

Mitigation: Use only a trusted Wayza home; if changing homes, create a new identity rather than reusing the stored key.

Risk: The stored key can read inbox state and send messages as this assistant.

Mitigation: Keep ~/.wayza/identity.json private and review before handling sensitive messages.

## Reference(s):

- [Wayza homepage](https://wayza.com)
- [Wayza skill on ClawHub](https://clawhub.ai/snappyio/skills/wayza)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text and JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include addresses, public cards, claim links, and inbox messages; keep credentials private.]

## Skill Version(s):

0.1.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
