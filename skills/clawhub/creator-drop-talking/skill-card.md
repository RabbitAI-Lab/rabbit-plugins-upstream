## Description:

Turns confirmed product-drop details and authorized stills into short, separate talking announcement clips, one per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and listing teams use this skill to plan and produce short talking teasers for a product launch from confirmed facts and authorized photos. It provides a slot list before any paid voice, speech, or video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra device token can authorize paid operations beyond this workflow.

Mitigation: Grant access only if comfortable with that account authority; protect the token and review paid stages before approval.

Risk: Voice, speech, and video generation can spend Beatra credits.

Mitigation: Check live model and price details, approve each paid stage separately, and monitor actual credit usage.

Risk: The bundled client silently installs verified updates by default.

Mitigation: Disable automatic updates when stable, reviewable code is required, and review updates before enabling them.

## Reference(s):

- [Creator Drop Talking Clips on ClawHub](https://clawhub.ai/beatra-ai/skills/creator-drop-talking)
- [Creator Drop Talking Clips homepage](https://beatra.ai/skills/creator-drop-talking)
- [Drop talking-clip workflow](references/workflow.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Installation and authentication](references/installation-and-auth.md)

## Skill Output:

**Output Type(s):** [Text, Audio clips, Video clips]

**Output Format:** [Markdown slot list and separate generated media artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One 2–15-second talking clip per approved still or audio segment; no stitched video. Generated media and actual credit charges are reported when available.]

## Skill Version(s):

0.1.8 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
