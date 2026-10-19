## Description:

Creates dated, single-voice store PA announcements for opening, promotions, flash offers, and closing during a campaign window.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Retail teams use this skill to prepare and generate four dated, consistently voiced in-store announcements for a promotion, with optional consent-based voice cloning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled client has broader Beatra account authority than the announcement workflow needs.

Mitigation: Grant account access only if comfortable with that scope; avoid generic tool calls outside the PA workflow.

Risk: A shared device token is stored locally under ~/.beatra.

Mitigation: Keep the token private and use the documented disconnect procedure when access is no longer needed.

Risk: Package updates install silently by default and can change future behavior.

Mitigation: Consider disabling automatic updates using the documented update command and review new releases before updating.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/store-pa-broadcast-pack)
- [Publisher's skill page](https://beatra.ai/skills/store-pa-broadcast-pack)
- [Store PA broadcast workflow](artifact/references/workflow.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Audio files, Guidance]

**Output Format:** [Dated MP3 clips with a labeled text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Four campaign slots (open, promo, flash, close); reports clip duration and charges.]

## Skill Version(s):

0.1.7 (source: ClawHub release and package manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
