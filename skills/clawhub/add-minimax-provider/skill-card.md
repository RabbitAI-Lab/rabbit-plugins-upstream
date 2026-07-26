## Description: <br>
为 OpenClaw 配置 MiniMax 作为模型源，覆盖 API Key 直连、OAuth 门户、provider 注册、模型定义、别名、fallback 链和验证流程。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jooey](https://clawhub.ai/user/jooey) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
OpenClaw 管理员和开发者使用此 skill 将 MiniMax M2.1 模型接入 OpenClaw，并验证模型可用性、别名、fallback 链和 gateway 状态。 <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Configuration edits can break OpenClaw provider loading, model selection, or fallback behavior. <br>
Mitigation: Review proposed openclaw.json changes, keep a backup, run JSON validation and openclaw doctor, then restart and verify the gateway before relying on the provider. <br>
Risk: API keys, OAuth settings, billing state, quota limits, and prompts routed through MiniMax may expose sensitive operational or account data. <br>
Mitigation: Avoid sharing API keys in chat or logs, confirm MiniMax billing, quota, referral-link, and privacy terms, and test availability with a minimal request before production use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jooey/skills/add-minimax-provider) <br>
- [MiniMax Platform](https://platform.minimaxi.com) <br>
- [MiniMax Chat Completions Endpoint](https://api.minimaxi.com/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with JSON and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes provider configuration snippets, validation commands, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
