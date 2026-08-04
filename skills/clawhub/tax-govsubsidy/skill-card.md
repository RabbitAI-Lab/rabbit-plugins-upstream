## Description: <br>
Provides government-subsidy and fiscal-fund tax compliance guidance for Chinese tax scenarios, including non-taxable income classification, dedicated-account controls, expense treatment, five-year tracking, VAT input-tax handling, risk scans, and self-check report workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business users and tax/compliance practitioners use this skill to assess Chinese government subsidy and fiscal-fund tax treatment, generate structured self-checks, identify common compliance risks, and prepare remediation-oriented guidance or reports. It is not a substitute for official tax authority determinations or licensed professional services. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax and compliance prompts may be forwarded to mcp.aitaxs.top for remote MCP processing. <br>
Mitigation: Use only when the publisher's data handling and retention terms are acceptable; avoid entering confidential business details unless approved for that remote service. <br>
Risk: Fallback behavior can send searches to public search engines when the remote service is unavailable. <br>
Mitigation: Remove sensitive identifiers and confidential facts before relying on fallback searches; treat fallback answers as preliminary references. <br>
Risk: The client may store an API key, cache data, health state, and logs under ~/.tax-policy-client. <br>
Mitigation: Protect that local directory, review or clear stored logs and credentials according to local security policy, and rotate credentials if exposure is suspected. <br>
Risk: Optional MCP setup can modify client configuration files when explicitly enabled. <br>
Mitigation: Run setup only after reviewing the target client configuration; rely on the built-in backup behavior and confirm the added MCP server entry before use. <br>
Risk: Generated tax guidance, risk scores, and reports may be incomplete, outdated, or inappropriate for a specific taxpayer's facts. <br>
Mitigation: Validate conclusions against official tax authority guidance and qualified professional review before filing, accounting, or remediation decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-govsubsidy) <br>
- [Government subsidy self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_govsubsidy.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge MCP endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>
- [Comprehensive tax knowledge companion skill](https://skillhub.cn/skills/user_11064e10/tax-policy-knowledge) <br>
- [High-tech and R&D deduction companion skill](https://skillhub.cn/skills/user_11064e10/tax-high-tech-deduction) <br>
- [Tax incentives companion skill](https://skillhub.cn/skills/user_11064e10/tax-incentives) <br>
- [Green and energy-saving tax companion skill](https://skillhub.cn/skills/user_11064e10/tax-renewable) <br>
- [Environmental tax and carbon companion skill](https://skillhub.cn/skills/user_11064e10/tax-environmental) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, structured text, JSON-like tool responses, HTML workflow output, and Python command-line output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote MCP tools, produce local offline fallback guidance, generate checklist-style compliance outputs, and suggest client MCP configuration only when setup is explicitly run.] <br>

## Skill Version(s): <br>
3.15.10 (source: frontmatter and server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
