## Description:

Tencent COS helps agents manage Tencent Cloud COS objects and buckets, run Data Intelligence processing workflows, query MetaInsight datasets and knowledge bases, and generate result previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shawnminh](https://clawhub.ai/user/shawnminh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to work with Tencent Cloud COS storage, Data Intelligence services, MetaInsight search, content processing, and knowledge-base workflows from an agent session. It can guide setup, propose and run shell commands, return structured JSON results, and create local HTML previews for retrieved files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and mutate Tencent Cloud COS and Data Intelligence resources when configured with broad credentials.

Mitigation: Use a least-privilege Tencent Cloud sub-account or short-lived STS credentials scoped to the intended buckets and actions.

Risk: Credential persistence can expose Tencent Cloud secrets if plaintext local environment files are used unnecessarily.

Mitigation: Prefer ephemeral environment variables or STS tokens, avoid plaintext .env persistence unless required, and remove local credential files after use.

Risk: Delete, service enablement, dataset binding, face-search, bulk content reads, and generic ci-request operations can have account, cost, privacy, or data-loss impact.

Mitigation: Keep KIKI=1 where possible and require explicit manual confirmation before running high-impact operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/shawnminh/skills/tencent-cos-skill)
- [COS Node.js SDK Operation Reference](references/api_reference.md)
- [CI Service Status Reference](references/ci-service-status.md)
- [Dataset Search Reference](references/dataset-search.md)
- [Dataset Simple Query Reference](references/dataset-simple-query.md)
- [Dataset Catalog Reference](references/dataset-catalog.md)
- [Bucket Content Aggregation Reference](references/bucket-content-aggregation.md)
- [Search Results Preview Reference](references/search-results-preview.md)
- [Query Spec Schema](references/query-spec.schema.json)
- [Tencent Cloud COS Node.js SDK Documentation](https://cloud.tencent.com/document/product/436/8629)
- [Tencent Cloud Data Intelligence Documentation](https://cloud.tencent.com/document/product/460)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON, HTML files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, structured JSON command output, and optional single-file HTML previews.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Tencent Cloud credentials plus Region and Bucket configuration; supports optional STS token use and strict mode with KIKI=1 to hide or reject delete actions.]

## Skill Version(s):

1.1.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
