## Description:

Analyzes Amazon competitor ASIN reviews with ARI to compare praise, complaints, trends, and gaps, then produces review reports and positioning suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to collect and compare Amazon review data for their own and competing ASINs, generate VOC, benchmark, keyword, and comparison reports, monitor negative-review alerts, and identify product and listing improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store and use an ARI API key for authenticated review-analysis workflows.

Mitigation: Install only if you trust ARI, keep API keys out of reports and shared files, and revoke or rotate the key from the ARI account page if access is no longer needed.

Risk: Some collection, analysis, leaderboard, and monitoring actions can consume ARI credits, and auto-confirm settings may allow spending without a fresh prompt.

Mitigation: Review or disable auto-confirm before use, require quotes for paid actions when appropriate, and confirm schedule, watch, and competitor-monitoring costs before enabling ongoing collection.

Risk: Interrupted paid analysis or collection can already have consumed credits or produced an archived report.

Mitigation: Check the latest reports or operation status before retrying a confirmed paid command, and rerun paid commands only after confirming that no result was generated.

Risk: The skill can export report and review files locally.

Mitigation: Choose export paths deliberately, inspect exported Markdown, HTML, or CSV before sharing, and avoid placing sensitive data in public or synced directories.

Risk: A custom ARI base URL could redirect authenticated requests if the environment is intentionally configured that way.

Mitigation: Use the default ARI service unless operating a trusted self-managed environment, and clear unexpected ARI_BASE_URL or ARI_WEB_URL settings before running authenticated commands.

## Reference(s):

- [ARI CLI and API Reference](references/reference.md)
- [Skill README](README.md)
- [User Guide](使用说明.md)
- [ClawHub Skill Listing](https://clawhub.ai/funewa/skills/competitor-review)
- [ARI Product Management](https://ari.funewa.com/zh/products)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown reports, structured JSON from CLI commands, CSV/Markdown/HTML export files, and shell command or configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Some collection, analysis, monitoring, and leaderboard workflows can consume ARI credits and may depend on confirmation or auto-confirm settings.]

## Skill Version(s):

1.4.5 (source: server release evidence, _meta.json, SKILL.md frontmatter, CLI VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
