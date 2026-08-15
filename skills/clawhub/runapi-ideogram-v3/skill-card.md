## Description:

Generate and edit images with Ideogram V3 through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agent users use this skill to create, edit, or transform images with Ideogram V3 through RunAPI. It supports one-off CLI generation and SDK-oriented integration work when the user is building an application or backend.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected input media are processed by the external RunAPI service.

Mitigation: Use the skill only when the user is comfortable sending that content to RunAPI, and avoid submitting sensitive media or prompts unless authorized.

Risk: RunAPI API keys or saved CLI login state can authorize paid or private service access.

Mitigation: Prefer environment authentication or saved CLI configuration, treat credentials as sensitive, and use browser login only when the user explicitly requests it.

Risk: A failed or timed-out generation task could lead to duplicate paid submissions if retried incorrectly.

Mitigation: Persist the task response, wait on the same task ID, and submit another paid request only with user authorization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-ideogram-v3)
- [RunAPI Ideogram V3 homepage](https://runapi.ai/models/ideogram-v3)
- [Model overview, pricing, and rate limits](https://runapi.ai/models/ideogram-v3.md)
- [Ideogram provider overview](https://runapi.ai/providers/ideogram.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [SDK integration](https://github.com/runapi-ai/ideogram-v3-sdk)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, files]

**Output Format:** [Markdown guidance with shell commands, JSON request and response files, optional SDK code, and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [For media deliverables, the skill requires complete response validation and non-empty downloaded files with the expected image MIME type.]

## Skill Version(s):

0.2.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
