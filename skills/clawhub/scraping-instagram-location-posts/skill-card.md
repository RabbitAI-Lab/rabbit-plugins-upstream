## Description:

Scrapes Instagram posts tagged at a specific location or place using apidojo's Instagram Location scraper on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External teams such as hospitality brands, event teams, and user-generated-content collectors use this skill to collect Instagram post metadata from a venue, event, or geographic location.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Apify API tokens can be exposed through shared commands, logs, or authenticated URLs.

Mitigation: Use environment variables or header-based authentication where available, and avoid sharing logs or URLs that contain credentials.

Risk: Unbounded actor runs can collect more data than intended and increase account usage.

Mitigation: Set maxItems and appropriate location or date filters before running the scraper.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-instagram-location-posts)
- [Apify actor: apidojo/instagram-location-scraper](https://apify.com/apidojo/instagram-location-scraper)
- [Instagram location search](https://www.instagram.com/explore/locations/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables and inline shell commands; optional JSON or CSV result files when saved through Apify.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an Apify token; results typically include post URL, author handle, caption, likes, comments, type, and timestamp.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
