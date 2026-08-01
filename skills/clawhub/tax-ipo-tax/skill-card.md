## Description: <br>
Provides structured IPO tax compliance guidance and self-check workflows for tax incentive reliance, disclosure, red-chip tax clearance, and listing-review risk response. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External finance, tax, legal, and listing project teams use this skill to structure IPO tax compliance self-checks, identify common review risks, and prepare practical remediation or disclosure guidance. It is intended as decision support and does not replace licensed tax, audit, legal, or regulatory advice. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Cloud-backed tax processing can send IPO, restructuring, shareholder, filing, or other sensitive tax details outside the local environment. <br>
Mitigation: Use only with approved data handling terms; avoid confidential or identifying details unless remote processing has been reviewed and accepted. <br>
Risk: The package stores persistent local credentials, cache, and logs for the tax policy client. <br>
Mitigation: Review local storage behavior before deployment and clear credentials, cache, or logs according to the organization's retention and privacy requirements. <br>
Risk: Optional auto-setup can modify MCP client configuration when explicitly enabled or when initialization scripts are run for that purpose. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP disabled unless configuration changes are intended; review generated configuration and backups before use. <br>
Risk: Tax guidance and listing-review practices can be jurisdiction-specific and may change over time. <br>
Mitigation: Treat outputs as support material, verify against official regulator and tax authority sources, and involve qualified professionals for filings, disclosures, and assurance work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-ipo-tax) <br>
- [IPO tax compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_ipo_tax.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, structured checklists, copied report text, JSON-like tool results, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route requests through a cloud-backed tax policy MCP service and also includes offline reference workflows.] <br>

## Skill Version(s): <br>
3.15.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
