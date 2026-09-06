## Description:

Scrapes YouTube channel statistics and optional video catalogs for channel URLs or handles using apidojo's YouTube scraper on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill to collect channel-level YouTube metrics and recent video data for creator research, competitor analysis, and audience benchmarking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends YouTube URLs, handles, keywords, and related scraping inputs to Apify under the user's APIFY_TOKEN.

Mitigation: Use only inputs appropriate for Apify processing, scope the token appropriately, and confirm that users are comfortable sending those inputs to the external actor.

Risk: The evidence notes inconsistent actor identity and scraping scope.

Mitigation: Confirm the intended Apify actor before execution and limit runs to the channel-data workflow unless broader YouTube scraping is explicitly intended.

Risk: Some channel fields may be unavailable or incomplete, such as hidden subscriber counts or age-restricted metadata.

Mitigation: Represent unavailable fields as null or flagged values and avoid treating incomplete channel records as complete measurements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-youtube-channel-data)
- [Publisher profile](https://clawhub.ai/user/apidojo-io)
- [Apify actor metadata](https://apify.com/apidojo/youtube-scraper)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and example JSON; delivered datasets may be shown as Markdown tables or saved as JSON/CSV.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output can include channel name, channel ID, subscriber count, view count, video count, country, joined date, description, channel URL, and recent videos.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata version: 1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
