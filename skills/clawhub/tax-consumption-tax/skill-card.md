## Description: <br>
Provides battery consumption tax guidance for rate timelines, exemption eligibility, CMA report checks, entrusted processing deductions, self-use scenarios, and compliance self-checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, finance, and compliance users use this skill to ask battery consumption tax questions, check exemption prerequisites, identify filing risks, and prepare practical self-check or remediation guidance. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions or self-check metrics may be sent to a cloud-backed service and local logs or configuration may be retained. <br>
Mitigation: Review the data flow and retention expectations before use, and redact tax IDs, customer lists, financial details, and non-redacted business identifiers. <br>
Risk: The skill may register an API key or change client MCP configuration during optional setup. <br>
Mitigation: Install in a controlled client profile, review generated MCP configuration before enabling automatic setup, and remove stored credentials if the skill is no longer trusted. <br>
Risk: Tax guidance can be incomplete, stale, or misapplied to a specific filing position. <br>
Mitigation: Verify material conclusions against official tax authority sources and qualified professional review before filing, claiming exemptions, or relying on deductions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-consumption-tax) <br>
- [Battery consumption tax self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_consumption_tax.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, JSON tool results, MCP tool content, local console text, and HTML self-check workflow output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces tax guidance, risk findings, checklists, calculation-oriented outputs, and report-style summaries.] <br>

## Skill Version(s): <br>
3.15.7 (source: frontmatter and server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
