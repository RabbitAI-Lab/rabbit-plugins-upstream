## Description: <br>
Call the DeepSeek API (deepseek-v4-pro, deepseek-v4-flash) through RunAPI using the official OpenAI SDK, Anthropic SDK, or compatible clients. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to configure agents and existing LLM SDK integrations for DeepSeek models through RunAPI. It provides setup guidance, code examples, streaming patterns, protocol compatibility notes, and constraints for the supported DeepSeek model subset. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and generated content are routed through RunAPI for DeepSeek requests, which can expose sensitive data to that service path. <br>
Mitigation: Use the skill only when routing through RunAPI is intended, and review RunAPI data-handling expectations before sending sensitive prompts. <br>
Risk: RunAPI tokens can be exposed if copied into source files, commits, or shell history. <br>
Mitigation: Keep tokens in environment variables or a secret manager, and avoid inline credentials in committed code or long-lived command history. <br>
Risk: Pricing, rate limits, and commercial usage terms may affect deployment decisions. <br>
Mitigation: Review the linked RunAPI DeepSeek model overview for current pricing, rate limits, and usage expectations before production use. <br>
Risk: Requests outside the documented cross-protocol subset may fail or behave differently than examples. <br>
Mitigation: Stay within the documented model, streaming, and single-function constraints, and treat unsupported advanced fields as integration risks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-deepseek) <br>
- [RunAPI DeepSeek model overview](https://runapi.ai/models/deepseek.md) <br>
- [RunAPI DeepSeek provider comparison](https://runapi.ai/providers/deepseek.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>
- [RunAPI DeepSeek homepage](https://runapi.ai/models/deepseek) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python, TypeScript, dotenv, and curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes environment-variable requirements, compatible API base URLs, model IDs, streaming guidance, and protocol constraints.] <br>

## Skill Version(s): <br>
0.1.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
