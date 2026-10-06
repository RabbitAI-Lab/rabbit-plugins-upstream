## Description:

Builds and qualifies local-business prospect lists by category and geography using Crawlora's business datasets, live map sources, and public business websites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and business-development teams use this skill to research and deduplicate public local-business listings, qualify prospects against stated criteria, and produce a sourced shortlist or CSV. Research does not authorize outreach or CRM import.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends the Crawlora API key and prospecting queries to Crawlora.

Mitigation: Install only if you accept this data sharing; keep the API key in the environment and avoid sensitive queries.

Risk: A researched prospect list could be used for unsolicited outreach without the user's authorization.

Mitigation: Limit the workflow to public business research; request and review a separate outreach workflow before contacting prospects or importing them into a CRM.

## Reference(s):

- [Local Business Prospecting on ClawHub](https://clawhub.ai/crawlora-org/skills/local-business-prospecting)
- [Crawlora](https://crawlora.net)
- [Endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV, Guidance]

**Output Format:** [Markdown table or CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes qualification evidence, source URLs, retrieval times, and refresh status where available.]

## Skill Version(s):

1.0.10 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
