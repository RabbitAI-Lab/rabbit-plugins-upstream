## Description:

Connect a Fellow Aiden through its cloud account and turn a coffee bag photo or roaster recipe into a named hot-coffee brew profile.

This skill is ready for commercial/non-commercial use.

## Publisher:

[patrick-erichsen-2](https://clawhub.ai/user/patrick-erichsen-2)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use the agent to turn a coffee-bag photo or roaster recipe into a named Fellow Aiden hot-coffee profile, reviewing the proposed settings before creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires Fellow account credentials.

Mitigation: Supply credentials through a secret manager and keep them out of chats, command arguments, files, and logs.

Risk: The undocumented Fellow cloud API may change, affecting profile operations.

Mitigation: Verify current behavior before changing profiles, review proposed settings, and use dry-run validation before account changes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/patrick-erichsen-2/skills/fellow-aiden)
- [Fellow Aiden connection statuses](https://help.fellowproducts.com/hc/en-us/articles/31125190846747-What-are-Aiden-s-connection-statuses-and-what-do-they-mean)
- [Fellow Aiden pre-installed brew profiles](https://help.fellowproducts.com/hc/en-us/articles/29539043135515-What-are-the-pre-installed-brew-profiles-Aiden-offers)
- [Fellow Drops profile help](https://help.fellowproducts.com/hc/en-us/articles/31277829842459-How-do-I-hide-Drops-brew-profiles)
- [Community Fellow Aiden Home Assistant integration](https://github.com/kristofferR/FellowAiden-HomeAssistant)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON brew-profile proposals and concise text or Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profile proposals can be validated without connecting; account changes require user authorization and may be verified by listing profiles.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
