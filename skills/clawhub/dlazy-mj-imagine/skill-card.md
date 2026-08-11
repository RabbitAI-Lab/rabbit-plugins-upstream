## Description:

Midjourney style generation with aspect-ratio, bot-type, and grid or U1-U4 output controls for artistic and strongly stylized image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to call the pinned dLazy CLI for Midjourney-style image generation with prompt, aspect ratio, bot type, and output-slot controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media files are sent to dLazy cloud endpoints for generation.

Mitigation: Use the skill only with content appropriate for dLazy's hosted service and avoid sending sensitive prompts or media unless that use is approved.

Risk: The skill depends on a third-party CLI and stores or reads a dLazy API key for authenticated calls.

Mitigation: Use the pinned npx or install command from the release metadata, review the third-party CLI before use, and rotate or revoke the API key from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [dLazy CLI repository](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON, image URLs]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses dLazy CLI command output; completed image results are returned as files.dlazy.com URLs, while asynchronous runs return a generateId for polling.]

## Skill Version(s):

1.3.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
