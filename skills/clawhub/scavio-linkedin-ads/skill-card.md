## Description:

Search ads running across LinkedIn by keyword and/or advertiser company id, returning each ad's advertiser, ad copy, format, promoted label, thumbnail and a detail link, then open one ad in full with its media, headline, who paid for it and the advertiser's company URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, demand-generation, and competitive-intelligence teams use this skill to search LinkedIn ads by keyword or advertiser, inspect individual ads, and retrieve structured ad-library data through Scavio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches and ad-detail requests are sent to Scavio and consume API credits.

Mitigation: Confirm the user's intent and credit budget before making requests, and avoid unnecessary pagination.

Risk: The skill requires a Scavio API key.

Mitigation: Load SCAVIO_API_KEY from the environment or a secret store and keep it out of source control.

Risk: Sensitive research terms may be transmitted to Scavio.

Mitigation: Avoid submitting sensitive keywords or advertiser research unless the user's organization permits that use.

Risk: LinkedIn ad-library fields such as impressions, demographics, run dates, and CDN media URLs may be unavailable or short-lived.

Mitigation: Report only values returned by the API, preserve nulls where data is absent, and fetch media links promptly when needed.

## Reference(s):

- [Scavio API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=linkedin-ad-library-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=linkedin-ad-library-api)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/scavio-linkedin-ads)
- [ClawHub publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with inline Python and curl examples plus structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; each LinkedIn Ads endpoint consumes 6 Scavio credits.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
