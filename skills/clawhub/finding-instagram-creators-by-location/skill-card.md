## Description:

Finds Instagram creators and influencers posting from a specific location using apidojo's Instagram location scraper on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, local businesses, and agencies use this skill to identify Instagram creators who post from a city, venue, neighborhood, or region for regional campaigns and partnerships. It helps group location posts by creator, score repeated local presence and engagement, and return tiered creator tables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Apify with an APIFY_TOKEN and sends selected Instagram location queries to Apify.

Mitigation: Install only when that third-party processing is acceptable, keep APIFY_TOKEN out of chat and committed files, and use the documented helper or MCP flow when available.

Risk: Broad or unbounded location scrapes may collect more Instagram post data than needed for a campaign.

Mitigation: Set a reasonable maxItems limit and use date or location filters that match the intended local creator search.

Risk: Custom actor inputs can expose sensitive or unnecessary data if pasted into customMapFunction or related fields.

Mitigation: Avoid placing secrets, private customer data, or unrelated identifiers in custom actor inputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-instagram-creators-by-location)
- [Apify Instagram location scraper REST API endpoint](https://api.apify.com/v2/acts/apidojo~instagram-location-scraper/runs?token=$APIFY_TOKEN)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with creator tables, scoring notes, and optional shell commands for Apify runs; actor outputs may be saved as JSON or CSV.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an APIFY_TOKEN for Apify execution; accepts Instagram location URLs or location IDs, optional maxItems and until filters, and an optional customMapFunction.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
