## Description: <br>
Helps domestic ecommerce sellers, livestream commerce teams, MCNs, creators, and platform operators self-check China tax-compliance risks and prepare practical remediation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business, finance, tax, and compliance users use this skill to ask ecommerce and livestream tax questions, run structured risk self-checks, and generate remediation-oriented checklists or reports for China-focused operations. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax scenarios may be sent to mcp.aitaxs.top for policy questions, risk checks, tax calculations, and self-check workflows. <br>
Mitigation: Use sanitized scenarios and avoid taxpayer identifiers, private account details, invoices, receipts, or confidential business facts unless the user accepts that remote processing. <br>
Risk: The client can store local identifiers, API keys, health cache, and raw query log entries under ~/.tax-policy-client, and the web workflow may use browser storage. <br>
Mitigation: Review or clear ~/.tax-policy-client and relevant browser localStorage after use, especially on shared machines or when testing sensitive scenarios. <br>
Risk: Tax outputs are decision-support guidance and may be incomplete, stale, or unsuitable for a specific taxpayer's facts. <br>
Mitigation: Confirm material filing, dispute, audit, and remediation decisions with official tax sources or a qualified tax professional before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-ecommerce) <br>
- [Ecommerce and livestream compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_ecommerce.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with structured JSON-style results and copyable report text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include policy references, risk levels, remediation checklists, self-check summaries, and report-ready text.] <br>

## Skill Version(s): <br>
3.15.6 (source: evidence.release.version, SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
