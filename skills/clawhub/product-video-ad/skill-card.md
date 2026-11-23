## Description:

Turns product selling points into a short advertising video through storyboarding, shot generation, stitching, and captions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants and marketing creators use this skill to turn product selling points into short advertising videos with generated shots, captions, and a stitched final clip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images may be sent to external video-generation providers, and the available security review leaves this data flow unresolved.

Mitigation: Before use, check which provider receives prompts and images, share only materials approved for that provider, and review behavior in files that were not fully analyzed.

## Reference(s):

- [Product Video Ad on ClawHub](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Provider CLI reference](references/provider-cli.md)
- [Video backend reference](references/video-backends.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Shell commands, Video files]

**Output Format:** [Storyboard JSON, prompts, shell commands, SRT subtitles, and MP4 video clips or finished video.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates separate shots and may stitch them into a captioned final video; narration and music are not produced.]

## Skill Version(s):

1.0.32 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
