## Description:

浙江供应商双证据核验，按企业名交叉核验资质（科技型中小企业名录）与业绩（工程中标记录）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users use this skill to check a Zhejiang supplier by company name, combining technology-SME roster status with public-works contract award history. It supports supplier qualification review, shortlist screening, competitor research, and supplier due diligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplier names and product credentials or session identifiers are sent to the skill's service endpoint.

Mitigation: Install and use the skill only when that data sharing is acceptable for the supplier review workflow.

Risk: Product credentials and cookies are stored locally in ~/.odf/combo-supplier-profile.json.

Mitigation: Protect the local credential file and remove it when access should be revoked on a shared or retired machine.

Risk: Returned supplier records are service data and may be incomplete or historical rather than real-time.

Mitigation: Treat the report as supporting evidence and verify important decisions with authoritative supplier identifiers and current source records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/zj-supplier-profile)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Plain text supplier-check report returned by a Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports roster match status, public-works award counts, amount bands or ranges, evidence combination status, freshness, and recommended next actions.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter, manifest.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
