## Description:

Supports Temu Global, excluding US and EU regions, product management by routing 24 Manage Product APIs through the LinkFox gateway with default site=global.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to query, update, delete, publish, unpublish, and adjust inventory for Temu Global product listings through LinkFox-mediated Temu APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can exercise live LinkFox and Temu account authority, including product deletion, stock edits, and status changes.

Mitigation: Use least-privilege LinkFox and Temu tokens and require explicit review before executing delete, stock, publish, unpublish, or status-changing actions.

Risk: Generic proxy scripts can forward broad Temu API requests beyond a narrowly named helper script.

Mitigation: Prefer the specific product-management scripts and use generic proxy scripts only when the target API type and parameters have been reviewed.

Risk: The skill can store Temu access tokens and save full API responses locally, which may contain sensitive account or business data.

Mitigation: Protect the local token store and saved response directories, avoid sharing generated files, and delete stored tokens or response files when they are no longer needed.

Risk: The security verdict is suspicious because the skill combines credential, payment, persistence, and gateway capabilities.

Mitigation: Install only after confirming trust in LinkFox and validating that the account permissions and data-retention behavior match the deployment's risk tolerance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-manage-product-global)
- [API reference](references/api.md)
- [Partner Global catalog](references/partner-global-catalog.md)
- [Per-interface API docs](references/apis/README.md)
- [Access token guide](references/access-token.md)
- [Temu Partner Global documentation](https://partner-global.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=2a343c65a03d42d380e9ad835aa7b54b)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON files]

**Output Format:** [Markdown guidance with inline shell commands; scripts emit JSON responses and saved JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Small API responses are printed to stdout; larger responses are summarized while full responses are saved under a local linkfox session data directory.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
