## Description:

Temu欧洲站-税务 helps agents call seven LinkFox-forwarded Temu Partner EU Tax APIs for export reports, Galerie signatures, invoice queries and downloads, merchant report downloads, and invoice uploads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and agent workflows use this skill to work with Temu EU tax/VAT records, invoices, reports, and upload/download flows through LinkFox.

### Deployment Geography for Use:

Europe for Temu Partner EU tax workflows

## Known Risks and Mitigations:

Risk: Temu merchant tokens and EU tax/invoice data are handled through the LinkFox gateway.

Mitigation: Use the skill only in trusted LinkFox contexts and keep LINKFOXAGENT_API_KEY and Temu access tokens scoped, rotated, and out of chat transcripts and logs.

Risk: Temu access tokens can be stored locally in ~/.linkfox/temu-access-tokens.json.

Mitigation: Prefer direct per-run accessToken input for sensitive tasks, or restrict local file permissions and remove saved tokens when they are no longer needed.

Risk: Full API responses are persisted under a linkfox/ session data directory and may contain EU tax or invoice data.

Mitigation: Treat generated linkfox/ data files as sensitive records; redact, restrict access, and delete them according to retention requirements.

Risk: Environment URL overrides can redirect gateway requests away from the default LinkFox endpoint.

Mitigation: Use the default gateway in normal operation and set LINKFOX_TOOL_GATEWAY, TEMU_API_BASE_URL, or STORE_API_BASE_URL only for deliberate testing with trusted endpoints.

Risk: Generic proxy and file-download helpers accept broader request shapes than the seven dedicated tax commands.

Mitigation: Prefer the dedicated eu_tax_* scripts for normal tax workflows and review generic proxy or file-download calls before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-tax-eu)
- [API reference](references/api.md)
- [Temu access token guide](references/access-token.md)
- [Partner EU Tax catalog](references/partner-eu-catalog.md)
- [Tax API document index](references/apis/README.md)
- [Apply export report API](https://partner-eu.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896&sub_menu_code=6494bb7afd8048d380a13e92f6275d17)
- [Get Galerie signature API](https://partner-eu.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896&sub_menu_code=d6147c0484a341c49790b6dfed7da275)
- [Invoice detail query API](https://partner-eu.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896&sub_menu_code=3985fe93bff5437c87863a22112b72db)
- [Invoice info query API](https://partner-eu.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896&sub_menu_code=5f5d1168742b4991a86684cbd0c21489)
- [Invoice PDF download API](https://partner-eu.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896&sub_menu_code=2b8a5a8a75604779b2e0017ee79b462a)
- [Merchant report download API](https://partner-eu.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896&sub_menu_code=cc87994f2ac24fc88795f2a3a8844683)
- [Merchant invoice upload API](https://partner-eu.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896&sub_menu_code=98fcf420ee5c4f0d8c8f708adfd89160)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands and JSON request/response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts persist full gateway responses to a linkfox/ session data directory and summarize large responses unless --inline is used.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
