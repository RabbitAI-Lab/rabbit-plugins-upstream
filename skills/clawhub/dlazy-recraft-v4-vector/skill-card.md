## Description:

Uses the dLazy CLI to call the hosted Recraft V4 Vector API for text-prompt image generation aimed at logos, icons, and scalable design workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use this skill to have an agent invoke dLazy's hosted Recraft V4 Vector generation workflow from text prompts and retrieve generated image assets or asynchronous task status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill advertises SVG/vector output while the documented successful output example returns image/png.

Mitigation: Test representative prompts and inspect returned mimeType and saved files before relying on editable or scalable vector output.

Risk: Prompts, parameters, and optional local media inputs are sent to dLazy API and storage endpoints.

Mitigation: Avoid submitting sensitive or restricted content unless the service terms and organizational policy permit that use.

Risk: The workflow requires a dLazy API key that may be stored locally or supplied through an environment variable.

Mitigation: Use least-privilege access, protect the local config file, and rotate or revoke keys when access changes.

Risk: The skill relies on a pinned third-party npm CLI to perform networked generation requests.

Mitigation: Install the pinned CLI version from the disclosed package source and review the package or source repository before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI command guidance and JSON results containing generated image URLs, with optional saved image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful documented outputs use image/png URLs; asynchronous runs may return a generateId for later polling.]

## Skill Version(s):

1.3.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
