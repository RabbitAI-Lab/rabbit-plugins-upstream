## Description: <br>
办税合规智能指引 helps users navigate China electronic tax bureau workflows, tax filings, invoice handling, tax deregistration, tax credit repair, filing calendars, forms, and frequent compliance questions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Enterprise tax staff, finance teams, and individual taxpayers use this skill for scenario-based guidance on China tax filing workflows, required materials, electronic tax bureau paths, common filing errors, and compliance reminders. It provides operational guidance and checklists, not taxpayer representation or a guarantee of tax authority outcomes. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and scenarios may be processed by the remote mcp.aitaxs.top service. <br>
Mitigation: Use the skill only if that remote processing is acceptable, and avoid entering taxpayer IDs, bank details, invoice numbers, or confidential business facts unless the service and its retention practices are trusted. <br>
Risk: The skill stores local credentials, cache, and logs under ~/.tax-policy-client. <br>
Mitigation: Protect that local directory as sensitive application data and review or remove stored configuration, cache, and logs when the skill is no longer needed. <br>
Risk: The optional matrix installer can modify the user's skills directory and install additional tax-related skills. <br>
Mitigation: Review the matrix package list and source integrity controls before using the full installer, and prefer dry-run or targeted installation when broad changes are not needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/china-tax-guidance) <br>
- [财税合规自检门户](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge MCP service](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>
- [综合财税知识库](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [数电票合规](https://skillhub.cn/skills/tax-invoice-compliance) <br>
- [增值税法落地](https://skillhub.cn/skills/tax-vat-law) <br>
- [涉税司法案例](https://skillhub.cn/skills/tax-tax-judicial) <br>
- [社保入税合规](https://skillhub.cn/skills/tax-social-insurance) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown or text guidance with structured checklists and optional installation or configuration actions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Cloud-backed MCP responses may be used when available; local fallback workflows and an optional matrix installer can produce offline guidance or modify the user's skills directory.] <br>

## Skill Version(s): <br>
3.15.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
