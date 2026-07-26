## Description: <br>
Temu全球站-订单 helps agents work with LinkFox and Temu Global order APIs for order lists, details, shipping information, amounts, combined shipments, customization data, and verification uploads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and developers use this skill to query and manage Temu Global order data through LinkFox. It supports order lookup, shipping information, amount queries, combined shipment discovery, customization details, and SN/IMEI verification upload workflows. <br>

### Deployment Geography for Use: <br>
Global, for Temu Global workflows outside the US/EU-specific order skills. <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes broad LinkFox/Temu gateway and credential-handling capabilities beyond the narrow order-management description. <br>
Mitigation: Install only if you trust linkfox-ai and need this gateway; use least-privilege Temu order-shipping tokens and restrict LinkFox API token access. <br>
Risk: Temu access tokens can be saved locally under ~/.linkfox or another configured token-store path. <br>
Mitigation: Avoid saving tokens on shared or synced machines, use a protected TEMU_TOKEN_STORE_PATH when possible, and rotate tokens if exposure is suspected. <br>
Risk: Order responses can contain sensitive customer, shipping, and order data and may be written under ./linkfox. <br>
Mitigation: Treat saved response files as sensitive, keep them out of logs and version control, limit access to the workspace, and delete them when no longer needed. <br>


## Reference(s): <br>
- [API reference](references/api.md) <br>
- [Order API index](references/apis/README.md) <br>
- [Partner Global order catalog](references/partner-global-catalog.md) <br>
- [Access token authorization](references/access-token.md) <br>
- [Temu Partner Global documentation](https://partner-global.temu.com/documentation?menu_code=dbd3d395963a408984b8ae7dbc5f64f9) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-order-global) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON request/response examples; scripts may write JSON response files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses may be written under ./linkfox by the artifact scripts; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
