## Description:

A structured skill for creating multi-platform social media visuals and captions for Instagram, TikTok, YouTube, LinkedIn, Xiaohongshu, and related formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent users use this skill to plan, generate, and iterate social media images, thumbnails, carousel structures, in-image text, and platform-specific captions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected media files may be sent to dLazy-hosted services during generation.

Mitigation: Avoid providing sensitive local media or confidential prompts unless upload to dLazy services is intended.

Risk: Using a persistent global CLI install or saved API key can leave local credentials and tooling in place after use.

Mitigation: Prefer npx or the DLAZY_API_KEY environment variable for temporary use, and rotate or revoke API keys from the dLazy dashboard when needed.

Risk: Generated social media assets can be off-brand, platform-inaccurate, or include unsuitable caption or in-image text.

Mitigation: Review generated layouts, safe-area checks, image text, and captions before publication.

## Reference(s):

- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with planning notes, safe-area checks, copy layers, captions, inline shell commands, and generated asset URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the dLazy CLI to submit prompts, parameters, and selected media files to dLazy-hosted services when generation is confirmed.]

## Skill Version(s):

1.3.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
