## Description: <br>
Temu 全球站（非 US/EU）商品管理 Manage Product API，经 LinkFox 网关转发 24 个 bg.local/temu.local 接口，默认 site=global。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and developers use this skill to query and manage Temu Global product catalogs through LinkFox, including listing products, reading details, editing inventory, changing sale status, deleting goods, and downloading signed files. <br>

### Deployment Geography for Use: <br>
Global, for Temu Global workflows outside the US/EU-specific skill paths called out by the documentation. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform live Temu catalog actions, including update, delete, stock, sale-status, compliance, pre-sale, generic proxy, and file-download operations. <br>
Mitigation: Require explicit human confirmation before mutating or downloading data, and verify the target store, site, request type, and parameters before execution. <br>
Risk: Temu access tokens and LinkFox credentials may be stored or exposed through arguments, local token stores, stdout, or saved response files. <br>
Mitigation: Treat tokens like passwords, avoid printing or sharing them, review local linkfox output folders for sensitive data, and rotate credentials if exposure is suspected. <br>
Risk: Broad proxy and file-download helpers can reach many documented Temu operations with less containment than a single-purpose read-only tool. <br>
Mitigation: Limit use to documented product-management workflows from trusted workspaces, prefer specific scripts over the generic proxy, and inspect saved outputs before reuse. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-manage-product-global) <br>
- [API reference](references/api.md) <br>
- [Temu accessToken authorization](references/access-token.md) <br>
- [Partner Global Manage Product catalog](references/partner-global-catalog.md) <br>
- [Per-interface API documents](references/apis/README.md) <br>
- [Temu Partner Global documentation](https://partner-global.temu.com/documentation) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses saved to local files or summarized on stdout.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts write full responses under a local linkfox dated session folder; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
