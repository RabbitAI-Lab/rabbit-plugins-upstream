## Description:

A comprehensive generation skill that helps an agent generate images, videos, and audio by selecting an appropriate dLazy CLI model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route multimodal media generation requests to dLazy CLI commands for image, video, audio, enhancement, segmentation, vectorization, and lip-sync workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the external dLazy npm CLI and sends prompts and selected media files to dLazy cloud services.

Mitigation: Review the CLI source and install only in an environment where sending the requested prompts and media to dLazy is acceptable.

Risk: Authentication can persist a dLazy API key in the user's local CLI configuration.

Mitigation: Use a per-run DLAZY_API_KEY or an isolated environment when credentials should not be persisted, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Generation requests may consume dLazy account credits.

Mitigation: Confirm the intended model and request before execution and monitor account credits for charge-sensitive workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text, JSON]

**Output Format:** [Markdown with inline shell commands and JSON command output references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or reference generated media URLs hosted by dLazy services.]

## Skill Version(s):

1.3.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
