## Description: <br>
tax-mfg-lifecycle-risk helps manufacturing organizations assess tax risk across formation, operations, restructuring, expansion, and liquidation, producing compliance self-checks, policy-oriented guidance, risk scans, calculations, and remediation checklists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business users, tax and compliance teams, and advisors use this skill to triage manufacturing lifecycle tax scenarios, ask policy questions, run self-check or risk-scan workflows, and prepare structured compliance or remediation outputs before professional review. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive company tax scenarios may be sent to a shared remote tax-policy service. <br>
Mitigation: Use redacted or representative scenarios unless the user has reviewed and accepted the service's data handling and retention practices. <br>
Risk: The skill can store credentials and logs under the user's home directory. <br>
Mitigation: Install only in trusted environments, inspect local client data directories, and rotate or remove stored credentials and logs when access is no longer needed. <br>
Risk: MCP client settings may be modified if automatic setup is explicitly enabled. <br>
Mitigation: Keep setup in dry-run mode until configuration changes are reviewed, and rely on the built-in backup behavior before enabling writes. <br>
Risk: Tax guidance, calculations, and risk scans may be incomplete or outdated for a specific filing or transaction. <br>
Mitigation: Verify outputs against current official sources and obtain qualified professional review before filing, restructuring, liquidation, or other consequential tax actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-mfg-lifecycle-risk) <br>
- [Manufacturing lifecycle tax self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_mfg_lifecycle.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge companion skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown conversational answers, structured checklists and reports, JSON-style MCP/tool responses, Python scripts, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote tax-policy MCP service; offline scripts provide local process guidance and keyword checks when service access is unavailable.] <br>

## Skill Version(s): <br>
3.15.10 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
