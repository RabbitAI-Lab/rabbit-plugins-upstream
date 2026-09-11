## Description:

Image super-resolution tool that enhances image clarity and details, returning an enhanced URL for low-resolution asset restoration and upscaling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run dLazy image super-resolution through the dLazy CLI, sending an image URL or local image path and receiving an enhanced image URL or saved output asset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or runs an external dLazy CLI package.

Mitigation: Review the linked CLI source and npm package before use, prefer pinned npx execution when a persistent global binary is not desired, and avoid elevated npm installs.

Risk: The skill requires a dLazy API key and stores or reads credentials through local CLI configuration or environment variables.

Mitigation: Use a revocable dLazy API key, restrict access to local configuration files, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Prompts and selected media files are sent to dLazy hosted endpoints for processing.

Mitigation: Only submit media and prompts that are appropriate for the dLazy service, and account for external processing at api.dlazy.com and files.dlazy.com.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI may return hosted image URLs, asynchronous task identifiers, or save enhanced image assets locally when requested.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
