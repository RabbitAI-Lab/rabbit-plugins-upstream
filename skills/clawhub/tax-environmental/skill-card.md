## Description: <br>
Environmental tax and carbon compliance assistant focused on taxable pollutant identification, monitoring and calculation, emission-reduction relief checks, quarterly filing, carbon quota settlement, CCER/VAT treatment, carbon data quality, and remediation workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external advisors, and business compliance teams use this skill to self-check China-oriented environmental tax and carbon compliance questions, estimate filing and relief issues, track carbon quota obligations, and produce structured remediation guidance. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Prompts or business facts may be sent to cloud services or search engines during online policy, risk, or calculation flows. <br>
Mitigation: Use only with clear consent, redact confidential tax, emissions, and business data, and prefer offline fallback guidance for sensitive scenarios. <br>
Risk: Installation or use may create persistent local files, logs, and API keys. <br>
Mitigation: Review local storage locations before deployment, restrict file permissions, and rotate or remove locally stored keys and logs when no longer needed. <br>
Risk: Optional auto-setup can modify AI-client MCP configuration. <br>
Mitigation: Keep setup in dry-run mode by default and require manual review before enabling configuration writes. <br>
Risk: The bundled client connects to a broader tax backend rather than a strictly environmental/carbon-only tool surface. <br>
Mitigation: Scope use to environmental tax and carbon compliance tasks and require professional review before relying on outputs for filings or regulated decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-environmental) <br>
- [Environmental tax and carbon compliance interactive workflow](https://mcp.aitaxs.top/web/topic_workflow_environmental.html) <br>
- [Tax compliance topic portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration, Shell commands] <br>
**Output Format:** [Markdown guidance with structured checklists, calculations, risk summaries, copied prompts, and optional configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include links to an interactive self-check page and offline fallback guidance when cloud tools are unavailable.] <br>

## Skill Version(s): <br>
3.15.8 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
