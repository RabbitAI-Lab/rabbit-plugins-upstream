## Description:

Researches books, authors, reviews, lists, charts, and audiobooks across Goodreads, Apple Books, and Audible through the Crawlora API, returning normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research books, authors, public reviews, curated lists, rankings, and audiobook details by calling Crawlora's documented book catalog endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Book and audiobook search terms, identifiers, and API credentials are sent to Crawlora when the helper runs.

Mitigation: Keep CRAWLORA_API_KEY in the environment, avoid hardcoding or logging it, and avoid submitting sensitive search terms unless sharing them with Crawlora is acceptable.

Risk: API use can consume Crawlora credits, especially when walking paginated reviews, lists, or chart endpoints.

Mitigation: Limit requests to the needed endpoints and page ranges, and confirm expected usage before high-volume research.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora API key signup](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/book-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Normalized JSON responses with concise Markdown guidance and shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses documented Crawlora routes for Goodreads, Apple Books, and Audible.]

## Skill Version(s):

1.0.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
