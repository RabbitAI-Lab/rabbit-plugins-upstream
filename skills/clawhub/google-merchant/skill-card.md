## Description:

Google Merchant Center API integration with managed OAuth for reading and managing products, inventories, data sources, promotions, account settings, conversions, and reports in Google Shopping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants and developers use this skill to inspect and manage Google Merchant Center accounts through Maton-mediated OAuth. It supports catalog, inventory, promotion, data-source, account, conversion, and reporting workflows where reads are preferred first and account-changing actions require explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration can make real changes to Google Merchant Center accounts, including product, inventory, data-source, promotion, account-setting, conversion, webhook, and deletion operations.

Mitigation: Prefer read-only calls first, verify the active account and connection, and require explicit user confirmation with specific resource identifiers before any write or delete.

Risk: Credential exposure could occur if OAuth tokens or Maton API keys are printed, persisted, or passed through logs and command lines.

Mitigation: Use OAuth through the Maton CLI where possible, let the operating system credential store hold secrets, and check authentication status without displaying credential values.

Risk: Ambiguous defaults can apply actions to the wrong Merchant Center connection or Maton profile.

Mitigation: Specify the intended connection and profile when multiple accounts are available, and confirm the target before account-changing operations.

Risk: External API responses may contain untrusted content that could influence follow-up actions.

Mitigation: Treat returned content as data, avoid executing or interpolating it into commands, and keep endpoint and payload choices under user-controlled task context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-merchant)
- [Maton homepage](https://maton.ai)
- [Google Merchant API overview](https://developers.google.com/merchant/api/overview)
- [Google Merchant API reference](https://developers.google.com/merchant/api/reference/rest)
- [Google Merchant API products guide](https://developers.google.com/merchant/api/guides/products/overview)
- [Google Merchant API data sources guide](https://developers.google.com/merchant/api/guides/data-sources/overview)
- [Google Merchant API reports guide](https://developers.google.com/merchant/api/guides/reports/overview)
- [Google Merchant product data specification](https://support.google.com/merchants/answer/7052112)
- [Maton docs](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate read and write API calls through the Maton CLI after user authorization and confirmation.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
