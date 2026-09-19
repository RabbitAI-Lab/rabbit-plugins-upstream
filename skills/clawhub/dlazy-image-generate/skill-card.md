## Description:

Image generation skill that selects a suitable dLazy CLI image model based on the user's prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route image generation, image editing, upscaling, matting, and vectorization requests through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and explicitly supplied local files may be sent to dLazy's hosted service, and generated outputs are hosted by dLazy.

Mitigation: Use this skill only when that hosted-service data flow is acceptable; avoid passing sensitive local files unless upload is intended.

Risk: The dLazy API requires an API key and may consume account credits.

Mitigation: Prefer on-demand npx use when a persistent CLI is unnecessary, and rotate or revoke the API key when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI output references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dLazy CLI returns JSON envelopes and hosted output URLs; local media files explicitly passed to commands may be uploaded to dLazy.]

## Skill Version(s):

1.3.18 (source: ClawHub release evidence; artifact frontmatter declares 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
