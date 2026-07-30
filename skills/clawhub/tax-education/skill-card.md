## Description: <br>
Provides education-sector tax compliance guidance for VAT exemptions and simplified calculation, nonprofit school tax qualification, tuition revenue recognition, teacher payroll tax and social insurance, invoice compliance, risk self-checks, case analysis, and compliance reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax professionals, and education or training organizations use this skill to ask education-sector tax questions, run lightweight compliance self-checks, and produce practical checklists or report-style guidance for risk review. It is advisory support and does not replace tax filing, legal representation, or professional review. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Remote processing by mcp.aitaxs.top may receive tax questions, scenarios, calculation parameters, and related identifiers. <br>
Mitigation: Review the remote data flow before deployment and avoid entering confidential tax, payroll, invoice, or client identifiers unless that processing is approved. <br>
Risk: The skill stores local API keys, identifiers, cache, health state, and logs, and the browser workflow stores credentials in localStorage. <br>
Mitigation: Restrict local profile access, review and rotate stored credentials, and clear local or browser storage after sensitive testing. <br>
Risk: Optional setup can modify AI client MCP configuration when explicitly enabled. <br>
Mitigation: Run setup in dry-run mode first, inspect generated MCP configuration changes, and keep backups before enabling automatic configuration. <br>
Risk: Tax policy output can be incomplete, stale, or not tailored to a specific filing position. <br>
Mitigation: Treat generated answers and calculations as review aids, verify current official sources and local practice, and consult qualified tax or legal professionals for material decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zxj2devs/skills/tax-education) <br>
- [Education Compliance Self-Check Web Workflow](https://mcp.aitaxs.top/web/topic_workflow_education.html) <br>
- [Tax Compliance Self-Check Portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, shell commands, guidance] <br>
**Output Format:** [Markdown, JSON-like tool results, and plain text guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote MCP tools for policy Q&A, risk checks, tax calculation, and knowledge-base listings; local fallback guidance is available when the remote service is unavailable.] <br>

## Skill Version(s): <br>
3.15.4 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
