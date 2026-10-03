## Description:

Turns public YouTube insurance captions and advisor-written clause lines into separate short talking clips using supplied stills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Insurance and wealth advisors use this skill to plan and produce individual talking clips from public YouTube insurance captions, their own approved clause wording, and supplied still images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared, persistent Beatra authorization can reach beyond this caption workflow and approved operations may spend credits.

Mitigation: Review the authorization scope and live prices before granting access or approving paid operations.

Risk: The bundled client installs updates silently by default.

Mitigation: Disable automatic updates using the documented update command if manual review is required.

Risk: Local Beatra credentials provide sensitive account access.

Mitigation: Protect ~/.beatra/credentials.json and do not share its contents.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/youtube-insure-caption-talking)
- [Insurance caption talking workflow](artifact/references/workflow.md)
- [Insurance caption lookup](artifact/references/caption-lookup.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Markdown, Video files, Audio files]

**Output Format:** [Labeled caption-to-clip plan and separate short video files, with speech audio when generated]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Clips remain separate; reports available file details and charges for completed paid tasks.]

## Skill Version(s):

0.1.7 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
