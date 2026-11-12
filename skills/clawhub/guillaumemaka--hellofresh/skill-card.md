## Description:

Manage a HelloFresh subscription by browsing recipes, changing meal selections, viewing delivery history, tracking shipments, converting recipe instructions to speech, and checking notification settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guillaumemaka](https://clawhub.ai/user/guillaumemaka)

### License/Terms of Use:

MIT-0

## Use Case:

External users with HelloFresh accounts use this skill to inspect subscription status, browse current or upcoming recipes, review delivery history, receive recipe and shipment reminders, and play cooking instructions through text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles authenticated HelloFresh browser sessions and stores subscription details in a local session file.

Mitigation: Use local browser mode where possible, avoid shared machines, and treat the session file as sensitive account data.

Risk: Optional Kernel.sh mode sends authenticated browsing activity through a cloud browser provider.

Mitigation: Enable Kernel.sh only when cloud browsing is acceptable for the account data being accessed.

Risk: Documentation includes real-looking tracking, phone, and subscription examples.

Mitigation: Remove or replace those examples before publication or distribution.

Risk: Dependencies are declared without a lockfile in the artifact.

Mitigation: Pin dependencies and add a lockfile before relying on this package.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guillaumemaka/skills/hellofresh)
- [Publisher profile](https://clawhub.ai/user/guillaumemaka)
- [Kernel dashboard](https://dashboard.onkernel.com)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown command responses with status summaries, recipe lists, notification settings, tracking updates, and optional text-to-speech playback for recipe instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses browser automation against a user's authenticated HelloFresh session and stores session and recipe cache files under the user's OpenClaw directory.]

## Skill Version(s):

1.0.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
