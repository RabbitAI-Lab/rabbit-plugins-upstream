## Description:

Helps music producers generate instrumental beats with Suno, manage BeatClaw listings, and optionally prepare stems for sale.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youngpietro](https://clawhub.ai/user/youngpietro)

### License/Terms of Use:

MIT-0

## Use Case:

Music producers use this skill to direct an agent to create instrumental beats, publish and manage marketplace listings, and arrange optional stem splitting for buyers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation can spend the owner's Suno credits.

Mitigation: Confirm each generation with the owner before spending; after reconnecting, stop and seek fresh approval for each pending action.

Risk: Publishing, changing, or deleting listings affects the public marketplace.

Mitigation: Review listing details and obtain the owner's approval before publication or consequential changes.

Risk: Long-lived BeatClaw and provider credentials can expose account access.

Mitigation: Avoid sharing tokens in chat, store credentials securely, set up PayPal through the owner dashboard, and revoke or rotate credentials when access is no longer needed.

Risk: A remote skill update can replace local instructions.

Mitigation: Prefer the ClawHub installation path or verify downloaded skill content before use; review updates and restart the agent session before resuming.

## Reference(s):

- [BeatClaw ClawHub listing](https://clawhub.ai/youngpietro/skills/beatclaw)
- [BeatClaw marketplace](https://beatclaw.com)
- [Suno API provider](https://sunoapi.org)
- [MVSEP API key setup](https://mvsep.com/user-api)

## Skill Output:

**Output Type(s):** [Text, Guidance, API calls, Configuration instructions]

**Output Format:** [Markdown with API requests and marketplace links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns generation status and listing links; audio and stems are delivered through the marketplace.]

## Skill Version(s):

1.59.0 (source: server-resolved release metadata and SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
