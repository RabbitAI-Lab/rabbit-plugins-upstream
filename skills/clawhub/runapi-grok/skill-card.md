## Description: <br>
Call Grok 4.3 and 4.5 through RunAPI with the official OpenAI SDK or compatible clients. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to configure Grok 4.3 and 4.5 requests through RunAPI with OpenAI-compatible clients, including Chat Completions, Responses, streaming, function tools, and structured JSON output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Requests may be routed to the wrong provider if OPENAI_BASE_URL is not set for RunAPI. <br>
Mitigation: Set OPENAI_BASE_URL to https://runapi.ai/v1 before using the examples. <br>
Risk: OPENAI_API_KEY may already contain a token for another provider in the user's environment. <br>
Mitigation: Confirm the value is a RunAPI token or use a secret manager with provider-specific scoping. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-grok) <br>
- [RunAPI Grok model page](https://runapi.ai/models/grok) <br>
- [Grok 4.3 overview and pricing](https://runapi.ai/models/grok/4.3.md) <br>
- [Grok 4.5 overview and pricing](https://runapi.ai/models/grok/4.5.md) <br>
- [RunAPI xAI provider page](https://runapi.ai/providers/xai.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown with dotenv, Python, and TypeScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance focuses on OpenAI-compatible RunAPI requests, environment variables, streaming usage events, function tools, and structured output examples.] <br>

## Skill Version(s): <br>
0.2.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
