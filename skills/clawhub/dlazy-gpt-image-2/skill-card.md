## Description:

GPT Image 2 generates images from text prompts and edits or synthesizes images from reference inputs through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users invoke this skill to generate new images from prompts or edit and synthesize images using reference inputs. It is useful for agent workflows that need dLazy-hosted GPT Image 2 image generation with CLI-based authentication, dry-run, async, and save options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and local reference media may be sent to dLazy cloud endpoints for hosted generation.

Mitigation: Only submit media and prompts that are appropriate for the user's dLazy organization and data-handling requirements.

Risk: The skill depends on an API key and a third-party npm CLI package.

Mitigation: Review the dLazy CLI package or source before installing in sensitive environments, avoid administrator privileges, and rotate or revoke API keys when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy Homepage](https://dlazy.com)
- [dLazy CLI Source Link from Metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Configuration instructions, Guidance]

**Output Format:** [JSON responses with generated image URLs; optional downloaded image files when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; local reference media may be uploaded to dLazy media storage for generation.]

## Skill Version(s):

1.3.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
