## Description:

Researches Ulta Beauty's catalog, including categories, products, shades, questions, reviews, and nearby stores, using the Crawlora API and returns clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to research Ulta Beauty products, compare category or search results, inspect product details, Q&A, reviews, shade variants, and locate nearby stores through Crawlora instead of scraping Ulta pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ulta search terms, product IDs, and store location searches are sent to Crawlora using the user's API key.

Mitigation: Only submit queries and locations the user is comfortable sending to Crawlora, and avoid including unnecessary personal or sensitive details.

Risk: The helper script can use a custom CRAWLORA_API_BASE when the environment is changed.

Mitigation: Leave CRAWLORA_API_BASE unset unless the destination is fully trusted.

Risk: API credentials may be exposed if the Crawlora key is hardcoded, passed in query strings, or committed.

Mitigation: Keep CRAWLORA_API_KEY in the environment only and do not commit it to source files or logs.

## Reference(s):

- [Ulta endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/ulta-research)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora API requests; paginated endpoints may require page-by-page retrieval.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
