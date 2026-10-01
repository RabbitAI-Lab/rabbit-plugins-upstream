## Description:

Identifies weed species and estimates coverage density from overhead field images or videos, producing distribution data to support precision weeding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farm managers and agricultural advisers use field images or videos to assess weed types, coverage, and distribution, and to review previous analysis reports. Results support field-management decisions rather than pesticide recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Field images, videos, or media URLs are sent to the vendor's cloud service for analysis.

Mitigation: Avoid sensitive media unless the provider's account, retention, and deletion practices are acceptable.

Risk: The skill may create or reuse an internal identity, store session tokens locally, and automatically retrieve identity-linked report history.

Mitigation: Review identity and local storage behavior before installation, and use only in an environment where that access is appropriate.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-farmland-weed-identification-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis results or a Markdown table of historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include weed categories, coverage estimates, distribution data, and report links; results can be saved to a file.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release; bundled SKILL.md lists 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
