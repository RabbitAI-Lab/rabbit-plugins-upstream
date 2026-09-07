## Description:

Generates 1MP raster images through the dLazy Recraft V4 CLI wrapper for everyday creative work and fast iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to create raster image assets with prompts and common aspect-ratio controls through the dLazy hosted generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party npm CLI and sends prompts and selected media files to dLazy hosted endpoints.

Mitigation: Install only after reviewing the linked CLI package/source, use the pinned one-off npx command when appropriate, and avoid submitting sensitive prompts or media unless approved for dLazy processing.

Risk: dLazy API keys are stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the local config and environment, use per-user credentials, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are returned as hosted image URLs and can be saved locally when the CLI save option is used.]

## Skill Version(s):

1.3.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
