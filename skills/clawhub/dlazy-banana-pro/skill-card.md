## Description:

Generate and edit images with Nano Banana Pro through dLazy, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate or edit images with Nano Banana Pro. It supports prompt-only requests and reference-image workflows using local paths or image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media may be sent to dLazy's cloud image service.

Mitigation: Use the skill only with content appropriate for dLazy processing and review service terms before sending sensitive prompts or media.

Risk: Local file paths passed as media inputs can cause those files to be uploaded to dLazy storage.

Mitigation: Pass only intended files, prefer URLs or dry runs when checking requests, and avoid sensitive local media.

Risk: The dLazy CLI may store an API key in a local configuration file.

Mitigation: Use per-invocation DLAZY_API_KEY when persistent local credentials are not desired, and rotate or revoke the key from the dLazy dashboard when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted image URLs, asynchronous task IDs, or saved image files when requested.]

## Skill Version(s):

1.2.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
