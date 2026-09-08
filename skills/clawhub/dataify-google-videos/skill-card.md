## Description:

Search Google Videos for video results. Do not use for YouTube media downloads or structured YouTube records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn a Google Videos search request into a Dataify Scraper API call and receive video search results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Videos search parameters are sent to Dataify and may use Dataify account credits.

Mitigation: Install and run the skill only when this external API use and credit consumption are acceptable for the intended search.

Risk: The skill requires a Dataify API token for live requests.

Mitigation: Store DATAIFY_API_TOKEN in the shell environment or another local secret store, and do not paste the token into chat.

## Reference(s):

- [Dataify Google Videos API](references/google_videos_api.md)
- [Dataify Scraper API endpoint](https://scraperapi.dataify.com/request)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-google-videos)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries, parameter tables, shell commands, and JSON or HTML when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Dataify account credits and requires DATAIFY_API_TOKEN for live API calls.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
