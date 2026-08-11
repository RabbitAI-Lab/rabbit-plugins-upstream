## Description:

Generate and transform music or compose lyrics with Suno through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to guide agents through Suno music, lyric, audio transformation, and custom voice workflows via RunAPI. It distinguishes one-off CLI tasks from SDK-based application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, uploaded audio, lyrics, and voice samples may be sent to external RunAPI/Suno services.

Mitigation: Use the skill only in environments where sending that data to RunAPI/Suno is approved.

Risk: API keys or CLI authentication may grant access to RunAPI-backed generation workflows.

Mitigation: Prefer RUNAPI_API_KEY or saved CLI config in controlled environments, and use browser login only when interactive authentication is explicitly acceptable.

Risk: Generated file URLs are temporary and may not remain available as durable assets.

Mitigation: Download and store generated audio, image, video, or related files in durable storage within 7 days.

Risk: Using the CLI as a production integration layer can make application behavior harder to control.

Mitigation: Use the appropriate RunAPI SDK for app, backend, worker, library, webhook, or production integration work.

## Reference(s):

- [RunAPI Suno homepage](https://runapi.ai/models/suno)
- [RunAPI Suno model overview, pricing, and rate limits](https://runapi.ai/models/suno.md)
- [RunAPI Suno provider comparison](https://runapi.ai/providers/suno.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-suno)
- [RunAPI publisher profile](https://clawhub.ai/user/runapi-ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference RunAPI CLI commands, SDK packages, environment authentication, and generated asset handling.]

## Skill Version(s):

0.4.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
