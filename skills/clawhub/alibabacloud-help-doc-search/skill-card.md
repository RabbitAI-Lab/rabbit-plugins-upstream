## Description:

Searches Alibaba Cloud official help documentation with relevance-ranked results and verifies OpenAPI contract details against public api.aliyun.com metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to retrieve Alibaba Cloud help-center documentation, inspect product catalogs, and verify API parameters, error codes, and RAM permission points before answering configuration, billing, quota, troubleshooting, and API-reference questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The read command can fetch arbitrary URLs, including local file paths, which is broader than the Alibaba Cloud documentation-only behavior described for the skill.

Mitigation: Restrict or review read-command use to Alibaba Cloud documentation URLs before installation or execution in sensitive environments.

Risk: The skill can produce misleading answers if retrieved documentation is stale or if narrative documentation conflicts with OpenAPI metadata.

Mitigation: Use retrieved source URLs in answers, prefer OpenAPI metadata for exact contract details, and flag possibly outdated documentation when freshness is unclear.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sdk-team/skills/alibabacloud-help-doc-search)
- [OpenAPI Metadata Endpoints](references/api-metadata.md)
- [Query Construction Methodology](references/query-construction.md)
- [Search Backend Architecture](references/search-backend.md)
- [RAM Permission Requirements](references/ram-policies.md)
- [Alibaba Cloud Help Center](https://help.aliyun.com)
- [Alibaba Cloud OpenAPI Metadata](https://api.aliyun.com/meta/v1)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or plain text with optional JSON output from helper commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers should cite retrieved source URLs; helper commands use result and line limits for bounded output.]

## Skill Version(s):

0.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
