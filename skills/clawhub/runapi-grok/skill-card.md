## Description:

Call Grok 4.3, 4.5, and Grok 4.20 non-reasoning through RunAPI using OpenAI-compatible Chat Completions and Responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure agents or compatibility clients for Grok requests through RunAPI, including chat, responses, streaming, tool use, structured output, and conditional Anthropic or Gemini protocol compatibility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: RunAPI credentials can be exposed if real tokens are hardcoded in files or prompts.

Mitigation: Store the RunAPI key in environment variables or a secret manager and avoid placing real tokens in source files or prompt text.

Risk: Prompts and tool inputs are sent to the configured external API endpoint.

Mitigation: Install and use this skill only when routing Grok requests through RunAPI is intended and approved for the data being processed.

Risk: Automatic retries or protocol changes can create duplicate requests or unexpected model behavior.

Mitigation: Follow the skill guidance to make at most one safe pre-response transport retry, correct one rejected shape, and stop without changing model or protocol.

## Reference(s):

- [RunAPI Grok documentation](https://runapi.ai/models/grok.md)
- [RunAPI xAI provider page](https://runapi.ai/providers/xai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Grok homepage](https://runapi.ai/models/grok)
- [Grok compatibility protocols](references/compatibility-protocols.md)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown guidance with Python snippets and endpoint configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OPENAI_API_KEY and OPENAI_BASE_URL; prompts and tool inputs are sent to the configured RunAPI endpoint.]

## Skill Version(s):

0.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
