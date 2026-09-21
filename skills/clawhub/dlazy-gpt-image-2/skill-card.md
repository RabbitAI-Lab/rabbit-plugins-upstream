## Description:

GPT Image 2 supports text-to-image generation and image editing or synthesis using reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to generate images from text prompts and edit or synthesize images with up to five reference inputs through the dLazy hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local image paths may be uploaded to dLazy's hosted API and media storage.

Mitigation: Avoid sending sensitive prompts or media unless the user accepts dLazy's service handling and data exposure.

Risk: Authentication can store a dLazy API key in the local user configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard as needed.

Risk: The skill depends on a third-party CLI and hosted API rather than NVIDIA-operated infrastructure.

Mitigation: Review the pinned npm package and prefer the documented npx invocation when a global install is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Guidance]

**Output Format:** [JSON responses with generated image URLs, plus optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return async task IDs when called with --no-wait; local saves are controlled by the --save option.]

## Skill Version(s):

1.3.18 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
