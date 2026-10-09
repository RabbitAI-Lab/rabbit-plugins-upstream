## Description:

Builds source-attributed investor and fund shortlists from Crawlora's public PitchBook profile data while preserving gaps in public coverage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Founders, fundraising teams, and their advisers use the skill to research potential investors and funds for a specified company and round, compare evidence of fit, and flag unresolved criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Crawlora API key and research query parameters are sent to Crawlora's API.

Mitigation: Use a scoped, rotatable key where possible and avoid submitting sensitive query details.

Risk: Public profile previews and stored records may be incomplete or stale, so shortlist results are not verified investment advice.

Mitigation: Review source dates and evidence, preserve unknown criteria, and independently verify candidates before decisions or outreach.

## Reference(s):

- [Investor fit research endpoint reference](artifact/reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/investor-fit-research)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown shortlist and criterion matrix]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes attributed sources, fit and uncertainty assessments, and conditional or rejected candidates.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
