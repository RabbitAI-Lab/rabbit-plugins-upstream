## Description:

Generate and remix images with Flux through RunAPI for one-off CLI work or SDK-based application integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to generate or transform Flux images through RunAPI, either by submitting a single CLI task or by integrating RunAPI SDKs into an application.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local input images may be sent to RunAPI for Flux image work.

Mitigation: Review prompts and image inputs for sensitive data before task submission, and use the skill only when the user accepts RunAPI processing.

Risk: RunAPI API credentials could be exposed if copied into logs, files, or prompts.

Mitigation: Prefer environment authentication or saved CLI configuration, keep RUNAPI_API_KEY protected, and import tokens from stdin when a key must be provided.

Risk: Successful submissions may create billable RunAPI tasks or duplicate paid requests.

Mitigation: Submit exactly once, persist task.json, wait on the same task id, and retry only when evidence confirms no task was created or billed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-flux)
- [RunAPI Flux model overview](https://runapi.ai/models/flux)
- [RunAPI Flux model documentation](https://runapi.ai/models/flux.md)
- [Black Forest Labs provider overview](https://runapi.ai/providers/black-forest-labs.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Flux SDK](https://github.com/runapi-ai/flux-sdk)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration, JSON, Files]

**Output Format:** [Markdown guidance with shell commands, JSON request and response artifacts, and file verification steps.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create RunAPI tasks that return image files; the skill requires complete response validation and media download verification before reporting completion.]

## Skill Version(s):

0.1.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
