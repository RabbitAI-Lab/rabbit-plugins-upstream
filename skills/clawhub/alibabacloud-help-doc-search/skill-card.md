## Description:

Search Alibaba Cloud official help documentation with relevance-ranked retrieval and verify OpenAPI contracts, including parameters, error codes, and RAM permission points, against Alibaba Cloud public metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud engineers, and support agents use this skill to find Alibaba Cloud documentation, read official help pages, and verify exact OpenAPI contract details before answering product, troubleshooting, quota, billing, or API-reference questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The document reader can fetch arbitrary URLs even though the skill is intended for Alibaba Cloud documentation endpoints.

Mitigation: Prefer URLs returned by the skill's own search or list commands, avoid private or signed URLs, and use an allowlist for help.aliyun.com, api.aliyun.com, and t.aliyun.com when agents process untrusted links.

## Reference(s):

- [OpenAPI Metadata Endpoints](references/api-metadata.md)
- [Search Backend Architecture](references/search-backend.md)
- [Query Construction Methodology](references/query-construction.md)
- [ECS Documentation Scenario Workflow](references/ecs-scenario-guide.md)
- [Help Center Product Codes](references/product-codes.md)
- [ECS Knowledge FAQ](references/ecs-knowledge-faq.md)
- [RAM Permission Requirements](references/ram-policies.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Guidance]

**Output Format:** [Markdown or plain text with source URLs and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include retrieved Alibaba Cloud help URLs, API metadata summaries, warnings, and suggested follow-up searches.]

## Skill Version(s):

0.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
