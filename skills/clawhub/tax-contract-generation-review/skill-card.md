## Description: <br>
Supports contract template selection, draft generation, clause review, tax compliance checks, risk prevention guidance, and review report generation for enterprise contract workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Enterprise legal, compliance, finance, and tax teams use this skill to draft contract templates, review contract clauses, identify tax compliance risks, and produce structured contract review reports. It is most relevant to Chinese tax and contract compliance scenarios. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Contract and tax questions, self-check data, or related usage signals may be sent to mcp.aitaxs.top. <br>
Mitigation: Use the skill only after approving remote processing for the data involved; avoid confidential contracts unless that data handling is acceptable. <br>
Risk: API credentials and logs may be stored locally. <br>
Mitigation: Protect local configuration and log directories, rotate or delete credentials when no longer needed, and avoid shared machines for sensitive use. <br>
Risk: Optional setup or install behavior may change MCP client configuration or add related skills. <br>
Mitigation: Review setup actions before enabling them and run with dry-run behavior where available. <br>
Risk: Generated tax and contract guidance may be incomplete or jurisdiction-sensitive. <br>
Mitigation: Treat outputs as review support, verify against current official sources, and consult qualified tax or legal professionals for material decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zxj2devs/skills/tax-contract-generation-review) <br>
- [Publisher Profile](https://clawhub.ai/user/zxj2devs) <br>
- [Contract Compliance Self-Check Web Workflow](https://mcp.aitaxs.top/web/topic_workflow_contract.html) <br>
- [Tax Policy Knowledge Matrix Hub](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown and structured text reports with checklists, risk findings, clause recommendations, and configuration guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include links to a web self-check workflow and locally routed MCP service configuration.] <br>

## Skill Version(s): <br>
3.14.38 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
