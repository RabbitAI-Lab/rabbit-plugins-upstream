## Description:

Plans platform-specific social media visuals and captions and supports image generation through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to plan and generate social media graphics, platform-specific layouts, in-image headlines, and accompanying captions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party CLI uses a dLazy API key.

Mitigation: Review the CLI before use, protect the key, and rotate or revoke it if needed.

Risk: Prompts and explicitly supplied media files are sent to dLazy's hosted service.

Mitigation: Only supply prompts and media approved for upload to that service.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Image URLs]

**Output Format:** [Markdown with design plans, captions, and generated image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes platform specifications, safe-area checks, and suggested revisions.]

## Skill Version(s):

1.3.23 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
