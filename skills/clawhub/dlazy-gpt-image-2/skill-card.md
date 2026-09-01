## Description:

Provides a dLazy CLI wrapper for GPT Image 2 text-to-image generation and image editing with optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to invoke dLazy's hosted GPT Image 2 service for generating images from prompts or editing and synthesizing images from up to five reference inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-provided media are sent to dLazy's hosted API and media storage when the skill is invoked.

Mitigation: Review dLazy's service terms and only pass prompts or files that are appropriate to upload to the hosted service.

Risk: Authentication commands can save the dLazy API key in local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable per invocation when local credential persistence is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI metadata source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Files, Guidance]

**Output Format:** [JSON responses with generated image URLs and optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and user-provided media are sent to dLazy hosted API endpoints when invoked.]

## Skill Version(s):

1.3.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
