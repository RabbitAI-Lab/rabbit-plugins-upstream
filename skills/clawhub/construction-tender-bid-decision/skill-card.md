## Description: <br>
面向施工、市政、装修、园林、公路和房建等工程项目，帮助投标团队基于知了标讯历史招中标数据评估是否投标、潜在竞争者、报价区间、资质门槛和废标风险。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonzu](https://clawhub.ai/user/dragonzu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
投标、商务和项目团队可用此技能对具体工程类招标项目做投标决策分析，形成是否参与、竞争格局、报价参考、资质门槛、废标风险和后续行动建议。它适合需要基于公开招中标历史数据快速评估施工项目机会和风险的商业场景。 <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can auto-register an account, collect device-derived identifiers, and write credentials to ~/.zlbx/config.json. <br>
Mitigation: Prefer a user-provided ZLBX_API_KEY when available; if no key exists, obtain explicit consent before registration and collect only the documented platform, architecture, and hashed MAC values. <br>
Risk: Generated HTML reports and citation links may contain signed access URLs and commercially sensitive bid-analysis conclusions. <br>
Mitigation: Treat reports as sensitive business documents, share them only with intended recipients, and preserve API-returned links without exposing unnecessary additional records. <br>
Risk: Bid recommendations based on incomplete public tender data could mislead business decisions or create reputational risk when discussing real organizations. <br>
Mitigation: Separate facts from inferences, state data gaps and confidence, avoid accusatory language, and require numeric claims, company names, and amounts to come from returned data. <br>
Risk: Full analysis consumes paid API credits and may exceed the expected budget for broad investigations. <br>
Mitigation: Tell the user the expected credit range before analysis, use the quick mode when requested, and pause for approval before exceeding the documented call budget. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/construction-tender-bid-decision) <br>
- [Publisher profile](https://clawhub.ai/user/dragonzu) <br>
- [API quick reference](references/api-quick.md) <br>
- [Bid decision workflow](references/workflow.md) <br>
- [Report template](references/report-template.md) <br>
- [Auto-registration flow](references/auto-register.md) <br>
- [ZLBX API endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{工具名}) <br>
- [ZLBX account portal](https://ai.zhiliaobiaoxun.com/?ch=s69) <br>
- [ZLBX business intelligence portal](https://agent.zhiliaobiaoxun.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, HTML, guidance, configuration] <br>
**Output Format:** [Markdown bid-decision report with an optional self-contained HTML report and concise setup or account guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved auto-registration. Complete analysis uses about 12-25 API calls; quick analysis uses about 5-8 API calls.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
