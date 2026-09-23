## Description:

GPT Image 2 model for text-to-image and image editing, supporting image generation from text and image editing or synthesis with reference inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to call the dLazy GPT Image 2 CLI for text-to-image generation, image editing, and image synthesis with up to five reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party npm CLI and a dLazy account for hosted image generation.

Mitigation: Review the referenced CLI package and source before installation, and use the pinned npx or npm install command from the artifact.

Risk: Prompts and local reference files may be uploaded to dLazy API and media storage endpoints.

Mitigation: Avoid submitting sensitive prompts or private media unless the user's dLazy account, organization policy, and service terms permit that use.

Risk: The dLazy API key can be saved in local CLI configuration.

Mitigation: Use the per-invocation DLAZY_API_KEY environment variable for temporary use, or rotate and revoke saved keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON responses with generated image URLs and optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs with later polling when --no-wait is used.]

## Skill Version(s):

1.3.19 (source: ClawHub release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
