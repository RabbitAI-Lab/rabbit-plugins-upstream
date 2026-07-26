## Description: <br>
Call the GLM API (glm-5.2, glm-5.1, glm-5-turbo, glm-5, glm-4.7, glm-4.6, glm-4.5, glm-4.5-air) through RunAPI using the official OpenAI SDK or compatible clients. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to configure RunAPI access for GLM chat, streaming completions, and OpenAI-, Anthropic-, or Gemini-compatible request patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and API payloads used with the examples are sent to RunAPI's service. <br>
Mitigation: Use this skill only when RunAPI is an approved provider for the workload, and avoid sending sensitive data unless covered by the user's data-handling requirements. <br>
Risk: RunAPI API keys can be exposed if copied into source files, commits, or shell history. <br>
Mitigation: Store the API key in OPENAI_API_KEY, RUNAPI_TOKEN, or a secret manager and avoid hard-coding credentials in examples or scripts. <br>
Risk: Unsupported GLM-5.2 features or oversized requests may be rejected rather than silently downgraded. <br>
Mitigation: Keep requests text-only, respect the documented context and output limits, and ask the user before removing rejected fields or changing request semantics. <br>


## Reference(s): <br>
- [RunAPI GLM model page](https://runapi.ai/models/glm) <br>
- [GLM model overview, pricing, and rate limits](https://runapi.ai/models/glm.md) <br>
- [Z.AI provider comparison](https://runapi.ai/providers/z-ai.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with dotenv, Python, TypeScript, and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires OPENAI_API_KEY and OPENAI_BASE_URL; examples send prompts and API payloads to RunAPI.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
