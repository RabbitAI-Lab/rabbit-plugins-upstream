## Description: <br>
持续跟踪客户、潜在客户、重点账户、合作伙伴或竞争对手在官网、LinkedIn、新闻、招聘、展会和活动官网中的新增公开动态，区分业务信号、联系机会、战略变化、风险信号和无行动价值内容，并结合我方业务背景给出联系、观察、调查或风险升级建议，同时维护去重和处理状态。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales, account management, and business development users use this skill to monitor public account updates, classify business and risk signals, and decide whether to contact, observe, investigate, or escalate. It is intended for baseline scans, incremental account reviews, event-window opportunity checks, and follow-up monitoring against confirmed public or authorized sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Monitoring can create privacy or access-control risk if users include private accounts, non-public data, paywalled sources, or unauthorized sources. <br>
Mitigation: Use only public or explicitly authorized sources, do not bypass login or payment restrictions, and do not collect sensitive personal information. <br>
Risk: Event and status records may expose account intelligence if stored in an inappropriate system. <br>
Mitigation: Confirm where event and status records are stored in the deployment environment and limit retention and access to the intended account workflow. <br>
Risk: Automated monitoring could be mistaken for continuous background surveillance or unsupervised outreach. <br>
Mitigation: Use explicitly chosen monitoring intervals and keep outreach, scheduling, and notification automation outside this skill unless separately authorized. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-account-watch) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Structured Markdown report with parameter status, monitoring summary, signal analysis, recommended action, status updates, and source list.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chinese-language workflow output; may include signal IDs, event status, risk notes, and stop conditions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, README, changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
