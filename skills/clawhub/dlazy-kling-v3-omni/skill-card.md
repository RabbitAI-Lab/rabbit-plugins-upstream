## Description:

Generates videos with Kling v3 Omni from multimodal inputs such as images and prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to request Kling v3 Omni video generation from text prompts and supported image or video references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media supplied as references are sent to dLazy's hosted API and media storage.

Mitigation: Submit only prompts and media you are comfortable uploading to the service.

Risk: Video generation can incur account charges.

Mitigation: Review the CLI cost estimate and your account balance before starting a generation.

Risk: The CLI stores API credentials in a local configuration file.

Mitigation: Prefer the device login flow, protect the local configuration, and revoke keys that are no longer needed.

Risk: The skill relies on a pinned third-party CLI package.

Mitigation: Review the CLI package and its project information before installing it.

## Reference(s):

- [CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands]

**Output Format:** [JSON task results with generated media URLs; optionally a locally saved video file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is hosted by dLazy; asynchronous requests can return a task ID before completion.]

## Skill Version(s):

1.3.35 (source: evidence.json release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
