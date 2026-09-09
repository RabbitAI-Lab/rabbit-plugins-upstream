## Description:

Researches Bonhams auctions and lots via the Crawlora API for upcoming and past sales, lot search, estimates, realized prices, departments, and auction detail, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and auction analysts use this skill to query Bonhams auction and lot data through Crawlora for sale discovery, comparable-lot research, estimates, realized prices, and auction detail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send CRAWLORA_API_KEY to a non-Crawlora host if CRAWLORA_API_BASE is set to an arbitrary value.

Mitigation: Unset CRAWLORA_API_BASE or pin it to https://api.crawlora.net/api/v1 before running the helper; review shell commands before execution.

Risk: Auction queries or request bodies may contain private or sensitive research data sent to Crawlora.

Mitigation: Avoid sending secrets, internal notes, or private data in query text or JSON request bodies.

## Reference(s):

- [auction-research endpoint reference](artifact/reference/endpoints.md)
- [auction-research on ClawHub](https://clawhub.ai/tonywangcn/skills/auction-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses from the helper]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The helper prints raw JSON to stdout; callers can pipe responses into jq for post-processing.]

## Skill Version(s):

1.0.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
