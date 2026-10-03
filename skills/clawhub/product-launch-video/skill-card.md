## Description:

Turns a product URL, script, or brief into a branded product-launch or promotional video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and creators use this skill to turn a product website, script, or brief into a branded launch video, including site showcases and feature reveals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned HyperFrames commands can run changing remote tooling and update globally installed skills.

Mitigation: Confirm updates with the user and consider pinning and sandboxing the CLI before use.

Risk: Capturing marketing URLs can collect content that should not be shared with external services.

Mitigation: Capture only authorized URLs and review the brief and captured assets before continuing.

Risk: Media generation may use configured HeyGen or other provider credentials.

Mitigation: Use trusted providers and scoped credentials, and review resumed project state before running commands.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/heygen-com/skills/product-launch-video)
- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Motion language](references/motion-language.md)
- [Cut catalog](references/cut-catalog.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Video files]

**Output Format:** [Project brief, storyboard and script in Markdown; HTML frame compositions and rendered MP4 video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include audio assets, captions, and a review contact sheet.]

## Skill Version(s):

1.0.46 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
