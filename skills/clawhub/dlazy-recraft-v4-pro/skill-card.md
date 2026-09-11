## Description:

4MP high-resolution raster image generation for print-ready assets and large-scale visual use cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate high-resolution raster images through the dLazy hosted Recraft V4 Pro workflow, including print-oriented and large-format visual assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party npm CLI and a hosted image-generation service.

Mitigation: Review the linked source or package before installation, prefer npx or a non-privileged environment when appropriate, and avoid running npm or the CLI as root or administrator.

Risk: Prompts, parameters, API keys, and media files may be sent to or used with dLazy's hosted service.

Mitigation: Only submit prompts and files that are appropriate for the service, keep API keys scoped to the user's organization, and rotate or revoke keys from the provider dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent can request asynchronous generation, return a task identifier, or save generated image assets through the dLazy CLI.]

## Skill Version(s):

1.3.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
