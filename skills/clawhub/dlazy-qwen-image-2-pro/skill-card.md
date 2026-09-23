## Description:

Alibaba Bailian qwen-image-2.0-pro general image generation for complex text rendering, multi-line layouts, photorealistic detail, and strong semantic adherence in mixed text and image designs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to call dLazy's hosted Qwen Image 2 Pro integration from an agent workflow, producing images from prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill requires a dLazy API key that may be stored locally by the CLI.

Mitigation: Use the CLI's documented authentication flow, restrict local config access, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Prompts and files explicitly passed to the command are sent to dLazy's hosted service.

Mitigation: Avoid passing sensitive prompts or local files unless uploading them to the hosted service is intended.

Risk: A persistent global CLI install may be undesirable in managed environments.

Mitigation: Use the pinned npx invocation when a temporary execution path is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill invokes a hosted image-generation API and can return generated image URLs or asynchronous task identifiers.]

## Skill Version(s):

1.3.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
