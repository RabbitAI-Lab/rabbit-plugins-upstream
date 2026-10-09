## Description:

Creates a short spoken recommendation video from a topic, including a shot list, still frames, narration, and an animated vertical clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to draft and generate short recommendation videos for social platforms without supplying footage or a recorded voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra device token can be reused by other Beatra skills and can authorize credit-spending requests.

Mitigation: Keep the token private, review access before installation, and use the Beatra Console to revoke it when needed.

Risk: Media-generation calls can spend credits.

Mitigation: Review the request details and live estimates before approving paid calls.

Risk: The installed package silently checks for and installs updates by default.

Mitigation: Disable automatic updates with the documented `update --auto off` command if unreviewed changes are unacceptable.

## Reference(s):

- [ClawHub release](https://clawhub.ai/beatra-ai/skills/oral-seeding-video-maker)
- [Seeding video workflow](artifact/references/workflow.md)
- [Writing spoken lines](artifact/references/spoken-lines.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Media artifact links]

**Output Format:** [Markdown shot list and delivery summary with links to generated stills, narration, and a vertical video clip]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional music bed; reports task IDs and charged credits when returned.]

## Skill Version(s):

0.2.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
