## Description:

Minimal cross-platform web search via Bing RSS with no API key and no dependencies beyond Python 3.8+ or curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cute-omega](https://clawhub.ai/user/cute-omega)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to perform basic web search when a built-in web search tool is unavailable, unconfigured, or unreachable. It returns titles, URLs, and snippets from Bing RSS in either readable text or JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to Bing over the network and may expose sensitive information.

Mitigation: Do not search for secrets, credentials, private customer data, or confidential internal material with this skill.

Risk: Search quality and availability depend on Bing RSS behavior, including regional bias, rate limiting, and empty results for niche queries.

Mitigation: Review returned links and snippets before relying on them, and use another search path when higher assurance, pagination, or stable coverage is required.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cute-omega/skills/min-web-search-skill)
- [Bing RSS Search Endpoint](https://www.bing.com/search?q={query}&format=rss)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON search results with titles, URLs, and snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a max-results option; practical result count is limited by the Bing RSS feed.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
