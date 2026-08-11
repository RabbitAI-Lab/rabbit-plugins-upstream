## Description:

GPT Image 2 model for text-to-image and image editing, supporting image generation from text and image editing or synthesis with reference inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's GPT Image 2 workflow for text-to-image generation and reference-based image editing through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A third-party CLI stores a dLazy API key in local user configuration.

Mitigation: Use the documented authentication flow deliberately, keep local configuration access restricted to the current OS user, and rotate or revoke the key from dLazy if needed.

Risk: Referenced local images are uploaded to dLazy for hosted image processing.

Mitigation: Review files before use and avoid sending sensitive images unless the user accepts dLazy processing and storage.

Risk: Global installation persists third-party tooling on the system.

Mitigation: Use npx @dlazy/cli@1.2.3 for on-demand execution when less persistent local tooling is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image outputs are returned as hosted URLs; asynchronous runs can return a generateId and status for polling.]

## Skill Version(s):

1.3.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
