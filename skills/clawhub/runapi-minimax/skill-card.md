## Description:

Call the MiniMax text API (MiniMax-M3 through MiniMax-M2) through RunAPI using OpenAI-compatible Chat Completions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to call MiniMax text chat through RunAPI, including streaming chat completions and compatibility guidance for existing Anthropic Messages or Gemini contents clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A globally configured OpenAI-compatible client could send an unrelated OpenAI API key to RunAPI if the environment variables are reused carelessly.

Mitigation: Configure OPENAI_API_KEY and OPENAI_BASE_URL deliberately in a project-specific shell or secret manager before using the skill.

Risk: Streaming or compatibility-client calls can be treated as complete before final content, finish status, and usage metadata are available.

Mitigation: Verify final assistant content, finish reason, authoritative usage, and the documented terminal stream marker before accepting a result.

## Reference(s):

- [RunAPI MiniMax model documentation](https://runapi.ai/models/minimax.md)
- [RunAPI MiniMax provider page](https://runapi.ai/providers/minimax.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI MiniMax homepage](https://runapi.ai/models/minimax)
- [MiniMax compatibility protocols](references/compatibility-protocols.md)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-minimax)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown with Python examples, endpoint configuration, and verification guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance includes required RunAPI environment variables, model IDs, streaming completion checks, and stop boundaries.]

## Skill Version(s):

0.1.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
