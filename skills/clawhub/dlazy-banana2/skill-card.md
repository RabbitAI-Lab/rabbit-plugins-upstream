## Description:

Generate and edit high-quality images with Nano Banana 2.0 for text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to ask an agent to generate or edit images through the dLazy Nano Banana 2 CLI, using text prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, reference images, and local paths passed to the skill are sent to the dLazy hosted service.

Mitigation: Use only data appropriate for dLazy processing and avoid sending sensitive prompts or files unless the user has approved that service.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Prefer per-invocation DLAZY_API_KEY where persistent storage is not acceptable, and rotate or revoke keys when needed.

Risk: Image-generation calls may be billable.

Mitigation: Use dry-run or explicit confirmation before calls where cost matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns image output URLs and may save generated assets locally when requested.]

## Skill Version(s):

1.3.10 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
