## Description:

Helps agents generate instrumental beats with a third-party Suno API key and publish them for sale on BeatClaw, with optional stem splitting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youngpietro](https://clawhub.ai/user/youngpietro)

### License/Terms of Use:

MIT-0

## Use Case:

Music producers and their agents use BeatClaw to create, manage, and sell instrumental beats, optionally offering stems or exclusive licenses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs agents to overwrite installed instructions from a remote URL during updates.

Mitigation: Review the replacement instructions before installing; prefer ClawHub or a pinned, reviewed copy.

Risk: The setup asks the agent to handle third-party music and stem-splitting API keys.

Mitigation: Do not paste keys into ordinary chat; enter them through a dedicated settings page or secure secret store.

Risk: Beat generation and stem splitting consume provider credits, while pricing, exclusivity, and deletion affect marketplace listings.

Mitigation: Confirm each credit-spending operation, price or exclusivity change, and deletion with the owner before proceeding.

Risk: Connecting a payout account affects where sales proceeds are received.

Mitigation: Connect PayPal only through BeatClaw's browser dashboard.

## Reference(s):

- [BeatClaw on ClawHub](https://clawhub.ai/youngpietro/skills/beatclaw)
- [BeatClaw skill instructions](https://beatclaw.com/skill)
- [MVSEP API access](https://mvsep.com/user-api)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Configuration instructions]

**Output Format:** [Text and Markdown with API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated audio is published on BeatClaw; stem file URLs are not returned to the agent.]

## Skill Version(s):

1.58.0 (source: ClawHub release metadata and skill instructions)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
