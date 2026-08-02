## Description: <br>
Provides structured tax compliance guidance for recognizing data resources as assets, managing book-tax differences, transfer and licensing tax treatment, R&D deduction tracking, ownership compliance, valuation risk, and listing-review preparation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business tax teams use this skill to triage data-asset tax questions, run structured compliance self-checks, and prepare practical follow-up checklists for Chinese tax and listing-review scenarios. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, scenarios, and calculator inputs may be sent to an external cloud service. <br>
Mitigation: Avoid entering confidential company, pre-IPO, personal, or financial details unless that data flow is approved for the deployment. <br>
Risk: The package may use persistent identifiers, API keys, local logs, and public-search fallback. <br>
Mitigation: Review deployment settings and logs before business or regulated use, and limit use to approved data and network paths. <br>
Risk: Optional setup can edit local MCP client configuration. <br>
Mitigation: Do not run config/init_agent.py or enable TAX_ENABLE_AUTOSETUP unless the user intentionally wants local MCP client configuration changed. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/zxj2devs/skills/tax-data-asset) <br>
- [Data asset tax compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_data_asset.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown and structured text checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include links to a web self-check workflow and MCP configuration guidance.] <br>

## Skill Version(s): <br>
3.15.7 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
