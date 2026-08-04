## Description: <br>
A tax compliance assistant for data-resource capitalization scenarios, covering accounting-tax differences, valuation risk, data-product transfers and licensing, R&D deduction classification, data ownership compliance, and listing-review preparation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax professionals, compliance teams, and developers use this skill to answer data-asset tax questions, run structured compliance self-checks, and generate practical remediation guidance for data-resource capitalization workflows. <br>

### Deployment Geography for Use: <br>
Global (content focuses on China tax compliance scenarios) <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, self-check metrics, or tool inputs may be sent to mcp.aitaxs.top. <br>
Mitigation: Avoid entering confidential taxpayer, customer, transaction, or filing details until the organization has approved that data flow and reviewed the service retention and privacy terms. <br>
Risk: The skill stores a service API key under the user's home directory. <br>
Mitigation: Review local credential storage before deployment, restrict local file access as appropriate, and remove or rotate the key when the skill is decommissioned. <br>
Risk: Setup scripts can configure local MCP clients when auto-setup is enabled or scripts are run directly. <br>
Mitigation: Keep auto-setup disabled unless needed, review client configuration changes before enabling it, and rely on the artifact's backup behavior when changes are approved. <br>
Risk: Tax conclusions, rates, and filing positions can be time-sensitive and jurisdiction-specific. <br>
Mitigation: Verify material conclusions against current official policy sources and qualified professional review before filing, transaction execution, or listing-review response. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/zxj2devs/skills/tax-data-asset) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Data-resource tax compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_data_asset.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Related comprehensive tax knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured text responses, with optional MCP tool results, local workflow output, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a cloud-backed MCP service for current tax answers and local offline workflows for limited fallback guidance.] <br>

## Skill Version(s): <br>
3.15.10 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
