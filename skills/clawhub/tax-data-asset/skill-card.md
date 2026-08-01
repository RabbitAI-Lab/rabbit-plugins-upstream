## Description: <br>
数据资源入表税务专项助手，帮助用户识别税会差异、估值虚高、转让授权涉税、研发加计归集、数据权属合规和上市审核问询风险。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external tax and compliance professionals, and developers use this skill to ask about Chinese tax treatment for data resources entered as assets, run structured self-checks, and produce practical risk guidance before filing, transaction, R&D, valuation, or listing review work. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax positions, IPO review facts, customer data, or business secrets may be transmitted to remote services. <br>
Mitigation: Review the skill before enterprise use and avoid entering confidential information unless transmission to mcp.aitaxs.top and possible fallback search is acceptable. <br>
Risk: Identifiers, API keys, and raw logs may persist locally. <br>
Mitigation: Inspect ~/.tax-policy-client and browser localStorage for stored credentials or identifiers, and clear them according to local policy. <br>
Risk: MCP client configuration may be modified when automatic setup is enabled. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP disabled unless configuration changes are intentional, and review generated MCP settings before relying on them. <br>
Risk: Tax guidance can be incomplete or time-sensitive in regulated contexts. <br>
Mitigation: Verify conclusions against current official policy and qualified professional review before filing, transaction, listing, or dispute use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-data-asset) <br>
- [Data asset tax compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_data_asset.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Related tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional code or shell snippets, configuration instructions, structured self-check results, and generated reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP services and a web self-check page; offline workflows provide checklist-style fallback guidance.] <br>

## Skill Version(s): <br>
3.15.6 (source: server release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
