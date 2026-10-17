## Description:

Turns one clear portrait and a short singing-audio excerpt into a singing-photo video, then guides review of the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and other external users can make a short singing clip from an approved portrait and singing-audio excerpt, then review the returned video for identity, motion, sound, and synchronization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra device token grants broad generation and spending-related access.

Mitigation: Review account permissions before connecting and revoke access in the Beatra Console when no longer needed.

Risk: Portrait and audio inputs are uploaded to Beatra for generation.

Mitigation: Use only media that the user is authorized to share with Beatra.

Risk: Automatic package updates install without separate confirmation by default.

Mitigation: Disable silent updates with the documented update --auto off option if review before installation is required.

Risk: Paid calls rely on the agent following written confirmation steps rather than an enforced local approval gate.

Mitigation: Confirm the exact estimated cost and request explicit user approval before each paid generation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/photo-singing-video)
- [Beatra photo-singing skill](https://beatra.ai/skills/photo-singing-video)
- [Singing-photo workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Markdown, Video artifact links, Guidance]

**Output Format:** [Markdown with returned video links and task details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation may incur charges; identity and lip synchronization should be reviewed.]

## Skill Version(s):

0.1.9 (source: ClawHub release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
