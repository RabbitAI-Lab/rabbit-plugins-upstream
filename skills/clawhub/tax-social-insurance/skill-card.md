## Description: <br>
社保入税与社保合规指引 helps agents provide structured Chinese guidance for social-insurance tax administration, contribution-base compliance, personal-income-tax/social-insurance matching, flexible-workforce boundaries, audits, remediation, and CPA accounting adjustments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, HR/payroll teams, finance teams, and compliance advisers use this skill to triage Chinese social-insurance compliance questions, run self-check workflows, estimate contribution-base differences and late fees, classify risk, and prepare remediation guidance. It does not replace official agency determinations or licensed representation. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill may use a remote tax-policy service and store local API or client identifiers. <br>
Mitigation: Review the configured endpoint before use, avoid sensitive payroll or business identifiers unless approved, and prefer low-sensitivity test inputs during evaluation. <br>
Risk: The skill can add persistent MCP configuration when setup is explicitly enabled. <br>
Mitigation: Use dry-run or manual setup first, review configuration diffs, and keep backups of existing MCP client configuration. <br>
Risk: The bundled matrix installer can install additional tax skills beyond the advertised social-insurance task. <br>
Mitigation: Run matrix installation only after reviewing the target skill list and source URLs; use selective installation where available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-social-insurance) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Social-insurance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_social_insurance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Remote tax-policy MCP service](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional links, structured checklists, calculations, shell commands, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a remote tax-policy service, local cached identifiers, MCP configuration snippets, and offline fallback workflows.] <br>

## Skill Version(s): <br>
3.15.3 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
