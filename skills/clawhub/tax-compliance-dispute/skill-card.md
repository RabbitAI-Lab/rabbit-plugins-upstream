## Description: <br>
Tax Compliance Dispute helps agents provide China-focused tax compliance and dispute guidance, including internal-control checks, liquidation tax issues, audit response, invoice-risk screening, contract tax clause review, and self-check report drafting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business users, tax staff, compliance teams, and their agents use this skill to triage China tax compliance questions, plan dispute-response steps, run structured self-checks, and draft practical remediation or reporting guidance. It is most useful for tax audits, administrative review or litigation pathways, company liquidation and deregistration, invoice compliance, and contract-related tax risk review. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax questions, risk scenarios, and self-check metrics may be sent to mcp.aitaxs.top. <br>
Mitigation: Use the skill only when that data transfer is acceptable; avoid submitting unnecessary confidential taxpayer, personal, or business-sensitive details. <br>
Risk: The skill can store API keys, persistent client identifiers, and plaintext logs under the user's home directory. <br>
Mitigation: Review and manage the local data directory after use, rotate or remove credentials when no longer needed, and avoid shared machines for sensitive tax work. <br>
Risk: Optional auto-setup can modify local MCP client settings when explicitly enabled. <br>
Mitigation: Leave TAX_ENABLE_AUTOSETUP disabled unless configuration changes are intentional, and review any MCP settings or backups before continuing. <br>
Risk: Tax and dispute guidance can be time-sensitive and jurisdiction-specific. <br>
Mitigation: Confirm high-impact conclusions with current official guidance, the competent tax authority, or qualified tax and legal professionals before acting. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zxj2devs/skills/tax-compliance-dispute) <br>
- [Interactive Tax Compliance Dispute Self-Check](https://mcp.aitaxs.top/web/topic_workflow_dispute.html) <br>
- [Tax Compliance Self-Check Portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text guidance, structured self-check results, generated reports, optional code snippets, and optional MCP configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route tax questions and self-check metrics to a cloud MCP service, with offline fallback guidance for limited local reference.] <br>

## Skill Version(s): <br>
3.15.7 (source: evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
