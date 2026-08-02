## Description: <br>
Tax Transfer Pricing is a China-focused transfer-pricing compliance assistant for related-party transaction review, contemporaneous documentation, pricing-method selection, thin-capitalization checks, APA preparation, CFC considerations, and structured risk remediation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, finance, and compliance users with related-party transactions use this skill to ask transfer-pricing questions, generate documentation checklists, run self-checks, and prepare remediation-oriented compliance reports. Its guidance should be reviewed against current Chinese tax rules and the user's facts before operational use. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Cloud-backed tax-policy calls can expose submitted questions or tax indicators to the provider. <br>
Mitigation: Do not enter taxpayer identifiers, confidential financial statements, trade secrets, or sensitive company details unless the provider's privacy and retention practices have been reviewed and approved. <br>
Risk: The client may create local persistent identifiers, API keys, and logs of tax questions. <br>
Mitigation: Review local storage and log locations before installation and periodically remove stored identifiers, API keys, and logs when no longer needed. <br>
Risk: Optional MCP auto-setup can modify supported client configuration files. <br>
Mitigation: Keep setup in dry-run mode unless configuration changes are intended, and review generated MCP entries and backups before enabling the service. <br>
Risk: Transfer-pricing and tax-compliance guidance may be incomplete, outdated, or unsuitable for a specific taxpayer's facts. <br>
Mitigation: Validate outputs against current authoritative tax rules and qualified professional advice before filing, negotiating an APA, or responding to a tax authority. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-transfer-pricing) <br>
- [zxj2devs publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Transfer-pricing self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_transfer_pricing.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown guidance with structured checklists, risk summaries, and optional configuration or command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a cloud-backed tax-policy MCP service or local fallback workflows; generated tax guidance requires review before reliance.] <br>

## Skill Version(s): <br>
3.15.7 (source: evidence release version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
