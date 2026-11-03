## Description:

使用场景: 用户要求在本机分析 CSV、JSON、XLSX、Parquet，运行只读 SQL 或生成本地报告时。

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

适用于需要在本机分析 CSV、JSON、XLSX 或 Parquet 文件的用户；可通过自然语言或只读 SQL 获取结果，并在本机生成 XLSX 或 HTML 报告。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A vulnerable certificate library could expose the platform API key to someone intercepting its connections.

Mitigation: Wait for a publisher release with a patched certificate bundle and refreshed dependency lock and checksums before using the skill.

Risk: Paid operations have per-operation fees, and authorization requests share operation metadata with the platform.

Mitigation: Review the fees and metadata sharing before paid use, and prefer a product-specific API key where available.

Risk: Imported datasets remain on the local machine until deleted.

Mitigation: Delete datasets when they are no longer needed and confirm the Runner reports successful deletion.

## Reference(s):

- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/API-KEY.md)
- [Local usage guide](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/USAGE.md)
- [Privacy and security boundaries](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/SECURITY.md)
- [Billing information](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/BILLING.md)
- [Authorization API specification](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/openapi.json)

## Skill Output:

**Output Type(s):** [Analysis, SQL, Guidance, Local report files]

**Output Format:** [Text, SQL, XLSX, and HTML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis results are bounded; reports are generated locally, and truncation or failures are reported.]

## Skill Version(s):

1.7.1 (source: server-resolved release metadata and packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
