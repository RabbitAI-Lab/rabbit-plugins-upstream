## Description:

Builds and qualifies deduplicated local-business prospect lists by category and geography using Crawlora's business datasets, maps results, and public business websites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and business-development teams use this skill to research and qualify local businesses, producing a sourced shortlist or CSV for review before outreach or CRM import.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Business search and website inputs are shared with a third-party service.

Mitigation: Use only publicly available business information and avoid submitting private or non-public data.

Risk: A disclosed third-party API key is needed for prospecting requests.

Mitigation: Keep the Crawlora API key in the environment and do not include it in shared results.

Risk: Prospect details or qualification signals may be incomplete or stale.

Mitigation: Review the sourced lead list before outreach or CRM import; report uncertain or unrefreshed entries.

## Reference(s):

- [Crawlora endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV]

**Output Format:** [Sourced prospect table or CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Business contact details, qualification evidence, source URLs, and refresh status when available.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
