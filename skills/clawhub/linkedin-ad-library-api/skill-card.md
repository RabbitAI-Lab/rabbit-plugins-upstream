## Description:

Search ads running across LinkedIn by keyword and/or advertiser company id, returning each ad's advertiser, ad copy, format, promoted label, thumbnail and a detail link, then open one ad in full with its media, headline, who paid for it and the advertiser's company URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketing analysts, and demand-generation teams use this skill to query Scavio's LinkedIn Ads endpoints for keyword, company, and ad-detail research. It helps agents gather structured ad creative, advertiser, media, headline, and paid-for-by data without fabricating missing metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and the Scavio API key are used with a third-party service.

Mitigation: Keep SCAVIO_API_KEY in an environment variable or secret store, and avoid submitting sensitive query content unless the user accepts third-party processing.

Risk: Each LinkedIn Ads endpoint call consumes disclosed credits.

Mitigation: Confirm the query scope before calling the API, paginate deliberately, and surface credit-related failures to the user.

Risk: The API may return null impressions, demographics, run dates, or other unavailable fields.

Mitigation: Return only values present in the API response and state when reach, spend, or demographic details are unavailable.

Risk: LinkedIn CDN media links returned by the API may expire.

Mitigation: Fetch media promptly when needed and avoid treating returned CDN URLs as stable long-term links.

## Reference(s):

- [Scavio documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=linkedin-ad-library-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=linkedin-ad-library-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/linkedin-ad-library-api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, API Calls, JSON]

**Output Format:** [Markdown guidance with inline shell, Python, curl, and structured JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; LinkedIn Ads endpoints cost 6 credits per call and return paged or detail-level JSON.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
