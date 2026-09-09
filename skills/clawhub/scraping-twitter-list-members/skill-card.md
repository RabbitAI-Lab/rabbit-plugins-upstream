## Description:

Scrapes all members and their profile data from any public Twitter/X list using apidojo's Twitter List scraper on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, competitive intelligence teams, curators, and outreach teams use this skill to collect public Twitter/X list member profiles and export profile metadata for review or downstream workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Twitter/X list URLs are sent to Apify for processing.

Mitigation: Use only public lists and confirm users are comfortable sharing the target list URLs with Apify before running the actor.

Risk: Exported member profile data may contain personal or sensitive profile metadata.

Mitigation: Collect only the fields needed, protect CSV or JSON exports, and follow applicable platform terms, privacy rules, and outreach policies.

Risk: Private, deleted, moved, very large, or rate-limited lists may produce empty or partial results.

Mitigation: Validate that the list is public and reachable, set practical maxItems limits, and retry large lists in smaller batches.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-twitter-list-members)
- [Publisher profile](https://clawhub.ai/user/apidojo-io)
- [Apify actor: apidojo/twitter-list-scraper](https://apify.com/apidojo/twitter-list-scraper)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, API request examples, and tabular result guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to save scraped public profile data as CSV or JSON when requested.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
