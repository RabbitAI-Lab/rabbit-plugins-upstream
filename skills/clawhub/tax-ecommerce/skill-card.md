## Description: <br>
Tax Ecommerce helps users assess China domestic e-commerce and livestreaming tax compliance scenarios, including platform reporting, revenue recognition, invoice risk, private-account collections, case analysis, report templates, and practical remediation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax practitioners, and business operators use this skill to ask e-commerce and livestreaming tax questions, run compliance self-checks, identify risk indicators, and draft practical remediation or reporting guidance. The skill is focused on China tax compliance content and should not be treated as legal, audit, or filing advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax questions, scenarios, and self-check metrics may be sent to mcp.aitaxs.top, with possible fallback searches to Bing or Baidu. <br>
Mitigation: Review the skill before installing, confirm outbound network use is acceptable, and avoid entering client names, tax IDs, bank details, or other sensitive identifiers. <br>
Risk: The security summary reports local storage of API credentials and logs with incomplete disclosure. <br>
Mitigation: Use a restricted local profile where possible, review stored credentials and logs periodically, and remove them when the skill is no longer needed. <br>
Risk: The security verdict is suspicious due to cloud data handling and local credential/log behavior. <br>
Mitigation: Deploy only after a privacy and data-retention review, and limit use to scenarios where the publisher's controls are acceptable. <br>
Risk: The skill provides tax compliance guidance that may be time-sensitive or jurisdiction-specific. <br>
Mitigation: Confirm material conclusions against official tax authorities or qualified tax professionals before filing, payment, audit, or dispute actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-ecommerce) <br>
- [E-commerce tax self-check page](https://mcp.aitaxs.top/web/topic_workflow_ecommerce.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown text with optional JSON/tool results, Python snippets, shell commands, configuration examples, and web self-check links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce tax compliance analysis, risk self-check summaries, tax calculation guidance, report outlines, and client configuration instructions.] <br>

## Skill Version(s): <br>
3.15.8 (source: SKILL.md frontmatter, ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
