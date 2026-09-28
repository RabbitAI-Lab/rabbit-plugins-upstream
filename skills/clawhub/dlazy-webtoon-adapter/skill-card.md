## Description:

Guides Chinese-language web-novel adaptation into plot breakdowns and episodic webtoon scripts, with optional dLazy image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and writers use this skill to turn web-novel chapters into plot outlines, episode plans, and Chinese-language webtoon scripts; they can optionally generate accompanying images through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install and run a third-party CLI to generate images.

Mitigation: Review the CLI and its requested actions before installation or execution; approve each generation step.

Risk: Signing in can store an API key in local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable when persistent storage is not wanted; rotate or revoke exposed keys.

Risk: Image prompts and referenced media may be sent to dLazy, and generated images may be available through hosted URLs.

Mitigation: Do not submit sensitive prompts or files without authorization; check generated URLs before sharing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Chinese-language structured outlines and scripts, with optional generation commands and hosted image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow asks for confirmation before generating each image.]

## Skill Version(s):

1.3.22 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
