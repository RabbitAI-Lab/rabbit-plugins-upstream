## Description:

Extracts comments from Instagram posts using apidojo's Instagram Comments Scraper on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Social media analysts, community managers, and researchers use this skill to collect Instagram post comments for downstream sentiment analysis, audience research, and engagement review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Instagram comment collection can raise platform-terms and privacy obligations.

Mitigation: Confirm the intended use complies with Instagram's terms and applicable privacy rules before installing or running the skill.

Risk: Returned data can include user IDs, usernames, full names, profile picture URLs, comment text, and timestamps.

Mitigation: Limit collection with explicit maxItems values and avoid exporting or retaining personal data unless it is necessary for the approved use case.

Risk: The REST/API path depends on an APIFY_TOKEN credential.

Mitigation: Protect the APIFY_TOKEN like any other API credential and avoid exposing it in prompts, logs, or shared output.

Risk: Unbounded or high-volume scraping can hit rate limits or collect more data than intended.

Mitigation: Use scoped post URLs or IDs, set maxItems, and reduce collection volume or schedule runs off peak when rate limits occur.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-instagram-comments)
- [Publisher profile](https://clawhub.ai/user/apidojo-io)
- [Apify Instagram Comments Scraper API endpoint](https://api.apify.com/v2/acts/apidojo~instagram-comments-scraper/runs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell and API examples; collected comments may be returned as tables, CSV, or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an Apify actor invocation and, for REST/API execution, an APIFY_TOKEN; maxItems can bound collection size.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
