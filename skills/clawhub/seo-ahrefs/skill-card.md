## Description:

Ahrefs API analyst (extension). Reads referring domains, backlinks, organic keywords, and content explorer data via the tested @ahrefs/mcp@0.0.11 server. Pairs with seo-backlinks for multi-source confidence weighting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and SEO analysts use this skill to query Ahrefs metrics, backlink, organic keyword, and content explorer data through the Ahrefs MCP server, then combine results with other SEO sources for confidence-weighted reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external Ahrefs MCP extension and install script.

Mitigation: Confirm the referenced Ahrefs MCP extension and install script are from a trusted source before installation.

Risk: Ahrefs API calls may consume paid units, especially for batches of 50 or more URLs.

Mitigation: Estimate batch cost before execution, surface the estimate to the orchestrator, and log actual cost after each call.

## Reference(s):

- [Ahrefs API](https://ahrefs.com/api)
- [seo-ahrefs ClawHub release](https://clawhub.ai/asale-ai/skills/seo-ahrefs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with cited live Ahrefs metrics and concise setup or routing commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Metrics should cite Ahrefs as the live source; batch usage should include estimated and actual Ahrefs API unit cost.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
