## Description:

Generates and edits images from text prompts and optional reference images through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from prompts or edit images using reference inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied image files are sent to dLazy's hosted service.

Mitigation: Only submit content you are authorized to share with dLazy.

Risk: The dLazy CLI requires an API key and can store it locally.

Mitigation: Protect the key and revoke or rotate it from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Images]

**Output Format:** [CLI commands and JSON responses with image URLs; optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports prompt-based generation and editing with up to five reference images; asynchronous requests return a task ID.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
