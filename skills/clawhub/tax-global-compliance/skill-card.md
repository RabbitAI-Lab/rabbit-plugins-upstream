## Description: <br>
为中国企业出海提供国别用工、薪酬个税、跨境税务、数据出境、反洗钱反腐和知识产权等合规问答、自检与报告指引。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
企业财税、法务、人力资源和合规负责人使用该技能梳理中国企业出海时的国别用工、全球薪酬、税务、数据跨境、反洗钱反腐、知识产权和外资安全审查事项。它可生成合规问答、风险自检、整改优先级和报告草稿，但复杂交易和争议事项仍需当地执业专业机构复核。 <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts mcp.aitaxs.top for policy Q&A, risk checks, tax calculations, registration, and web self-check workflows. <br>
Mitigation: Minimize or anonymize payroll, employee, tax, cross-border transaction, and business-sensitive details unless the publisher provides an acceptable data-handling and retention policy. <br>
Risk: The client may register and store API credentials, cache state, and write local logs under the user's data directory. <br>
Mitigation: Protect the local configuration and log directory, avoid sharing it, and rotate or remove the stored API key if credentials may have been exposed. <br>
Risk: Setup code can add MCP configuration entries for supported clients when auto-setup is explicitly enabled or setup scripts are run. <br>
Mitigation: Review planned MCP configuration changes first, keep the default dry-run posture when evaluating, and enable write mode only after confirming the endpoint and client configuration. <br>
Risk: Compliance outputs are preliminary guidance and may become outdated or vary by jurisdiction. <br>
Mitigation: Verify material decisions against current official sources and qualified local tax, labor, data protection, or legal professionals before filing, hiring, transferring data, or restructuring. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-global-compliance) <br>
- [企业出海全球合规自检页](https://mcp.aitaxs.top/web/topic_workflow_global_compliance.html) <br>
- [财税合规自检门户](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [财税政策知识库](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [跨境财税架构](https://skillhub.cn/skills/tax-crossborder) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, structured tool results, shell command and MCP configuration snippets, and copied self-check report text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP-backed policy, risk, calculation, and knowledge-list tools; includes local offline reference workflows and a browser-based self-check page.] <br>

## Skill Version(s): <br>
3.15.6 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
