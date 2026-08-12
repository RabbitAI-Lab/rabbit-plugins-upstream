## Description:

经 LinkFox 网关调用 Temu Partner Global 电商合规 OpenAPI，帮助代理查询和编辑商品合规模板、标签、资质、实拍图和证书上传相关数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Temu Global sellers, operators, and developers use this skill to guide product compliance API calls for metadata lookup, compliance label retrieval, certificate upload/query, real-image upload, and compliance edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can exercise broad Temu and LinkFox account authority through credentials and a generic proxy beyond the narrow compliance workflow.

Mitigation: Use least-privilege Temu and LinkFox credentials, prefer the specific compliance scripts, and use the generic proxy only when broad API access is intended.

Risk: API responses and saved Temu access tokens may remain on disk after use.

Mitigation: Run in a trusted workspace, protect or override the token store path, and delete generated response files or stored tokens when they are no longer needed.

Risk: Environment variables can redirect gateway calls to unexpected services.

Mitigation: Confirm LINKFOX_TOOL_GATEWAY, TEMU_API_BASE_URL, and STORE_API_BASE_URL point only to trusted LinkFox or Temu endpoints before execution.

Risk: Onboarding, SMS login, and payment/order commands can affect account setup or billing.

Mitigation: Review those commands before running them and execute order or payment actions only after explicit user approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-compliance-global)
- [Gateway and API reference](references/api.md)
- [Partner Global compliance catalog](references/partner-global-catalog.md)
- [Compliance API document index](references/apis/README.md)
- [Temu access token authorization](references/access-token.md)
- [Temu Partner documentation: bg.compliance.edit](https://partner-global.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=a8829c8ede574d9a97cd3cea7c019bc4)
- [Temu Partner documentation: bg.compliance.metadata.get](https://partner-global.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=fd12bdf5cb364366bdef85aad9cd8e48)
- [Temu Partner documentation: bg.goods.compliancelabel.get](https://partner-global.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=c49495eb93904c93b750e9798c95e7db)
- [Temu Partner documentation: certificate upload/query APIs](https://partner-global.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=56de04bcafae45509b21edeab57c9fdb)
- [Temu Partner documentation: image upload recognition](https://partner-global.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=960adb7a9d1f47069cdc0a9abd686dc9)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses saved to disk.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts write full responses under a linkfox session data directory; small responses may also print full JSON, while larger responses print summaries unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
