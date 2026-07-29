## Description: <br>
Tax Equity Governance provides Chinese-language tax guidance, calculations, structure comparisons, and risk warnings for equity transfers, family ownership structures, state-owned enterprise mixed-ownership reform, VIE/red-chip structures, and equity-governance tax compliance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external tax advisors, and individual users can use this skill to ask Chinese equity-tax questions, run preliminary risk checks, compare ownership structures, and prepare self-check or remediation guidance before confirming final positions with tax authorities or licensed professionals. <br>

### Deployment Geography for Use: <br>
Global availability; China-focused tax and equity-governance content. <br>

## Known Risks and Mitigations: <br>
Risk: Confidential enterprise tax facts may be sent to the remote MCP service or to public-search fallback paths. <br>
Mitigation: Use redacted or minimum necessary facts, avoid sensitive identifiers, and install only if remote processing is acceptable for the intended tax workflow. <br>
Risk: Optional setup paths can modify MCP client configuration when setup helpers are run or TAX_ENABLE_AUTOSETUP is enabled. <br>
Mitigation: Keep auto setup disabled unless configuration changes are intended, review target client configuration first, and retain backups before enabling setup. <br>
Risk: Credential persistence is present for service access. <br>
Mitigation: Use the skill only in trusted environments and review, rotate, or remove stored credentials when access is no longer needed. <br>
Risk: Tax guidance can be jurisdiction-specific, time-sensitive, or unsuitable as final professional advice. <br>
Mitigation: Confirm material transactions with current official sources, the competent tax authority, or a licensed tax professional before filing or executing a transaction. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-equity-governance) <br>
- [Equity governance self-check page](https://mcp.aitaxs.top/web/topic_workflow_equity_governance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text responses, JSON-RPC tool results, Python helper output, and web self-check output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a remote MCP service, local offline workflow guidance, or a web self-check link depending on client configuration and service availability.] <br>

## Skill Version(s): <br>
3.15.4 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
