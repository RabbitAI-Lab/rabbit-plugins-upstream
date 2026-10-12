## Description:

Helps agents generate instrumental beats and manage their sale on the BeatClaw marketplace, with optional stem splitting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youngpietro](https://clawhub.ai/user/youngpietro)

### License/Terms of Use:

MIT-0

## Use Case:

External producers use the skill to connect an agent to their BeatClaw account, generate instrumental beats, manage marketplace listings, and optionally split stems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs agents to overwrite persistent instructions from a live URL without an integrity check or prior review.

Mitigation: Prefer a versioned ClawHub installation, or inspect the downloaded SKILL.md before enabling or updating it; only trust updates from beatclaw.com if you trust its operator.

Risk: A connected agent can change marketplace listings and initiate generation that spends the producer's credits.

Mitigation: Protect connection tokens and require the producer's explicit approval before spending credits or changing public listings.

## Reference(s):

- [BeatClaw ClawHub release](https://clawhub.ai/youngpietro/skills/beatclaw)
- [BeatClaw marketplace and producer dashboard](https://beatclaw.com)
- [Suno API provider](https://sunoapi.org)
- [MVSEP stem-splitting API](https://mvsep.com/user-api)

## Skill Output:

**Output Type(s):** [Text, Guidance, API calls]

**Output Format:** [Conversational text with beat details, marketplace links, and optional API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates marketplace-hosted audio and optional stems; agents report results rather than distributing audio files.]

## Skill Version(s):

1.61.0 (source: server-resolved release metadata and skill document)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
