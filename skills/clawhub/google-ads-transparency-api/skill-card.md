## Description:

Resolve a brand or domain to a Google advertiser id, then pull every ad it runs across Search, YouTube, Shopping, Maps and Play, and open one creative with its full region and impression history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, marketers, and ad-intelligence teams use this skill to resolve Google advertiser identities, retrieve live ad creatives, and inspect creative history from public Google Ads Transparency data through Scavio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key and sends advertiser or domain queries to Scavio.

Mitigation: Store SCAVIO_API_KEY in environment or secret storage, avoid committing it to source control, and use the skill only when sending those queries to Scavio is acceptable.

Risk: Every documented request or paginated search page spends one API credit.

Mitigation: Budget searches before walking pages, cap pagination intentionally, and avoid unnecessary retries or broad pulls.

Risk: Using a search limit above 100 can return zero rows and lead to a false negative.

Mitigation: Keep search limits at 100 or lower and retry with a valid limit before concluding that an advertiser has no ads.

Risk: Google publishes reach and impression figures only where available, and non-EEA results may contain null values.

Mitigation: Report null impressions as unavailable rather than zero, and query an EEA region when the user specifically needs reach data.

## Reference(s):

- [Scavio Google Ads Advertisers API documentation](https://scavio.dev/docs/google-ads-advertisers)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-ads-transparency-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API payloads and Python, JavaScript, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide authenticated API calls to Scavio and structured JSON responses from Google Ads Transparency endpoints.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
