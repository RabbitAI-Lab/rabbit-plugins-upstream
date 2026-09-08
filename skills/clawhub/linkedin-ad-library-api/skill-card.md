## Description:

Search LinkedIn ads by keyword or advertiser company id through Scavio, then retrieve structured ad details including advertiser, copy, format, media, payer, and company URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, marketing teams, and agents use this skill for LinkedIn ad research, competitor swipe-file creation, and ad creative inspection through Scavio's API. It is suited for workflows that need structured JSON about search results and individual ad details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key for a third-party API provider.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store and do not commit it to source control.

Risk: LinkedIn Ads query and detail calls consume Scavio credits.

Mitigation: Confirm the user is comfortable with credit consumption before running repeated searches or detail lookups.

Risk: API responses can omit impressions, demographics, run dates, or other fields.

Mitigation: Return only data present in the API response and avoid fabricating missing ad metrics or media details.

## Reference(s):

- [Scavio API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=linkedin-ad-library-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=linkedin-ad-library-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/linkedin-ad-library-api)
- [Publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, API Calls, JSON]

**Output Format:** [Markdown with inline shell, Python, curl, and JSON API guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; LinkedIn Ads API calls consume 6 credits each.]

## Skill Version(s):

1.0.2 (source: server release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
