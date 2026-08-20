## Description:

Provides agents with LinkFox-mediated Temu Global order-management commands and references for nine bg.order.*, temu.order.*, and temu.local.order.* APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators managing Temu Global shops use this skill to query order lists, order details, shipping information, decrypted shipping data, order amounts, combined-shipment candidates, customization content, and verification uploads through LinkFox gateway scripts.

### Deployment Geography for Use:

Global, excluding the separate US and EU Temu order sites

## Known Risks and Mitigations:

Risk: The skill includes broad Temu proxy and signed-file download capabilities that go beyond the narrow order API list.

Mitigation: Review the requested API type or file URL before execution and require explicit user confirmation before generic proxy calls or signed-file downloads.

Risk: The skill handles LinkFox credentials, Temu access tokens, and optional local token storage.

Mitigation: Use least-privilege LinkFox and Temu credentials, protect local machines and backups, and avoid storing raw tokens unless local storage is secured.

Risk: Order and shipping workflows can return sensitive recipient data and save full response archives locally.

Mitigation: Query only the required orders, avoid exposing full responses unnecessarily, and delete saved response archives when they are no longer needed.

Risk: Onboarding and billing helpers can involve SMS-code handling and payment QR creation.

Mitigation: Require explicit user confirmation before onboarding, SMS-code handling, or payment QR creation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-order-global)
- [Temu Global order API reference](artifact/references/api.md)
- [Partner Global order catalog](artifact/references/partner-global-catalog.md)
- [Order API documents index](artifact/references/apis/README.md)
- [Temu accessToken authorization](artifact/references/access-token.md)
- [Temu Partner Global documentation](https://partner-global.temu.com/documentation?menu_code=dbd3d395963a408984b8ae7dbc5f64f9)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, JSON files, guidance]

**Output Format:** [Markdown guidance with inline shell commands; Python scripts emit JSON responses and may save full response JSON files locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires LinkFox API credentials and either a Temu accessToken or a saved storeKey; large responses may be summarized in stdout.]

## Skill Version(s):

1.0.6 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
