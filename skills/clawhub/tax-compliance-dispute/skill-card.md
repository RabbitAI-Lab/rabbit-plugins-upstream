## Description: <br>
Provides Chinese-language tax compliance and dispute guidance for internal controls, liquidation and deregistration, tax audits, administrative remedies, contract tax clauses, invoice compliance, and tax-related criminal risk self-checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and tax, finance, legal, and compliance teams use this skill to triage Chinese tax compliance issues, prepare dispute-response paths, run structured self-checks, and generate practical remediation guidance. It is advisory support and should be reviewed against current rules and professional judgment before relying on it for high-stakes tax decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions or scenarios may be sent to a cloud-backed tax knowledge service. <br>
Mitigation: Avoid entering confidential taxpayer, client, or transaction data unless the cloud data handling is acceptable for the use case. <br>
Risk: The package may store local API credentials, cache data, and logs. <br>
Mitigation: Review local credential and log storage before use, and remove stored data when it is no longer needed. <br>
Risk: The package includes agent configuration and auto-setup behavior. <br>
Mitigation: Run setup in dry-run or review mode first, and disable auto-setup unless the intended MCP configuration changes are understood. <br>
Risk: The package includes tooling to install related skills into a user skill directory. <br>
Mitigation: Prefer explicit installation of selected related skills instead of one-click matrix installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-compliance-dispute) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Tax compliance workflow page](https://mcp.aitaxs.top/web/topic_workflow_dispute.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands, configuration] <br>
**Output Format:** [Markdown text with structured checklists, risk assessments, remediation steps, links, and occasional command or configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route questions to a cloud-backed MCP tax knowledge service and may use local offline workflow scripts for limited fallback guidance.] <br>

## Skill Version(s): <br>
3.15.3 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
