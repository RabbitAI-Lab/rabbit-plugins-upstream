## Description:

Call MiniMax text models through RunAPI using the official OpenAI SDK or compatible OpenAI, Anthropic, and Gemini-style clients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure MiniMax text chat and streaming completions through RunAPI, including OpenAI-compatible clients and compatibility paths for Anthropic or Gemini-style callers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys can be exposed if copied into source files, commits, or shell history.

Mitigation: Keep the RunAPI token in environment variables or a secret manager and avoid embedding it directly in code or command history.

Risk: MiniMax text requests are routed through RunAPI when the base URL is configured for this skill.

Mitigation: Install and use the skill only when that routing is intended, and set OPENAI_BASE_URL explicitly to https://runapi.ai/v1.

## Reference(s):

- [RunAPI MiniMax Homepage](https://runapi.ai/models/minimax)
- [MiniMax Model Overview](https://runapi.ai/models/minimax.md)
- [MiniMax Provider Comparison](https://runapi.ai/providers/minimax.md)
- [RunAPI Model Catalog](https://runapi.ai/models.md)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown with dotenv, Python, TypeScript, and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OPENAI_API_KEY and OPENAI_BASE_URL for RunAPI requests.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
