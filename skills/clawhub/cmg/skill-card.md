## Description:

CMG helps agents guide cloud migration assessments through resource scanning, Tencent Cloud sizing recommendations, TCO analysis, and migration tool guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[llm-pm](https://clawhub.ai/user/llm-pm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud architects, and migration engineers use this skill to assess source cloud resources, map them to Tencent Cloud offerings, obtain real quoted pricing, generate TCO reports, and identify migration tools for execution planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may handle raw cloud credentials during resource scanning and pricing workflows.

Mitigation: Use least-privilege temporary credentials, avoid pasting secrets into chat, and avoid command-line AK/SK where possible.

Risk: The skill downloads and guides execution of precompiled scanner binaries.

Mitigation: Use the bundled checksum workflow before execution, reject checksum mismatches, and do not use artifacts marked unavailable.

Risk: Recommendation requests can send resource topology and sizing details to a remote MCP server.

Mitigation: Use only a trusted, user-provided HTTPS MCP endpoint and do not fall back to guessed or default server addresses.

Risk: Generated JSON, Excel, HTML, text, and Mermaid outputs can contain confidential infrastructure and cost data.

Mitigation: Treat reports and intermediate files as confidential infrastructure data and store or share them under the user's normal data-handling controls.

Risk: Incorrect or estimated pricing can mislead migration cost decisions.

Mitigation: Use real cloud pricing APIs or official pricing calculators, require price_source values, and fail clearly rather than inventing unavailable prices.

## Reference(s):

- [CMG skill page](https://clawhub.ai/llm-pm/skills/cmg)
- [CMG resource scanning guide](references/scan.md)
- [CMG recommendation guide](references/recommend.md)
- [CMG TCO analysis guide](references/tco.md)
- [CMG migration guidance](references/migrate.md)
- [Product code lookup](references/products.md)
- [Scanner package checksums](references/CHECKSUMS.md)
- [Scanner package base URL](https://msp-release-1258344699.cos.ap-shanghai.myqcloud.com/package/urp/)
- [Tencent Cloud pricing calculator](https://buy.cloud.tencent.com/price)
- [Alibaba Cloud pricing](https://www.aliyun.com/price/product)
- [Huawei Cloud pricing calculator](https://www.huaweicloud.com/pricing/calculator.html)
- [AWS Pricing Calculator](https://calculator.aws/#/addService)
- [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/)
- [Google Cloud pricing calculator](https://cloud.google.com/products/calculator?hl=zh-CN)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, JSON, Files]

**Output Format:** [Markdown guidance with inline shell commands plus generated JSON, Excel, HTML, text, and Mermaid report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce scan workbooks, recommendation JSON, pricing_data.json, TCO Excel/HTML reports, and dependency analysis outputs.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter lists 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
