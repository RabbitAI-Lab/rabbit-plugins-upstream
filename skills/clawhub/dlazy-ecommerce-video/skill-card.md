## Description:

Helps turn product images, documents, or shopping listings into ecommerce ad videos through dLazy's hosted video-generation service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and marketers use this skill to create product advertising videos for storefronts, social commerce, and cross-border campaigns, with multilingual voiceover and an optional virtual host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected attachments are sent to dLazy, including uploads to its file storage.

Mitigation: Only submit prompts and files you are comfortable sharing with dLazy.

Risk: The external npm CLI may persist an API key in local configuration.

Mitigation: Review the CLI before installing, manage the saved key in ~/.dlazy/config.json, or use DLAZY_API_KEY to avoid persistence.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-video)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Streaming text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped conversations support follow-up requests.]

## Skill Version(s):

1.0.27 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
