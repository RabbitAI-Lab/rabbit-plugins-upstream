## Description: <br>
财税中介机构AI合规咨询服务转型专题（供给侧·B视角）。覆盖涉税专业服务执业规范、三级复核与质量控制、咨询项目承接/交付SOP、税务服务合同与收费、数据安全与执业风险分级、AI数智化执业落地、IMA对标人才培养，配套机构专属模板与工具，与「企业合规指引」（需求侧·A视角）配套。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tax advisory firms, tax agent practices, bookkeeping agencies, and accounting-firm tax teams use this skill to ask institution-side compliance questions, generate tax service templates, run practice risk self-checks, and structure AI-assisted tax consulting delivery with review and quality-control steps. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax and compliance inputs may be sent to mcp.aitaxs.top, and fallback paths may use search engines. <br>
Mitigation: Avoid entering confidential client data, taxpayer identifiers, privileged business details, or other sensitive information unless the service's data-handling terms have been reviewed and accepted. <br>
Risk: The package includes client configuration behavior and remote MCP setup paths that may affect local agent configuration. <br>
Mitigation: Review or disable auto-setup behavior before running configuration scripts, and inspect any generated client configuration before using the service. <br>
Risk: Local API keys, cache files, and logs are treated as sensitive because they may relate to service access and user activity. <br>
Mitigation: Protect the local data directory, avoid sharing logs, rotate or remove stored credentials when no longer needed, and follow the publisher's guidance for credential handling. <br>
Risk: Generated tax guidance, templates, and risk checks may be incomplete or stale for a specific client matter. <br>
Mitigation: Have qualified tax professionals verify policy currency, client facts, calculations, and required review or signing steps before relying on outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-advisory-practice) <br>
- [Interactive advisory self-check page](https://mcp.aitaxs.top/web/topic_workflow_advisory.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Remote MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured text responses, with optional JSON tool results, configuration snippets, generated templates, reports, and local shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include tax policy answers, risk assessments, tax calculations, compliance self-check reports, service-contract templates, checklist guidance, MCP configuration, and offline fallback summaries.] <br>

## Skill Version(s): <br>
3.15.6 (source: frontmatter and server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
