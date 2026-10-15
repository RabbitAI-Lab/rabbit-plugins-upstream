## Description:

Helps an assistant verify claimed identities through Wayza and exchange messages with people and other AIs using Wayza addresses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snappyio](https://clawhub.ai/user/snappyio)

### License/Terms of Use:

MIT-0

## Use Case:

People and their assistants use Wayza to ask a known contact to confirm a suspicious message, check whether an AI acts for someone, and exchange messages through Wayza addresses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Disclosure of the local Wayza key or a private claim link could compromise the assistant's account or claim process.

Mitigation: Treat the key as a credential and share claim links only privately with the person claiming the assistant.

Risk: A custom Wayza home receives the assistant's key.

Mitigation: Set WAYZA_HOME only to a Wayza home you trust.

Risk: An unanswered identity check or an unconfirmed AI ownership claim may be mistaken for verification.

Mitigation: Treat no answer and any result other than confirmation as unconfirmed; use a contact address already known to the person.

## Reference(s):

- [Wayza](https://wayza.com)
- [Wayza skill on ClawHub](https://clawhub.ai/snappyio/skills/wayza)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [JSON command responses and plain-language guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes address cards, messages, and identity-check results when requested.]

## Skill Version(s):

0.1.5 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
