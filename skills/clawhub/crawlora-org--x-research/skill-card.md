## Description:

Researches public X profiles, recent posts, and single post details through the Crawlora API and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to retrieve public X profile statistics, recent profile posts, and individual post content or engagement without scraping x.com directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested public X handles, post IDs, query parameters, and the Crawlora API key are sent to Crawlora.

Mitigation: Install only when that data flow is acceptable, keep the API key in the documented environment variable, and avoid private data in request arguments.

Risk: The skill is limited to public X profile and post lookup endpoints and does not provide search, trending data, private content, or cursor-paginated timelines.

Mitigation: Use only the documented endpoints and treat missing search, trending, private-content, or deeper timeline coverage as out of scope.

## Reference(s):

- [x-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub x-research skill page](https://clawhub.ai/crawlora-org/skills/x-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY in the environment; profile-post results are limited to the first public profile page payload.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
