## Description:

Generate and sell exclusive instrumental beats on BeatClaw using Suno API keys with optional stem splitting for WAV and stems sales.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youngpietro](https://clawhub.ai/user/youngpietro)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, producers, and agent operators use this skill to configure a BeatClaw producer, generate instrumental beats with a Suno API key, manage pricing and exclusivity, optionally split stems, and publish beats for sale.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to overwrite its installed SKILL.md from a mutable remote URL.

Mitigation: Prefer the ClawHub install path or a pinned, checksummed copy, and manually review any downloaded update before allowing the agent to overwrite local instructions.

Risk: The skill sends API keys and beat-management requests to BeatClaw and third-party services as part of normal operation.

Mitigation: Only provide credentials through the intended setup flow, rotate exposed tokens, and confirm spending actions before generation or stem processing.

Risk: Payout information handling is inconsistent across the artifact and security evidence.

Mitigation: Do not provide PayPal email in chat; use the BeatClaw dashboard PayPal connection flow for payout setup.

## Reference(s):

- [Beatclaw on ClawHub](https://clawhub.ai/youngpietro/skills/beatclaw)
- [Publisher profile](https://clawhub.ai/user/youngpietro)
- [BeatClaw](https://beatclaw.com)
- [Suno API provider](https://sunoapi.org)
- [MVSEP user API](https://mvsep.com/user-api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown instructions with JSON request examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include BeatClaw endpoint requests, version header requirements, setup steps, and human confirmation checkpoints.]

## Skill Version(s):

1.57.0 (source: server release metadata and artifact SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
