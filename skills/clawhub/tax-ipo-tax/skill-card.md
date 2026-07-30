## Description: <br>
An IPO tax-compliance assistant focused on Chinese listing-review tax issues, including tax incentive dependency, disclosure requirements, red-chip tax documentation, exchange review concerns, and structured self-check workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, finance teams, tax advisers, and listing-preparation teams use this skill to ask IPO tax-compliance questions, run lightweight risk self-checks, and generate structured guidance for remediation planning. It is most relevant to tax incentive sustainability, disclosure, red-chip tax clearance, R&D super-deduction evidence, and listing-review response preparation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User questions and risk scenarios may be sent to a remote tax-policy service and may be logged locally. <br>
Mitigation: Avoid entering confidential IPO, cap-table, restructuring, or tax-diligence facts unless that data flow is acceptable; review and clear local ~/.tax-policy-client logs and configuration as needed. <br>
Risk: The skill stores credentials and client configuration locally. <br>
Mitigation: Inspect local configuration before deployment, protect stored API keys, and remove unused credentials after testing or when rotating access. <br>
Risk: Client configuration behavior may modify MCP client settings when autosetup is enabled. <br>
Mitigation: Leave TAX_ENABLE_AUTOSETUP disabled unless configuration changes are intended, and review generated MCP client entries before use. <br>
Risk: Tax-compliance guidance can be incorrect, outdated, or unsuitable for a specific filing or listing-review matter. <br>
Mitigation: Have qualified tax, legal, or listing advisers verify outputs against current official rules and case-specific evidence before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-ipo-tax) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Interactive IPO tax workflow](https://mcp.aitaxs.top/web/topic_workflow_ipo_tax.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance, structured checklists, risk summaries, configuration snippets, and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote tax-policy MCP service when online; includes offline reference workflows for limited local checks.] <br>

## Skill Version(s): <br>
3.15.4 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
