## Description: <br>
微信AI接入顾问 helps WeChat mini-program merchants, operations teams, and developers choose an AI integration mode and generate structured GEO data, integration plans, code skeletons, test matrices, and launch checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huangjihua007-rgb](https://clawhub.ai/user/huangjihua007-rgb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External merchants, operations teams, digital leads, and developers use this skill to plan WeChat mini-program AI integration, compare development and automatic modes, structure product and service data, and draft integration artifacts and code skeletons. <br>

### Deployment Geography for Use: <br>
Global, for teams building WeChat mini-program experiences. <br>

## Known Risks and Mitigations: <br>
Risk: Generated code and configuration drafts may contain inappropriate permissions, backend URLs, token handling, or business-flow assumptions if used directly. <br>
Mitigation: Review generated code, mcp.json, AGENTS.md, and SKILL.md before implementation, and replace placeholders with approved service endpoints, permission scopes, and token handling. <br>
Risk: Real mini-program integrations can involve phone numbers, addresses, payments, order confirmation, and privacy compliance obligations. <br>
Mitigation: Perform privacy and compliance review before use in a real app, and require explicit user confirmation for payment, order, address, and personal-information flows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huangjihua007-rgb/skills/wechat-aiagent-dev) <br>
- [Publisher profile](https://clawhub.ai/user/huangjihua007-rgb) <br>
- [微信小程序 AI 入门与接入模式](references/wechat-agent-basics.md) <br>
- [微信小程序 AI 开发模式 · 能力清单](references/ai-capabilities.md) <br>
- [行业接入示范](references/industry-cases.md) <br>
- [GEO 数据、测试与上线清单](references/geo-checklists.md) <br>
- [开发模式三件套模板](references/dev-mode-templates.md) <br>
- [代码生成模板](references/code-templates.md) <br>
- [微信官方 Demo 逐文件解读](references/demo-walkthrough.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with structured tables and inline code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include draft AGENTS.md, SKILL.md, mcp.json, app.json, JavaScript skeletons, GEO checklists, and test matrices for human review.] <br>

## Skill Version(s): <br>
1.4.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
