## Description:

Generate images with the Kling O1 model from text prompts and optional reference images through the dLazy hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agent users can use this skill to request text-to-image or image-to-image generation with Kling O1. It is suited for workflows where an agent prepares prompts, passes optional reference images, and returns generated image URLs or saved image files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected input images are sent to dLazy's hosted API and media storage.

Mitigation: Avoid submitting sensitive prompts or local files unless that data transfer is acceptable for the user's workflow.

Risk: The skill depends on a third-party npm CLI whose implementation is outside the skill artifact.

Mitigation: Prefer the pinned npx or install command from the metadata and review the linked CLI source or npm package before deployment.

Risk: dLazy API keys may be stored in local CLI configuration or passed through the environment.

Mitigation: Protect the key, restrict local file access, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands; CLI responses are JSON with generated image URLs or async task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save generated images to a local path when the CLI is invoked with --save.]

## Skill Version(s):

1.3.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
