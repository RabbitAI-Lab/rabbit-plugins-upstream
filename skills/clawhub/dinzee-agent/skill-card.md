## Description:

DinzeeAgent helps agents run cross-border e-commerce research by discovering Dinzee gateway data tools, syncing bundled business skills, calling selected tools with a user token, and summarizing results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yefeng311](https://clawhub.ai/user/yefeng311)

### License/Terms of Use:

MIT-0

## Use Case:

External users, commerce analysts, and developers use this skill to route Amazon and cross-border e-commerce research tasks through Dinzee data sources, local bundled business skills, and generated summaries. It supports product, market, advertising, traffic, keyword, and supplier research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or update local business skills delivered through the Dinzee gateway.

Mitigation: Use only in an agent environment where Dinzee gateway-delivered skills are trusted; avoid broad update requests and keep any overridden skills directory under a controlled skills root.

Risk: Gateway tool calls and skill install/update operations can charge user points.

Mitigation: Confirm pricing from catalog, provider, list-tools, or charge details before running chargeable operations, and ensure the user intends to spend points.

Risk: Business call records may be saved locally, and artifact evidence shows broad permissions for data directories and JSON records.

Mitigation: Use --no-save for sensitive tasks or set DINZEE_DATA_DIR to a restricted private directory before running calls that may contain sensitive business data.

## Reference(s):

- [Dinzee Gateway](https://gateway.dinzee.ai/)
- [ClawHub Skill Page](https://clawhub.ai/yefeng311/skills/dinzee-agent)
- [Keepa API Reference](artifact/references/keepa.md)
- [Seller Sprite MCP Reference](artifact/references/seller-sprite.md)
- [SIF MCP Reference](artifact/references/sif.md)
- [Sorftime MCP Reference](artifact/references/sorftime.md)
- [Server Skill Workflows](artifact/references/server-skill-workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with inline shell commands, JSON tool-call records, report links, and point-charge details when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Gateway call results are saved locally by default unless --no-save is used; some workflows may return hosted report URLs.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
