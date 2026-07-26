## Description: <br>
领星ERP helps agents use Lingxing ERP OpenAPI documentation and CLI scripts to query Amazon, advertising, sales, inventory, finance, FBA, purchase, customer service, logistics, warehouse, and multi-platform ERP data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Lingxing ERP data and run documented OpenAPI calls for ecommerce operations, reporting, inventory, finance, and fulfillment workflows. It is intended for users who already have authorized Lingxing API credentials and need agent-assisted command generation, parameter guidance, and JSON response handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access broad Lingxing ERP data and includes high-impact ERP actions. <br>
Mitigation: Install only when the publisher is trusted, use least-privilege Lingxing API credentials, and avoid invoking write-capable APIs unless the action is explicitly intended. <br>
Risk: Access tokens and full ERP API responses may persist locally. <br>
Mitigation: Store response files outside project repositories, delete saved responses and token cache files after use, and avoid committing ERP data or credentials. <br>
Risk: The server security verdict is suspicious. <br>
Mitigation: Review the security summary and guidance before installation, and limit use to environments where broad Lingxing ERP access is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-lingxing-erp) <br>
- [Publisher profile: linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>
- [Lingxing OpenAPI host](https://openapi.lingxing.com) <br>
- [领星 OpenAPI 调用说明](references/api.md) <br>
- [领星新广告-报告接口参考](references/newad-report.md) <br>
- [领星销售查询接口参考](references/sale-full.md) <br>
- [领星订单 / Listing / 运营操作接口参考](references/sale-ops.md) <br>
- [领星财务接口参考](references/finance.md) <br>
- [领星统计报表接口参考](references/statistics.md) <br>
- [领星仓库接口参考](references/warehouse.md) <br>
- [领星FBA接口参考](references/fba.md) <br>
- [领星多平台 V2 接口参考](references/multiplatform-v2.md) <br>
- [领星多平台广告接口参考](references/multiplatform-ads.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May persist full ERP responses to local files when the response I/O helper is used; users should clean up saved files after use.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
