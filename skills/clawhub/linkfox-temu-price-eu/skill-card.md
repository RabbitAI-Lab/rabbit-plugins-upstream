## Description: <br>
Temu 欧洲站商品价格管理 API，经 LinkFox 网关转发 Partner EU 价格接口，支持定价单查询、批量修改 SKU 基础价、推荐供货价查询和基础价估算。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and marketplace operators use this skill to manage Temu EU pricing through LinkFox gateway scripts, including price-order lookup, recommended-price checks, base-price estimation, and controlled SKU base-price changes. <br>

### Deployment Geography for Use: <br>
Europe (Temu EU and Partner EU workflows) <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires LinkFox and Temu seller credentials. <br>
Mitigation: Use store keys and environment variables carefully, avoid printing raw tokens, keep token files in protected paths, and rotate or revoke credentials when access is no longer needed. <br>
Risk: The skill can change live Temu EU SKU prices. <br>
Mitigation: Require explicit user confirmation before batch price-change operations and review the exact goodsId, skuId, amount, and currency values before execution. <br>
Risk: The skill archives full API responses and optional Temu access tokens to local disk. <br>
Mitigation: Review saved files under the LinkFox output and token paths, avoid storing sensitive results in shared workspaces, and delete local artifacts that are no longer needed. <br>
Risk: Generic Temu proxy and file-download scripts can be used beyond the narrow EU pricing workflow. <br>
Mitigation: Restrict use to intended Temu EU pricing tasks and review requested API type or download URL before running generic proxy actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-price-eu) <br>
- [API reference](references/api.md) <br>
- [Temu accessToken authorization](references/access-token.md) <br>
- [Temu authorization flow](references/authorization-flow.md) <br>
- [Partner EU Price interface catalog](references/partner-eu-catalog.md) <br>
- [Price API document index](references/apis/README.md) <br>
- [Temu Partner EU documentation](https://partner-eu.temu.com/documentation?menu_code=dfff38c23adf498d8a7cd55052bd3648) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON request/response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts write full API responses to local LinkFox output paths and may print concise summaries for large responses.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
