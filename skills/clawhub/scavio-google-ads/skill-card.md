## Description:

Scavio Google Ads resolves a brand or domain to a Google advertiser ID, pulls ads across Search, YouTube, Shopping, Maps and Play, and opens a creative with its region and impression history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, and developers use this skill to research Google Ads Transparency Center advertisers, active creatives, regional impression ranges, and political ad disclosures through Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-supplied advertiser, domain, region, and creative queries are sent to Scavio's API with the user's SCAVIO_API_KEY.

Mitigation: Confirm the queries are appropriate to share with Scavio and keep the API key in environment or secret storage rather than source files.

Risk: Each endpoint call consumes Scavio API credits, and cursor pagination can multiply the number of requests.

Mitigation: Budget requests before long searches, keep page limits at or below 100, and cap pagination walks when broad collection is unnecessary.

Risk: Google publishes impression data only where available and reports ad counts and impressions as ranges rather than exact numbers.

Mitigation: Report unavailable impression fields as unavailable, not zero, and preserve published ranges instead of converting them to precise figures.

## Reference(s):

- [Scavio Google Ads Advertisers documentation](https://scavio.dev/docs/google-ads-advertisers)
- [Scavio rate limits documentation](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-google-ads)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request bodies and Python or JavaScript code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides API requests and interpretation of structured Google Ads Transparency data; requests consume Scavio API credits.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
