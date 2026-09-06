## Description:

Finds digital marketing agencies, creative studios, and web design firms via Google Search using apidojo's Google Search Scraper on Apify, returning agency names, website URLs, snippets, and priority tiers for outreach.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, partnership, and business development teams use this skill to build prospect lists of digital agencies by location or specialty for outreach. It helps agents run Google Search Scraper queries, rank likely agency domains, and prepare initial lead lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, start URLs, and custom mapping input are sent to Apify during actor execution.

Mitigation: Avoid including secrets, private customer data, or unrelated sensitive information in search terms, start URLs, or customMapFunction input.

Risk: Actor execution requires an APIFY_TOKEN.

Mitigation: Keep APIFY_TOKEN in an environment variable or secret manager and do not commit it in commands, examples, or output files.

Risk: Google search results can include directories, non-agency pages, duplicates, or low-confidence prospects.

Mitigation: Apply the documented filtering, scoring, and domain deduplication steps, then manually review leads before outreach.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-digital-agencies-via-google-search)
- [Apify Google Search Scraper run endpoint](https://api.apify.com/v2/acts/apidojo~google-search-scraper/runs)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown with inline bash, curl, JSON input examples, scoring guidance, and optional CSV or JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agency names, website URLs, Google snippets, relevance scores, and prospect tiers when executed with the Apify actor.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata version 1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
