## Description: <br>
Provides transfer-pricing and contemporaneous documentation compliance guidance for related-party transactions, including method selection, self-checks, risk scanning, APA preparation, thin capitalization, intangible assets, and CFC topics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and tax practitioners use this skill to structure transfer-pricing self-checks, prepare contemporaneous documentation checklists, scan related-party transaction risks, and draft practical compliance next steps. It is suited to China tax transfer-pricing workflows where users still need professional review for final filing, audit, and tax authority outcomes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Confidential tax, financing, audit strategy, or related-party transaction details may be sent to a cloud MCP service. <br>
Mitigation: Review the skill before installation, avoid entering highly sensitive facts unless the service is approved for that data, and sanitize prompts where possible. <br>
Risk: When the remote service is unavailable, the client may use public search fallback for tax questions. <br>
Mitigation: Treat fallback answers as preliminary public-source guidance and confirm material tax conclusions with authoritative sources or a qualified professional. <br>
Risk: The client can persist local configuration, credentials, cache, health state, and logs under ~/.tax-policy-client. <br>
Mitigation: Inspect and protect that directory, remove stored credentials when uninstalling, and avoid shared-machine use without appropriate account controls. <br>
Risk: MCP client configuration files may be modified if setup is run or TAX_ENABLE_AUTOSETUP is enabled. <br>
Mitigation: Run setup in dry-run mode first, review proposed MCP configuration changes, and keep backups of existing client config files. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zxj2devs/skills/tax-transfer-pricing) <br>
- [Publisher Profile](https://clawhub.ai/user/zxj2devs) <br>
- [Transfer Pricing Interactive Workflow](https://mcp.aitaxs.top/web/topic_workflow_transfer_pricing.html) <br>
- [Tax Compliance Self-Check Portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and structured text, with optional local Python workflow output and web workflow links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a cloud MCP service, fall back to public web search, or provide offline checklist-style guidance depending on connectivity and setup.] <br>

## Skill Version(s): <br>
3.15.10 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
