## Description:

Beatclaw helps agents generate instrumental beats through BeatClaw, publish them for sale, manage pricing and exclusivity, and optionally process stems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youngpietro](https://clawhub.ai/user/youngpietro)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and agent users use Beatclaw to set up a BeatClaw seller account, generate instrumental beats with a third-party Suno API key, publish beats for marketplace sale, and manage pricing, exclusivity, stems, and listing updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can self-update from a mutable beatclaw.com URL.

Mitigation: Inspect the downloaded SKILL.md before installing or replacing the local skill, and restart the agent session only after review.

Risk: The skill handles third-party Suno and MVSEP API keys and payment-related setup.

Mitigation: Use low-privilege or revocable provider keys, understand where keys are stored, and monitor provider spending and key activity.

Risk: The skill can affect marketplace listings, including deletion, exclusivity, and pricing.

Mitigation: Require explicit human confirmation before spending credits or changing commercial listing terms.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youngpietro/skills/beatclaw)
- [Publisher Profile](https://clawhub.ai/user/youngpietro)
- [BeatClaw Skill Installer](https://beatclaw.com/skill)
- [BeatClaw Marketplace](https://beatclaw.com)
- [Suno API Provider](https://sunoapi.org)
- [MVSEP User API](https://mvsep.com/user-api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, API calls, configuration, markdown]

**Output Format:** [Markdown guidance with JSON request bodies and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can guide setup, request human confirmation before spending credits, and produce API calls for beat generation, listing management, token rotation, and stem processing.]

## Skill Version(s):

1.50.0 (source: server release evidence and artifact SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
