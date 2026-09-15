## Description:

PixVerse C1 is a dLazy cloud video-generation skill for text-to-video, image-to-video, first/last-frame-to-video, and reference-guided video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent invoke dLazy's PixVerse C1 model for video generation from prompts, image references, or first and last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an external npm CLI package and dLazy cloud API.

Mitigation: Install only if you trust the dLazy CLI package and service; use npx or an isolated environment when avoiding a persistent global binary.

Risk: API keys, prompts, parameters, and selected local media files are handled by the external CLI and cloud API.

Mitigation: Use organization-scoped dLazy API keys, rotate or revoke keys when needed, and avoid sending sensitive prompts or media unless the service is approved for that data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, json, files, guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result envelopes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs, saved output files, or an asynchronous generation task identifier.]

## Skill Version(s):

1.2.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
