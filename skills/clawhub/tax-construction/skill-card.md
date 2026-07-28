## Description: <br>
为建筑施工企业和顾问提供财税合规问答、风险自查、政策溯源、计算和整改报告指引，覆盖异地预缴、甲供工程、挂靠虚开、四流合一、农民工工资专户、跨地区涉税等施工场景。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external consultants, and developers use this skill to assess construction-industry tax compliance scenarios, generate practical checklists, trace policy basis, and prepare remediation guidance. It is suited to China-focused construction tax workflows such as off-site VAT prepayment, simplified taxation for owner-supplied materials, subcontracting, payroll accounts, invoice remarks, and project-based income recognition. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Questions and workflow data may be processed by the remote mcp.aitaxs.top service. <br>
Mitigation: Use anonymized or aggregated facts and avoid raw payroll, identity, invoice, bank, or full tax-registration data unless retention and handling controls are clarified. <br>
Risk: The package can persist local or browser credentials and logs of tax questions. <br>
Mitigation: Review local configuration, cache, and log storage before use; rotate or revoke API keys and clear local logs when handling sensitive scenarios. <br>
Risk: Fallback public search can introduce outdated or unverified policy information. <br>
Mitigation: Treat fallback results as prompts for further review and verify final conclusions against official tax/legal sources or qualified professionals. <br>
Risk: The user-triggered matrix installer can add other tax skills. <br>
Mitigation: Run installation only from trusted release channels and review the target skill list, package source, and versions before allowing new skills. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-construction) <br>
- [Construction compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_construction.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown or plain text with structured checklists, calculations, links, and optional setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote MCP service, produce local fallback guidance, and suggest related skill installation steps.] <br>

## Skill Version(s): <br>
3.15.3 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
