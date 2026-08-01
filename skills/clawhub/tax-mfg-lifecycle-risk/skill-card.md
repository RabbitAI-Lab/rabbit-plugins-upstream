## Description: <br>
Provides manufacturing lifecycle tax-risk guidance for company setup, operations, R&D deductions, restructuring, expansion, liquidation, and compliance self-checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business users, tax teams, and advisors use this skill to identify China manufacturing tax risks, classify input VAT issues, evaluate restructuring or liquidation scenarios, and produce practical compliance checklists or reports. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, risk scenarios, and web self-check metrics may be sent to mcp.aitaxs.top. <br>
Mitigation: Install only when that remote service use is acceptable for the data being entered; avoid entering confidential taxpayer details unless approved. <br>
Risk: The skill may create local credential, cache, or log files under ~/.tax-policy-client and browser localStorage entries. <br>
Mitigation: Review and remove those local files or storage entries when uninstalling or when operating under stricter data-retention requirements. <br>
Risk: Optional setup can change Claude, Cursor, or Cline MCP configuration when explicitly enabled. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP unset unless those configuration changes are intended, and review any MCP entries during uninstall. <br>
Risk: Tax guidance can become outdated or may not fit a specific filing position. <br>
Mitigation: Verify policy citations, rates, deadlines, and filing actions against official tax authority sources or qualified professionals before relying on the output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-mfg-lifecycle-risk) <br>
- [Manufacturing lifecycle self-check page](https://mcp.aitaxs.top/web/topic_workflow_mfg_lifecycle.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Comprehensive tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance, structured checklists, links, and optional local command or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a remote MCP service for tax questions, risk checks, calculations, and knowledge-base listings; includes offline process guidance when the service is unavailable.] <br>

## Skill Version(s): <br>
3.15.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
