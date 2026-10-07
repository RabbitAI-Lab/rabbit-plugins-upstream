## Description:

Guides agents in calling Gemini models through RunAPI using Gemini contents clients, with compatibility guidance for existing Chat Completions clients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure RunAPI credentials, send Gemini requests, and check streaming responses. Existing Chat Completions clients can follow its separate compatibility guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and related request content are sent to RunAPI.

Mitigation: Use the skill only when this disclosure is acceptable, and review request content before sending it.

Risk: The RunAPI API key is sensitive.

Mitigation: Keep the key in the configured environment variable and avoid exposing it in shared requests or logs.

## Reference(s):

- [Gemini on RunAPI documentation](https://runapi.ai/models/gemini.md)
- [RunAPI Gemini homepage](https://runapi.ai/models/gemini)
- [RunAPI Google provider](https://runapi.ai/providers/google.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Compatibility protocols](references/compatibility-protocols.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers response-completion checks and bounded retry guidance.]

## Skill Version(s):

0.2.16 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
