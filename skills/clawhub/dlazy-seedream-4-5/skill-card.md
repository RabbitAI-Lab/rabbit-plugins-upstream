## Description:

Generate high-quality images with Doubao Seedream 4.5, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent generate or transform images through the dLazy CLI and hosted Doubao Seedream 4.5 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy's hosted API and media storage.

Mitigation: Use a revocable dLazy API key and avoid private images or sensitive prompts unless they are intended to be uploaded to dLazy.

Risk: The skill installs or invokes a third-party npm CLI.

Mitigation: Prefer npx or another isolated install path and review the pinned @dlazy/cli package before use.

Risk: CLI authentication can store an API key in the local user configuration.

Mitigation: Protect the local user account, rotate or revoke keys from the dLazy dashboard, or pass DLAZY_API_KEY per invocation when appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted image URLs from files.dlazy.com or save generated assets to a local path when requested.]

## Skill Version(s):

1.3.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
