## Description:

Generate and edit video with Runway through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create, edit, or transform Runway videos through RunAPI. It guides one-off CLI generation and SDK-based application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation requests and media are sent to an external RunAPI service.

Mitigation: Use the skill only when external RunAPI processing is acceptable for the user's data and workflow.

Risk: RUNAPI_API_KEY or saved CLI login credentials grant access to RunAPI operations.

Mitigation: Treat API keys and saved login state as credentials, prefer environment-based auth for agents, and avoid exposing tokens in prompts, logs, or generated files.

Risk: RunAPI-generated file URLs are temporary.

Mitigation: Download generated media and store it in durable storage within 7 days when the output must be retained.

## Reference(s):

- [RunAPI Runway model overview](https://runapi.ai/models/runway)
- [Runway model documentation](https://runapi.ai/models/runway.md)
- [Runway provider comparison](https://runapi.ai/providers/runway.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands and SDK package guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference temporary generated media URLs that should be downloaded to durable storage within 7 days.]

## Skill Version(s):

0.2.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
