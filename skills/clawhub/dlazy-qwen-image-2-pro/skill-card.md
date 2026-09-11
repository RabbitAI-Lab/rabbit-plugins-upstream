## Description:

文生图 通义 Qwen Image 2 Pro helps an agent generate images with Alibaba Bailian qwen-image-2.0-pro through the dLazy CLI and hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to create images from text prompts and up to three reference images. It is suited for mixed text/image designs, photorealistic detail, multi-line layout, and Chinese-English content generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party npm CLI and hosted dLazy service.

Mitigation: Use npx or another isolated setup when avoiding a global install, and review the package or source before use in sensitive environments.

Risk: Prompts and referenced local files are sent to dLazy endpoints for generation.

Mitigation: Provide only prompts and files intended for upload, and avoid sensitive local paths or confidential media.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY when persistent local storage is not desired, and rotate or revoke keys from the service dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The underlying CLI can return hosted image URLs or an asynchronous generation ID; generated assets may be downloaded with the save option.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
