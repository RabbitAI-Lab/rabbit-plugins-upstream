## Description:

Guides platform-specific social media image design, copywriting, and image generation through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to plan and generate social media visuals, image text, and captions tailored to Instagram, TikTok, YouTube, LinkedIn, and Xiaohongshu.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation parameters, and supplied media may be sent to dLazy cloud services.

Mitigation: Avoid supplying sensitive content unless authorized to share it with dLazy.

Risk: The dLazy CLI may save an API key locally for reuse.

Mitigation: Protect the local configuration and rotate or revoke the key if exposed.

Risk: A global CLI installation persists on the local system.

Mitigation: Use the documented npx option or review the package before a global install.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (referenced by skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Markdown text with design plans, captions, optional CLI commands, and generated image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Platform specifications, safe-area checks, and revision suggestions]

## Skill Version(s):

1.3.26 (source: server-resolved ClawHub release; skill frontmatter lists 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
