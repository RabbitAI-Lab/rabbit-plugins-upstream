## Description:

Researches Pinterest profiles, boards, pins, ideas categories, and search results via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and content researchers use this skill to gather public Pinterest profile, board, pin, category, and keyword-search data through Crawlora instead of scraping Pinterest directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shipped Crawlora helper can send the Crawlora API key to requests outside the documented Pinterest endpoints.

Mitigation: Use the helper only with the documented Pinterest paths, review commands before execution, and prefer a version that restricts requests to those endpoints.

Risk: CRAWLORA_API_BASE can redirect requests and the API key to a configurable host.

Mitigation: Do not set CRAWLORA_API_BASE unless you fully control and trust the destination.

Risk: The skill requires a real Crawlora API key for live requests.

Mitigation: Keep the key in CRAWLORA_API_KEY only, avoid committing it, and run the skill in a trusted shell environment.

## Reference(s):

- [Pinterest Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, text]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY for live Crawlora API calls.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
