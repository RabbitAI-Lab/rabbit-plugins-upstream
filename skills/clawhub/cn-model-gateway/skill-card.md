## Description: <br>
CN Model Gateway is a local Python gateway that exposes MCP and agent-framework adapters for sending text prompts to configured Chinese model providers such as DeepSeek, Tongyi, Zhipu GLM, Kimi, Hunyuan, Doubao, MiniMax, LingYi, Baichuan, and StepFun. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to connect MCP-compatible tools and other agent frameworks to multiple Chinese text model APIs through one local gateway. It supports asking one model, comparing multiple providers, listing available providers, checking health, reading configuration and usage summaries, and using prompt templates for code review and translation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and generated content are sent to the configured third-party model providers. <br>
Mitigation: Use only providers approved for the data being processed, and avoid compare_models for sensitive prompts unless every selected provider is acceptable. <br>
Risk: Provider API keys can be exposed if configuration files are shared or committed. <br>
Mitigation: Keep config.json private, do not commit API keys, and limit access to the local configuration directory. <br>
Risk: Model calls may consume paid provider quota. <br>
Mitigation: Monitor usage with the built-in stats functionality and configure provider-side quota or billing alerts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/cn-model-gateway) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [MCP JSON-RPC responses, command-line text, framework adapter outputs, and markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May send user prompts to configured third-party model providers and may record local usage statistics in SQLite.] <br>

## Skill Version(s): <br>
1.2.0 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
