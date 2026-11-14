## Description:

Generate images, video, speech, music, 3D and LLM output with Wiro AI models through the Wiro MCP server or REST API, including finding a model, checking its price, running it and collecting the result. Use when the user wants generative media or LLM calls through an API, or mentions Wiro, wiro.ai or a Wiro API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wiroai](https://clawhub.ai/user/wiroai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to find and run Wiro AI models through the MCP server or REST API, check model pricing, and collect generated results. It also guides application code that calls Wiro's LLM gateway.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conversation history may be sent to an external LLM service without clear limits.

Mitigation: Review what conversation content the selected model route sends and limit it to information appropriate for that service.

Risk: The installation instructions recommend running an unpinned package.

Mitigation: Review the package and pin the version before installing or running it.

Risk: The security scan was partial because two local references could not be resolved.

Mitigation: Resolve and review the missing references before treating the scan as complete.

## Reference(s):

- [Wiro API introduction](https://wiro.ai/docs/introduction)
- [Run a model](https://wiro.ai/docs/run-a-model)
- [Tasks](https://wiro.ai/docs/tasks)
- [Pricing](https://wiro.ai/docs/pricing)
- [LLM completions API](https://wiro.ai/docs/completions-api)
- [Wiro MCP server](https://wiro.ai/docs/wiro-mcp-server)
- [WebSocket](https://wiro.ai/docs/websocket)

## Skill Output:

**Output Type(s):** [API calls, Text, Generated media, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with JSON and shell examples; model results may include text or generated media files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated result types depend on the selected Wiro model.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
