## Description:

Helps prepare the patent portion of China's High-Tech Enterprise certification by classifying company patents, checking ownership and validity, and estimating the intellectual-property quantity score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Companies and their advisors preparing or renewing China's High-Tech Enterprise certification use this skill to inventory eligible patents, distinguish Class I and II rights and acquisition methods, and estimate the quantity-based score.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Company names, patent searches, and technical context are sent to a third-party patent service, which may charge for API calls.

Mitigation: Obtain permission to share this information and disclose likely API charges before searching.

Risk: API or trial credentials and task cache may persist locally.

Mitigation: Set PATENTMAX_API_KEY only in trusted environments and remove ~/.patentmax when stored trial keys or cache are no longer needed.

Risk: An environment setting can redirect the patent API connection to another endpoint.

Mitigation: Do not set PATENTMAX_BASE_URL unless you control and trust the endpoint.

Risk: Patent status and certification eligibility estimates may not reflect official records or current local requirements.

Mitigation: Confirm legal status against official patent records and check current certification rules with the local authority before filing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/hitech-patent-prep)
- [Publisher profile](https://clawhub.ai/user/ip930)
- [PatentMax API reference](references/api-reference.md)
- [Patent search syntax](references/query-syntax.md)
- [Patent search workflow](references/search-workflow.md)

## Skill Output:

**Output Type(s):** [Text, CSV files]

**Output Format:** [UTF-8 CSV patent inventory and written score estimate]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lists eligible and pending patents separately; estimates only the intellectual-property quantity component, not the full certification score.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
