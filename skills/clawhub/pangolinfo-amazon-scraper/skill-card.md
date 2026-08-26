## Description:

Guides an agent to use Pangolinfo MCP tools to collect Amazon product, keyword search, category, seller, bestseller, new-release, review, and custom URL data for structured analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pangolinfo](https://clawhub.ai/user/pangolinfo)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and ecommerce analysts use this skill to instruct agents to fetch Amazon ASIN details, search results, category and seller listings, bestseller and new-release lists, and reviews for product and voice-of-customer analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The credential model is inconsistent about whether the agent should read PANGOLINFO_API_KEY directly.

Mitigation: Configure the Pangolinfo API key in the MCP server or a scoped secret store, and avoid workflows that require the agent to read or display the key.

Risk: Amazon review scraping and broad scraping workflows can consume quota or fail when run too aggressively.

Mitigation: Use the skill's budget prompts, Fast and Full modes, and documented concurrency limits before collecting reviews or running multi-step scraping workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pangolinfo/skills/pangolinfo-amazon-scraper)
- [Pangolinfo website](https://www.pangolinfo.com)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown responses with tables, product cards, summaries, JSON tool-call examples, and occasional setup commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Pangolinfo MCP tools, avoids exposing raw tool JSON, and includes budget guidance before review scraping.]

## Skill Version(s):

4.0.0 (source: server release metadata; artifact frontmatter says 3.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
