## Description: <br>
Provides a paid enterprise due-diligence report that queries company registry details and public risk signals, including business abnormality, enforcement, dishonest enforcement, and consumption-restriction records, then returns a concise Markdown report with a risk-light summary. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill for paid pre-cooperation checks, supplier or customer risk screening, and quick review of public Chinese enterprise registry and enforcement-risk signals. It is intended for reference reports, not credit reports, legal opinions, or final business-decision advice. <br>

### Deployment Geography for Use: <br>
Global deployment; China-focused enterprise registry and public-risk data coverage. <br>

## Known Risks and Mitigations: <br>
Risk: Reports may display legal, registry, shareholder, address, certificate, or identity-linked fields that can be sensitive in business workflows. <br>
Mitigation: Restrict report access, avoid unnecessary retention, mask identifiers when sharing, and follow the release security guidance before storing or displaying results. <br>
Risk: Public risk records may be delayed, incomplete, or limited to the first returned page, which can lead users to over-read the report. <br>
Mitigation: Keep the partial-record and reference-only disclaimers, show total-versus-displayed counts, and direct users to official public channels for complete and current records. <br>
Risk: The report could be mistaken for a credit report, legal opinion, or final cooperation recommendation. <br>
Mitigation: Present only factual summaries and risk-light signals, avoid deterministic cooperation advice, and preserve the non-legal-opinion disclaimer. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-enterprise-dd-pro-a2a) <br>
- [Artifact README](artifact/README.md) <br>
- [Output format](artifact/OUT_FORMAT.md) <br>
- [Product scope](artifact/PRODUCT.md) <br>
- [Business registry fields](artifact/docs/工商主体信息.md) <br>
- [Business abnormality fields](artifact/docs/企业经营异常信息.md) <br>
- [Enforcement fields](artifact/docs/企业被执行人信息.md) <br>
- [Dishonest enforcement fields](artifact/docs/企业失信被执行人信息.md) <br>
- [Consumption restriction fields](artifact/docs/企业限制高消费.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with structured tables, factual risk-summary bullets, and user-facing disclaimers.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses one enterprise name, registration number, or unified social credit code as the query keyword; risk modules show recent-page records with documented row limits and should not be presented as complete historical lists.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
