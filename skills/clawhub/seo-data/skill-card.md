## Description:

SEO and search intelligence for agents: live Google results, keyword research, competitor and backlink gaps, page audits and AI answer visibility.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use the skill to research search results, keywords, competitors, backlinks, page health, AI answer visibility, and website technologies. It supports SEO analysis and prospecting workflows through superagnt's SEO data service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, URLs, and AI prompts are sent to superagnt for processing.

Mitigation: Avoid submitting sensitive or confidential information in requests.

Risk: Research calls consume paid credits, with costs that can scale by requested rows or results.

Mitigation: Choose request limits deliberately and review endpoint pricing before increasing result sizes.

Risk: The shared service API key grants access to the account’s paid service.

Mitigation: Keep SUPERAGNT_API_KEY private and avoid exposing it in logs or shared files.

Risk: The documented curl examples contain escaped quotes and token expansion issues.

Mitigation: Correct the examples’ quoting and bearer-token expansion before running them.

## Reference(s):

- [SEO Data documentation](https://superagnt.com/r/ch-seo-data-docs)
- [API keys and account](https://superagnt.com/r/ch-seo-data-key)
- [MCP installation guide](https://www.superagnt.com/install?facet=seo)
- [SEO Data listing](https://clawhub.ai/superagnt/skills/seo-data)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Analysis, Guidance]

**Output Format:** [SEO research results and API data, including structured JSON, Markdown summaries, and AI answers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the requested endpoint and consume paid API credits.]

## Skill Version(s):

2.0.13 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
