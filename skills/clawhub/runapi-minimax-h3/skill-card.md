## Description:

Generate video from text, reference media, or first and last frames with MiniMax H3 through RunAPI. Use the RunAPI CLI for one-off generation and an SDK for application integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate MiniMax H3 video through RunAPI for one-off artifacts or application integrations. It guides contract discovery, request construction, task execution, result validation, and bounded recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be sent to RunAPI or MiniMax.

Mitigation: Review request.json for sensitive prompt or media content before submitting a task.

Risk: Generation tasks may create billable RunAPI work.

Mitigation: Authenticate with an approved RunAPI API key and submit only after confirming the request and selected operation.

Risk: Interactive browser login can use an unintended account context.

Mitigation: Prefer RUNAPI_API_KEY or saved CLI authentication and use browser login only when explicitly requested.

## Reference(s):

- [MiniMax H3 model overview](https://runapi.ai/models/minimax-h3)
- [MiniMax H3 documentation](https://runapi.ai/models/minimax-h3.md)
- [MiniMax provider overview](https://runapi.ai/providers/minimax.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [MiniMax H3 SDK integration](https://github.com/runapi-ai/minimax-h3-sdk)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with inline shell commands and JSON request or response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local media downloads and preserved task or result JSON when the agent follows the workflow.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
