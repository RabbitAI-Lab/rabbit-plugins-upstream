## Description:

Checks whether a Zhejiang supplier appears in the collected technology-SME roster and historical engineering contract awards, then provides a combined assessment and suggested next steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and supplier-review teams use this skill to check a Zhejiang company against a collected technology-SME roster and historical engineering award records before supplier screening or due diligence.

### Deployment Geography for Use:

Global (data coverage: Zhejiang Province, China)

## Known Risks and Mitigations:

Risk: Company queries are sent to a remote service, and product credentials and session cookies are stored locally in plaintext.

Mitigation: Use only if remote processing is acceptable; keep unrelated secrets out of the credential file and remove it when no longer needed.

Risk: A missing roster or award record may reflect incomplete or historical coverage rather than absence of qualifications or contracts.

Mitigation: Treat unmatched records as inconclusive and corroborate important decisions with current official records and the company's unified social credit code.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chenqg618/skills/zj-supplier-profile)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Four-category assessment with roster and award evidence, amount bands, and suggested actions; records are historical and collection is incomplete.]

## Skill Version(s):

1.0.4 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
