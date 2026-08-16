## Description:

Generate and edit video with Seedance through RunAPI for one-off CLI generation or SDK-backed application integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to create, edit, or transform video with Seedance through RunAPI, using the CLI for one-off tasks and SDK guidance for application or backend integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts or referenced media files may be sent to RunAPI for Seedance video generation.

Mitigation: Review request.json before submission, especially when handling sensitive media.

Risk: Submitting a RunAPI task may create billable work.

Mitigation: Authenticate intentionally, submit each task once, and request user authorization before replacing a paid task after a service failure.

Risk: Interactive browser login can expose an unintended account flow in automated agent sessions.

Mitigation: Prefer an environment-provided RUNAPI_API_KEY or saved CLI configuration, and use browser login only when explicitly chosen.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/runapi-ai/skills/runapi-seedance)
- [RunAPI Seedance Homepage](https://runapi.ai/models/seedance)
- [RunAPI Seedance Model Overview](https://runapi.ai/models/seedance.md)
- [RunAPI ByteDance Provider Overview](https://runapi.ai/providers/bytedance.md)
- [RunAPI Model Catalog](https://runapi.ai/models.md)
- [RunAPI Seedance SDK](https://github.com/runapi-ai/seedance-sdk)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, JSON, Files, Guidance]

**Output Format:** [Markdown with shell commands, JSON request and task artifacts, SDK code guidance, and downloaded video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces or verifies video deliverables through RunAPI tasks; requires complete response validation before reporting completion.]

## Skill Version(s):

0.2.12 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
