## Description:

Researches global news and US television coverage via the Crawlora API, including GDELT web-news search, context, timeline, sentiment, and Television 2.0 AI indexes, returning clean JSON for media and OSINT research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, analysts, journalists, and agents use this skill to query GDELT-backed news and US television coverage through Crawlora for media monitoring, OSINT, sentiment, coverage-volume trends, and cross-outlet comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send the user's Crawlora API key to a redirected API base if CRAWLORA_API_BASE is set.

Mitigation: Use the default Crawlora API base unless the alternate destination is fully trusted, and review the script before using a real key.

Risk: The helper accepts arbitrary paths, which can move calls outside the documented /gdelt/* GET endpoints.

Mitigation: Limit use to the documented GDELT endpoints or install a version that enforces those endpoint restrictions.

Risk: The skill requires a Crawlora API key for requests.

Mitigation: Store the key only in CRAWLORA_API_KEY and do not hardcode, commit, or pass it in URLs.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Crawlora API GET requests and expects CRAWLORA_API_KEY for authenticated calls.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
