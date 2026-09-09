## Description:

Runs SERP and keyword research via the Crawlora API, covering Google, Bing, Brave, DuckDuckGo, Yahoo, and Google Trends data, and returns clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SEO analysts, and research teams use this skill to query public search result pages, keyword suggestions, and Google Trends signals through Crawlora instead of scraping result pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper allows CRAWLORA_API_BASE to redirect authenticated requests, which could expose the Crawlora API key to an untrusted endpoint.

Mitigation: Leave CRAWLORA_API_BASE unset unless the destination is fully trusted, or use a version that pins or validates the API base before sending the API key.

Risk: Search terms, company or place identifiers, and request bodies are sent to Crawlora.

Mitigation: Avoid submitting confidential, regulated, or sensitive queries unless that data sharing is approved.

Risk: The endpoint reference documents broader Crawlora API capabilities than the skill's SERP and keyword research purpose.

Mitigation: Review planned endpoint use before installation and restrict calls to the SERP, suggest, and trends endpoints needed for the task.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/serp-keyword-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and may send search terms, company or place identifiers, and request bodies to Crawlora.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
