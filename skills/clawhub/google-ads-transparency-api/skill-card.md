## Description:

Resolve a brand or domain to a Google advertiser ID, retrieve its Google ads across Search, YouTube, Shopping, Maps, and Play, and open individual creatives with region and impression history through Scavio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketing, advertising, and research users use this skill to resolve Google advertiser IDs and retrieve public ad-transparency data through Scavio for competitor monitoring, creative research, and political-ad review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key and sends ad-research queries to Scavio.

Mitigation: Use an environment or secret store for SCAVIO_API_KEY, avoid placing keys in source files or prompts, and confirm that the user is comfortable sending the query to Scavio before making requests.

Risk: Each endpoint call consumes credits, and cursor pagination can multiply usage.

Mitigation: Set a page budget before walking paginated results, cap search pages deliberately, and monitor returned credit counts and rate-limit responses.

Risk: Google transparency data can be misread when region filters, impression ranges, null EEA-only fields, or the 100-result limit are ignored.

Mitigation: Report ranges as ranges, preserve null impression values as unavailable data, keep limits at 100 or below, and include region and format caveats in summaries.

## Reference(s):

- [Scavio Google Ads Advertisers documentation](https://scavio.dev/docs/google-ads-advertisers?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-ads-transparency-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-ads-transparency-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-ads-transparency-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API payloads and Python, JavaScript, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve advertiser IDs, creative IDs, regions, pagination cursors, ranges, and null values from the API response.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
