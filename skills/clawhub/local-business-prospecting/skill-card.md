## Description:

Build and qualify local-business prospect lists by category and geography using Crawlora's Google Maps dataset, live Google Maps, Apple Maps, Yelp, and public business websites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, marketing, operations, and research users can use this skill to assemble deduplicated local-business prospect shortlists or CSVs with contact fields and qualification evidence. It is intended for public business prospecting, not for unsolicited outreach or CRM import unless the user explicitly requests those actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, selected public URLs, and the Crawlora API key are sent to Crawlora.

Mitigation: Use this skill for public business prospecting, keep the API key in an environment variable, and avoid confidential lead strategy, private URLs, or sensitive customer data unless sharing that data with Crawlora is acceptable.

Risk: Prospect outputs can be mistaken for authorization to contact businesses or import records into a CRM.

Mitigation: Treat the shortlist as research output only; perform outreach or CRM import only when the user explicitly requests it.

Risk: Indexed datasets can contain unknown closure status, missing ratings, locationless service-area businesses, or stale records.

Mitigation: Preserve source identities, refresh important candidates with live place details, report shortfalls, and keep retrieval time separate from dataset refresh time.

Risk: Public contact details can be over-interpreted as verified or inferred contact information.

Mitigation: Extract only publicly published business contact details, retain the exact source page, and do not infer email addresses or claim deliverability verification.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/local-business-prospecting)
- [Publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown tables or CSV with optional shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source URLs, retrieval timestamps, refresh status, qualification evidence, and exclusion reasons.]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
