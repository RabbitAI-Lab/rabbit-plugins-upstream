## Description:

Guides an agent in using Pangolinfo MCP tools to retrieve Amazon product details, keyword results, category and seller listings, bestseller and new-release rankings, reviews, and custom Amazon URL data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pangolinfo](https://clawhub.ai/user/pangolinfo)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and ecommerce analysts use this skill to collect Amazon marketplace data through Pangolinfo MCP tools and present product, search, ranking, seller, and review findings in structured agent responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan found unsafe and contradictory guidance for handling a Pangolinfo API key.

Mitigation: Keep credentials outside prompts and chat-visible tool arguments, use protected MCP or client configuration, and prefer authorization headers or a secret manager.

Risk: Scraping workflows may expose sensitive tokens through URLs, logs, or generated instructions if credentials are copied into visible text.

Mitigation: Do not place Pangolinfo tokens in URLs, logs, prompts, or agent-visible examples; validate credential handling before installation.

## Reference(s):

- [Pangolinfo website](https://www.pangolinfo.com)
- [ClawHub skill page](https://clawhub.ai/pangolinfo/skills/pangolinfo-amazon-scraper)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables, concise summaries, JSON-like MCP call examples, and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should avoid raw tool JSON, cite returned data fields, respect cost and rate limits, and match the user's language.]

## Skill Version(s):

4.0.0 (source: server release metadata; artifact frontmatter says 3.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
