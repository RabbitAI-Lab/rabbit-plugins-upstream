## Description:

Search Redfin listings for sale, sold or for rent, pull one property in full with the Redfin Estimate and MLS fact sheet, and read housing-market stats for a region. 3 endpoints, 1 credit each.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Redfin sale, sold, and rental listings, inspect individual property details, and gather regional housing-market statistics for real-estate research, lead lists, comparable-sales analysis, and market-trend datasets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and property identifiers are sent to Scavio's external API and consume credits.

Mitigation: Use the skill only for user-requested real-estate research, prefer efficient searches, and make credit use clear when planning calls.

Risk: The Scavio API key is required for requests.

Mitigation: Keep SCAVIO_API_KEY private and avoid exposing it in prompts, logs, code examples, or shared outputs.

Risk: Listing data, market statistics, and estimates can change quickly.

Mitigation: Include when data was fetched and verify important property facts or estimates against the original Redfin listing before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-redfin)
- [Scavio Redfin Search documentation](https://scavio.dev/docs/redfin-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with JSON API payloads and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; requests call Scavio's external API and consume credits.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
