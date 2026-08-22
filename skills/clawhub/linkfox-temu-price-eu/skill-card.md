## Description:

Temu 欧洲站商品价格管理 API skill for querying price orders, estimating recommended or base prices, and changing SKU base prices through LinkFox gateway access to Temu Partner EU price interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to manage Temu EU marketplace pricing: query pricing orders, estimate recommended supply or base prices, and prepare or execute SKU base-price updates through LinkFox and Temu Partner EU APIs.

### Deployment Geography for Use:

Global use for Temu EU marketplace pricing workflows

## Known Risks and Mitigations:

Risk: The skill requires LinkFox and Temu credential access and can store Temu access tokens locally.

Mitigation: Use scoped credentials, avoid unmasked token listing, and remove local LinkFox or Temu token files when they are no longer needed.

Risk: The skill can perform live Temu EU SKU price changes.

Mitigation: Review generated price-change payloads, target goods IDs, SKU IDs, amounts, and currencies before executing write operations.

Risk: The skill bundles broad proxy, file-download, onboarding/payment, and automatic local data-storage capabilities.

Mitigation: Install only after reviewing the security summary and keep downloaded files and saved full API responses in controlled workspaces.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-price-eu)
- [API reference](references/api.md)
- [API document index](references/apis/README.md)
- [Temu accessToken authorization](references/access-token.md)
- [Partner EU price catalog](references/partner-eu-catalog.md)
- [Temu Partner EU documentation](https://partner-eu.temu.com/documentation?menu_code=dfff38c23adf498d8a7cd55052bd3648)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and JSON API payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts can write full API responses to local JSON files; large responses may be summarized on stdout.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
