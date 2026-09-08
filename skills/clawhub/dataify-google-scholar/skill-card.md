## Description:

Search Google Scholar for academic papers and scholarly results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to translate Google Scholar research requests into Dataify Scraper API calls and receive compact academic search results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends search parameters and a Dataify API token to Dataify and may consume account credits.

Mitigation: Review requests before high-volume or ambiguous searches, keep the token in the environment, and avoid exposing credentials in chat or output.

Risk: Security evidence flags a scope contradiction: the skill says not to use it for patents but documents and enables patent and U.S. case-law search paths.

Mitigation: Treat patent and case-law searches as out of scope unless explicitly reviewed and approved for the deployment.

## Reference(s):

- [Dataify Google Scholar API Reference](references/google_scholar_api.md)
- [Dataify Scraper API endpoint](https://scraperapi.dataify.com/request)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-google-scholar)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with optional shell commands and raw JSON or HTML when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the Dataify Scraper API using a Dataify API token and return compact result summaries by default.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
