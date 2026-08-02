## Description: <br>
Tax Crossborder helps agents answer cross-border e-commerce and trade tax compliance questions, run risk self-checks, calculate selected tax scenarios, and draft advisory compliance guidance for China-focused cross-border tax contexts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, finance teams, and tax/compliance teams use this skill to ask cross-border e-commerce and trade tax questions, perform preliminary risk self-checks, and produce advisory checklists or compliance report drafts. It focuses on export refunds, import tax, transfer pricing, foreign income tax credits, withholding tax, beneficial ownership, CRS, VIE/red-chip structures, and related China cross-border scenarios. <br>

### Deployment Geography for Use: <br>
Global use for China-focused cross-border tax scenarios <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, scenarios, and selected self-check metrics may be sent to the publisher's remote service. <br>
Mitigation: Use only approved, non-confidential inputs; avoid taxpayer IDs, bank details, contracts, and personal data unless authorized. <br>
Risk: Service credentials, query logs, and web client keys may be stored locally. <br>
Mitigation: Use trusted machines and periodically clear the local client config/log/cache directories and browser localStorage, especially on shared or managed devices. <br>
Risk: The skill provides advisory tax calculations, risk scores, and report drafts that may be incomplete or time-sensitive. <br>
Mitigation: Validate outputs against current official rules and consult a qualified tax professional before filings, audits, disputes, or material transactions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-crossborder) <br>
- [Cross-border self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_crossborder.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge hub](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown and plain text guidance, with structured tool results when MCP tools are available] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisory tax guidance only; remote service responses and local fallback outputs should be checked against current official rules and professional advice.] <br>

## Skill Version(s): <br>
3.15.7 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
