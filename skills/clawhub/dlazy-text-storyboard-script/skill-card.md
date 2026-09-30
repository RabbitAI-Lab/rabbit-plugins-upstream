## Description:

Turns themes, structured copy, or outlines into shot-by-shot short-video storyboard scripts with scenes, camera directions, and spoken lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and video production teams use this skill to turn supplied copy into a shootable storyboard while preserving the original spoken wording.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests media generation and external CLI use despite presenting itself as a text storyboard generator.

Mitigation: Review the skill before installation; limit it to script generation if media creation is not desired.

Risk: Using the dLazy workflow may store an API key locally, send prompts or media to dLazy, consume account quota, and return hosted image URLs.

Mitigation: Use it only with approval for external media processing and account charges; protect and rotate the API key as needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)
- [dLazy CLI homepage (release metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (release metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown storyboard with video parameters and numbered shots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each shot includes scene, camera movement, filming notes, and original spoken copy; defaults to 9:16 at 720p when unspecified.]

## Skill Version(s):

1.2.19 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
