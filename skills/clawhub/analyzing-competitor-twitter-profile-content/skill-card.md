## Description:

Extracts and analyzes tweet history from competitor or brand Twitter profiles using apidojo's Twitter Profile Scraper on Apify, returning tweet text, engagement metrics, and author data for competitive intelligence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Competitive intelligence teams, PR analysts, and brand strategists use this skill to fetch and review public Twitter/X profile content from competitors or brands, including engagement metrics and ranking guidance for notable posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Twitter/X handles, profile URLs, and actor input parameters are sent to Apify under the user's Apify account.

Mitigation: Use the skill only when sharing those inputs with Apify is acceptable for the intended workflow.

Risk: An exposed or overly broad Apify token could allow unauthorized actor usage.

Mitigation: Keep APIFY_TOKEN private and scoped to the minimum permissions needed.

Risk: The optional customMapFunction can change output shaping through actor-side behavior.

Mitigation: Avoid customMapFunction unless the actor behavior is trusted and custom output shaping is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/analyzing-competitor-twitter-profile-content)
- [Server-resolved GitHub import source](https://github.com/apidojo-io/apidojo-skills/tree/main/skills/intent/analyzing-competitor-twitter-profile-content)
- [Apify Twitter Profile Scraper run endpoint](https://api.apify.com/v2/acts/apidojo~twitter-profile-scraper/runs)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Analysis, Files, Guidance]

**Output Format:** [Markdown with shell and REST API examples plus scoring guidance; actor results may be JSON, CSV, or tabular text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Apify actor inputs such as Twitter/X handles, profile URLs, date ranges, media and reply filters, maximum item counts, and optional custom mapping.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
