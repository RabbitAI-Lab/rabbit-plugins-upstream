## Description:

Generate video from text, reference media, or first and last frames with MiniMax H3 through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate MiniMax H3 videos through RunAPI for one-off CLI tasks, manual testing, and application integrations through language SDKs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, reference media, and generated video requests may be processed by RunAPI and may consume paid quota.

Mitigation: Use this skill only when the user is comfortable with RunAPI handling the generation request and any associated billing.

Risk: RunAPI credentials could be exposed if copied into source files or command history carelessly.

Mitigation: Keep API keys in RUNAPI_API_KEY or saved RunAPI CLI configuration and do not commit secrets.

Risk: Generated file URLs are temporary and may expire before downstream use.

Mitigation: Download generated files into durable storage within the retention window.

Risk: Using the CLI as a production integration layer can create brittle application behavior.

Mitigation: Use the language SDK path for application, backend, worker, service, or webhook integrations.

## Reference(s):

- [MiniMax H3 model overview, pricing, and rate limits](https://runapi.ai/models/minimax-h3.md)
- [RunAPI MiniMax H3 homepage](https://runapi.ai/models/minimax-h3)
- [MiniMax provider comparison](https://runapi.ai/providers/minimax.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-minimax-h3)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell commands and SDK package guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference RunAPI authentication, request JSON files, asynchronous task polling, SDK package choices, and temporary generated file URLs.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
