## Description:

Finds medical practices, clinics, dental offices, and healthcare providers via Google Search using apidojo's Google Search Scraper on Apify, returning practice name, website URL, and Google snippet for each result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

HealthTech vendors, medical suppliers, and B2B service teams use this skill to find healthcare practices, clinics, providers, and similar business prospects in target locations. It helps agents prepare outreach-oriented prospect lists from public Google Search results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Healthcare search terms or inputs may expose sensitive personal information if users include PHI, patient names, private contact lists, or other sensitive data.

Mitigation: Use only public business prospecting queries and keep sensitive personal or patient data out of all search terms and inputs.

Risk: The skill sends healthcare business search queries to Apify-backed Google Search scraping infrastructure.

Mitigation: Install and use it only when sending those public business queries to Apify is acceptable for the user's organization.

Risk: Search results may include directories, duplicate practices, or limited contact information.

Mitigation: Filter directory domains, deduplicate by domain, and treat URL and snippet results as a starting list that requires review before outreach.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-healthcare-practices-via-google-search)
- [Apify Google Search Scraper API endpoint](https://api.apify.com/v2/acts/apidojo~google-search-scraper/runs)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured search-result data suitable for table, CSV, or JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include practice name, website URL, Google snippet, and optional scoring or ranking labels.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
