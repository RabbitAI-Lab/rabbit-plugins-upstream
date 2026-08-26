## Description:

Search Amazon products, retrieve known product details, and collect product reviews through the official Gecho Bridge MCP tools for marketplace discovery, catalog research, product comparison, review analysis, and ASIN-level research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketplace researchers use this skill to route Amazon product discovery, ASIN-level product inspection, and review collection requests through Gecho Bridge MCP tools. It is best suited for read-only catalog research, product comparison, and review theme analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires trusting Gecho's Chrome extension and MCP server with access to Amazon pages available in the logged-in browser session.

Mitigation: Use the skill for read-only product and review research, and avoid running it in sensitive Chrome profiles when that access is unnecessary.

Risk: Raw product or review results may be written to local JSON files.

Mitigation: Choose save directories deliberately and review stored result files before sharing or retaining them.

Risk: Amazon login walls, CAPTCHA prompts, regional prompts, rate limits, unavailable listings, or blocked pages can prevent reliable collection.

Mitigation: Resolve browser prompts manually in Chrome and report unavailable or blocked page states instead of inventing product, listing, or review data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/amazon)
- [Gecho website](https://gecho.ai/)
- [Gecho Bridge GitHub repository](https://github.com/gecho-ai/gecho-bridge)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with inline shell commands and structured tool-result descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local JSON result paths when Gecho tools save Amazon search, product, or review data.]

## Skill Version(s):

1.1.37 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
