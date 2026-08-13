## Description:

Provides TikTok Shop ERP authorization, authorized store listing, and optional token lookup or manual refresh workflows for LinkFox agents, limited to appType=erp and global or US regions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and agents use this skill to create TikTok Shop ERP authorization URLs, confirm authorized ERP stores, and troubleshoot stored ERP tokens when explicitly needed.

### Deployment Geography for Use:

Global and United States

## Known Risks and Mitigations:

Risk: The skill handles sensitive authorization workflows and may persist authorization URLs, seller identifiers, masked token metadata, or API error details locally.

Mitigation: Review before installing, keep the local LinkFox response directory private, and avoid committing response files.

Risk: Credentialed requests can be routed through configurable gateway environment variables.

Mitigation: Use only trusted LinkFox gateway configuration and avoid setting LINKFOX_TOOL_GATEWAY or TIKTOK_SHOP_API_BASE_URL to untrusted hosts.

Risk: Manual token lookup or refresh can expose sensitive token metadata or be used outside normal troubleshooting.

Mitigation: Reserve token lookup and manual refresh for explicit troubleshooting; use authorized store selection and openId-based business calls for routine workflows.

## Reference(s):

- [TikTok Shop ERP Authorization API Reference](references/api.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-shop-auth)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Token values are masked in normal output; large responses may be persisted to a local LinkFox response directory.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
