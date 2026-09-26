## Description:

Looks up Zhejiang public-works contract awards by supplier and summarizes projects, contract amounts, dates, and comparable price ranges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Suppliers and procurement analysts can review a company's recorded Zhejiang public-works awards, contract amounts, and prices for similar project types. The results are not an assessment of company creditworthiness.

### Deployment Geography for Use:

Zhejiang Province, China (data coverage)

## Known Risks and Mitigations:

Risk: Search queries are sent to the vendor's HTTPS service.

Mitigation: Use only for appropriate Zhejiang tender-history queries; avoid including sensitive information in searches.

Risk: Product-specific credentials and session cookies are stored locally.

Mitigation: Protect access to the local credential file and install only if this storage is acceptable.

Risk: Only collected contract notices are covered; missing results do not establish that a supplier has no awards.

Mitigation: Disclose the coverage limit and do not use results for general procurement or company credit evaluations.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chenqg618/skills/zj-tender-history)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lists recorded projects, dates, contract amounts, comparable price percentiles, and coverage caveats.]

## Skill Version(s):

1.0.9 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
