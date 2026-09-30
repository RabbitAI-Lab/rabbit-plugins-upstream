## Description:

Creates four dated, single-voice store PA announcement reads for the opening, promotion, flash sale, and closing of a campaign window.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Retail teams use this skill to draft and produce dated opening, promotional, flash-sale, and closing announcements in a consistent store voice for one campaign window.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared device credential grants access to the Beatra account, including paid generation.

Mitigation: Install only if you trust Beatra with this access; confirm costs before paid requests and review or revoke the connection in the Beatra Console when needed.

Risk: Automatic updates can change the installed code without a separate review.

Mitigation: Review the update policy and consider turning off automatic updates after installation with the documented update --auto off command.

Risk: Voice samples and other chosen uploads are sent to Beatra; cloning a person's voice requires authorization.

Mitigation: Upload only material you are authorized to share, and obtain the speaker's explicit consent before requesting voice cloning.

## Reference(s):

- [Store PA Broadcast Pack on ClawHub](https://clawhub.ai/beatra-ai/skills/store-pa-broadcast-pack)
- [Beatra skill homepage](https://beatra.ai/skills/store-pa-broadcast-pack)
- [Store PA broadcast workflow](references/workflow.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Audio clips, Text]

**Output Format:** [MP3 clips with a Markdown delivery summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Four dated, labeled reads with slot IDs, duration, MIME type, clip link or artifact, and reported credit charges.]

## Skill Version(s):

0.1.6 (source: server-resolved release and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
