## Description:

Helps create commercial key visuals and brand assets with Seedream 5.0 Pro from text prompts and optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and brand teams use this skill to generate visual assets from text prompts, optionally using reference images and specifying an aspect ratio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy for generation.

Mitigation: Share only content you are comfortable sending to dLazy.

Risk: The CLI can store an API key in local configuration.

Mitigation: In sensitive environments, pass DLAZY_API_KEY per invocation and rotate or revoke any exposed key.

Risk: Running the skill requires installing or executing the dLazy CLI package.

Mitigation: Confirm you trust the dLazy CLI package before installing or running it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-pro)
- [dLazy CLI homepage (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown guidance and shell commands; CLI results contain JSON with generated image links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional reference images, aspect ratio selection, and asynchronous generation.]

## Skill Version(s):

1.2.21 (source: ClawHub release metadata; skill frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
