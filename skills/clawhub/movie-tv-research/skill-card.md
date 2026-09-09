## Description:

Researches movies and TV shows through Crawlora API endpoints for metadata, cast and crew, ratings, reviews, streaming availability, and box-office performance, returning normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer movie and TV research questions, including cast and crew lookup, score comparison, streaming availability, reviews, recommendations, and box-office analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Crawlora API key and request data could be sent to an unintended server if CRAWLORA_API_BASE is configured incorrectly.

Mitigation: Before use, leave CRAWLORA_API_BASE unset or set it exactly to https://api.crawlora.net/api/v1; treat CRAWLORA_API_KEY as a credential and rotate it after use in untrusted environments.

Risk: Entertainment lookup queries may expose secrets, private identifiers, or personal data if those values are included in query parameters or JSON bodies.

Mitigation: Review lookup inputs before execution and avoid sending secrets, private identifiers, or personal data to the Crawlora API.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/movie-tv-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and normalized JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; requests use Crawlora movie and TV lookup endpoints.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
