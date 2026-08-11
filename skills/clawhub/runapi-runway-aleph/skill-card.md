## Description:

Generate and edit video with Runway Aleph through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agents use this skill to create, edit, or transform videos with Runway Aleph through RunAPI for one-off generation tasks or application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media inputs may be sent to an external video generation service.

Mitigation: Confirm trust in RunAPI before installation and avoid sending sensitive media or prompts unless approved for the use case.

Risk: Authentication may rely on local saved CLI state or an API key.

Mitigation: Prefer RUNAPI_API_KEY for headless runs, protect the token as a secret, and use browser login only when local authentication state is intentional.

Risk: Generated file URLs are temporary.

Mitigation: Download generated assets and move them to durable storage within the documented retention window.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/runapi-ai/skills/runapi-runway-aleph)
- [RunAPI Runway Aleph Model](https://runapi.ai/models/runway-aleph)
- [RunAPI Runway Aleph Documentation](https://runapi.ai/models/runway-aleph.md)
- [RunAPI Runway Provider](https://runapi.ai/providers/runway.md)
- [RunAPI Model Catalog](https://runapi.ai/models.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands, SDK package names, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to use the RunAPI CLI for one-off tasks and SDKs for application integration.]

## Skill Version(s):

0.2.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
