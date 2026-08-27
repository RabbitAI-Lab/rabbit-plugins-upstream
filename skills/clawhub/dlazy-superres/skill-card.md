## Description:

Image super-resolution tool that enhances image clarity and detail and returns an enhanced image URL for restoration and upscaling workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and content teams use this skill through the pinned dLazy CLI to upscale low-resolution images and retrieve hosted enhanced image outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and prompts are sent to dLazy hosted endpoints for processing.

Mitigation: Upload only media intended for dLazy processing, and avoid private media unless the user accepts that hosted-service flow.

Risk: Authentication depends on a dLazy API key stored in CLI configuration or supplied through an environment variable.

Mitigation: Use OS-user-restricted config storage, rotate or revoke keys from the dLazy dashboard when needed, and avoid exposing keys in command history or shared logs.

Risk: A global CLI install persists a third-party executable on the system.

Mitigation: Use the pinned npx invocation, `npx @dlazy/cli@1.2.3`, when a persistent global install is not desired.

## Reference(s):

- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)
- [ClawHub Skill Release](https://clawhub.ai/dlazyai/skills/dlazy-superres)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Image URL, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return a hosted image URL or, with save options, a downloaded image file.]

## Skill Version(s):

1.3.10 (source: server release evidence; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
