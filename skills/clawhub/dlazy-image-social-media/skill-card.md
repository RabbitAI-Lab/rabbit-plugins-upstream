## Description:

Plans platform-adapted social media visuals, layouts, and caption copy for Instagram, TikTok, YouTube, LinkedIn, Xiaohongshu, and other platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Social media creators and marketers can use the skill to plan platform-specific visuals, image text, captions, and adaptations, with optional image generation through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy's hosted API and media storage during generation.

Mitigation: Use only prompts and media you intend to share with dLazy.

Risk: The dLazy API key is stored in the local CLI configuration unless provided through an environment variable.

Mitigation: Protect the local configuration file and rotate or revoke the key through the dLazy dashboard if needed.

Risk: The documentation includes a stale CLI version statement alongside commands pinned to version 1.2.3.

Mitigation: Check the package version before use and follow the 1.2.3 installation command identified in the security guidance.

## Reference(s):

- [Clawhub release page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)
- [dLazy website](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI project link listed in skill metadata (provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Image-generation prompts, Shell commands]

**Output Format:** [Markdown with platform-specific design plans, image text, captions, and CLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes platform format, safe-area, and visual guidance; generated image results may be returned as URLs.]

## Skill Version(s):

1.3.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
