## Description:

Generate and edit images with Flux Kontext through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to have an agent generate, edit, or transform images with Flux Kontext through RunAPI. It supports one-off CLI use and SDK-oriented integration guidance for application or backend workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can submit paid RunAPI tasks and send selected input media to RunAPI.

Mitigation: Confirm authentication, request details, and user authorization before submission; submit only once and do not replace a paid task without explicit approval.

Risk: Generated image deliverables may be incomplete, empty, or returned in an unexpected media type.

Mitigation: Download every requested media result and verify each file is non-empty and matches the expected image MIME type before reporting completion.

Risk: The installed CLI contract or API reference may differ from expected request fields.

Mitigation: Discover the current service and operation contract before building requests, and stop on contract mismatches or unresolved required fields instead of guessing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-flux-kontext)
- [RunAPI Flux Kontext model overview](https://runapi.ai/models/flux-kontext.md)
- [RunAPI Black Forest Labs provider overview](https://runapi.ai/providers/black-forest-labs.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Flux Kontext SDK](https://github.com/runapi-ai/flux-kontext-sdk)
- [RunAPI Flux Kontext homepage](https://runapi.ai/models/flux-kontext)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to produce request JSON, task/result files, verified image downloads, SDK integration code, or stop-condition guidance depending on the user request.]

## Skill Version(s):

0.2.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
