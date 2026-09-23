## Description:

Search Amazon products, retrieve known product details, and collect product reviews through the official Gecho Bridge MCP tools for marketplace discovery, catalog research, product comparison, review analysis, and ASIN-level research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketplace researchers use this skill to run Amazon product discovery, product detail lookup, and review analysis through Gecho Bridge. It is best suited for product comparison, catalog research, and ASIN-level marketplace validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Gecho's Chrome extension and MCP server and uses the user's logged-in Amazon browser session to read marketplace pages.

Mitigation: Install and use it only when Gecho is trusted, keep the extension logged in intentionally, and prefer a dedicated browser profile for marketplace research.

Risk: Amazon login walls, CAPTCHA challenges, regional prompts, rate limits, unavailable listings, or blocked pages can prevent successful research.

Mitigation: Resolve browser prompts manually in Chrome and have the agent report page state or tool errors instead of inventing product, listing, rating, or review data.

Risk: Parallel or unofficial Amazon data collection can produce unreliable behavior or bypass the skill's stated safeguards.

Mitigation: Use only the official Gecho MCP tools, keep search, product, and review workflows sequential, and avoid generic web scraping or unofficial APIs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/amazon)
- [Gecho publisher profile](https://clawhub.ai/user/gecho-ai)
- [Gecho website](https://gecho.ai/)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with links, setup commands, troubleshooting guidance, and saved JSON file paths when returned by tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local JSON result files produced by the Gecho Bridge MCP tools when a writable save directory is available.]

## Skill Version(s):

1.1.38 (source: server release evidence and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
