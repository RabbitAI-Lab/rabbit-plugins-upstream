## Description:

Looks up Zhejiang enterprise registration information by company name or unified social credit code, including registration status, industry, and coverage notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, bidders, and other users can check Zhejiang enterprise registration details for supplier screening, pre-bid checks, and preliminary due diligence.

### Deployment Geography for Use:

Global (registry coverage limited to Zhejiang Province, China)

## Known Risks and Mitigations:

Risk: Enterprise names or credit codes are sent to a third-party service for lookup.

Mitigation: Use only when sharing those identifiers with the service is acceptable.

Risk: Product API and session data are stored locally for access.

Mitigation: Review or delete ~/.odf/zj-enterprise-registry.json when the saved access state is no longer needed.

Risk: Incomplete index coverage can cause a lookup to miss an existing enterprise.

Mitigation: Check the reported coverage and data cutoff, and do not treat a missing result as proof of nonexistence.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chenqg618/skills/zj-enterprise-registry)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes coverage and data-cutoff notes; an unmatched query does not establish that an enterprise does not exist.]

## Skill Version(s):

1.0.4 (source: frontmatter, manifest.json, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
