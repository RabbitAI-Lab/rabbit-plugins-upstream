## Description:

Searches LinkedIn ads by keyword or advertiser company ID through Scavio, returns ad summaries with creative metadata, and opens individual ads for full details including media, headline, payer, and advertiser company URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and marketing teams use this skill to research LinkedIn ad activity, inspect competitor or advertiser creatives, and retrieve structured ad details from Scavio-backed LinkedIn Ad Library endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Scavio as a third-party API provider and sends LinkedIn ad lookup requests to Scavio endpoints.

Mitigation: Install only when third-party API use is acceptable for the workflow and review Scavio documentation before use.

Risk: SCAVIO_API_KEY could be exposed if copied into source code, logs, or shared prompts.

Mitigation: Keep SCAVIO_API_KEY in the environment or a secret store and do not hardcode it.

Risk: Each LinkedIn ads request consumes credits, so broad or repeated queries can create avoidable usage cost.

Mitigation: Use targeted keywords, company IDs, country filters, and rate-limit handling before making repeated calls.

Risk: LinkedIn ad metrics, media, impressions, demographics, and run dates may be absent or short-lived in returned data.

Mitigation: Return only API-provided values, do not infer missing metrics, and fetch CDN media links promptly when needed.

## Reference(s):

- [Scavio Documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=linkedin-ad-library-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=linkedin-ad-library-api)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/linkedin-ad-library-api)

## Skill Output:

**Output Type(s):** [API calls, JSON, Guidance]

**Output Format:** [Markdown guidance with JSON API responses and optional shell or Python request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; LinkedIn ads search and detail calls each consume 6 credits.]

## Skill Version(s):

1.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
