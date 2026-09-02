## Description:

GPT Image 2 model for text-to-image and image editing, including generation from prompts and image editing or synthesis from reference inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call the dLazy GPT Image 2 service for text-to-image generation and reference-image editing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local image inputs passed to the skill are sent to dLazy, and generated outputs are hosted by dLazy.

Mitigation: Avoid passing private or sensitive images or prompts unless uploading them to the dLazy service is acceptable.

Risk: Authentication uses a dLazy API key that may be stored in the local CLI configuration.

Mitigation: Use per-invocation environment variables when appropriate, protect the local configuration file, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: Global CLI installation persists the dLazy CLI on the local system.

Mitigation: Use the pinned npx invocation when a non-persistent CLI execution path is preferred.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [JSON responses with generated image URLs, optional downloaded image files, and Markdown guidance for command usage or errors]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers when no-wait mode is used; generated media URLs are hosted by dLazy.]

## Skill Version(s):

1.3.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
