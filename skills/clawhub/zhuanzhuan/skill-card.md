## Description:

Zhuanzhuan Assistant helps agents support second-hand buying, resale valuation, market-price checks, product-detail review, and account-page link retrieval through the Zhuanzhuan MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhuanzhuan-tech](https://clawhub.ai/user/zhuanzhuan-tech)

### License/Terms of Use:

MIT-0

## Use Case:

External users and shopping assistants use this skill to search second-hand listings, compare market prices, estimate resale value from descriptions or selected images, and navigate Zhuanzhuan account links after MCP setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence flags under-disclosed self-update behavior that may download and overwrite the installed skill package.

Mitigation: Approve updates only after independently verifying the downloaded package; prefer a managed update channel with signed or hash-verified releases.

Risk: Security evidence flags broad credential and configuration handling for the Zhuanzhuan MCP integration.

Mitigation: Use scoped secret storage, review MCP configuration before installation, and do not expose tokens in chat, logs, or generated files.

Risk: Valuation workflows may upload user-selected product images to a Zhuanzhuan endpoint.

Mitigation: Upload only images the user explicitly selects for valuation and avoid images containing unrelated sensitive information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhuanzhuan-tech/skills/zhuanzhuan)
- [Publisher profile](https://clawhub.ai/user/zhuanzhuan-tech)
- [MCP setup guide](artifact/guides/mcp-setup.md)
- [Image upload guide](artifact/guides/image-upload.md)
- [Detail display guide](artifact/guides/detail-display.md)
- [Skill upgrade guide](artifact/guides/skill-upgrade.md)
- [Zhuanzhuan open platform MCP setup](https://open.zhuanzhuan.com/mcp?copymcp=1)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown shopping results and links, optional HTML product cards, JSON MCP configuration, and inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a configured zz-mcp server for live listings, prices, valuations, account links, orders, and logistics.]

## Skill Version(s):

1.5.5 (source: server release metadata; artifact frontmatter reports 1.5.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
