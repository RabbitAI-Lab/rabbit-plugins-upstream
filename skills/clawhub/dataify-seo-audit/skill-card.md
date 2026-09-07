## Description:

Audit a public webpage or website for crawlability, indexing signals, metadata, canonical URLs, headings, structured data, and evidence-backed SEO fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and SEO practitioners use this skill to run bounded technical and on-page SEO audits for public websites they are authorized to assess. It produces evidence-backed findings for crawlability, indexation signals, metadata, headings, structured data, internal discovery, and practical fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports under-scoped URL fetching and recommends use only for public websites the user is authorized to audit.

Mitigation: Limit targets to authorized public HTTP(S) sites, avoid internal or secret-bearing URLs, and review the planned scope before high-volume crawls.

Risk: The security scan notes auxiliary scripts that can mishandle the Dataify API token.

Mitigation: Keep DATAIFY_API_TOKEN in the environment, never paste or print it, rotate it if exposed, and review token-handling behavior before installation.

Risk: Bundled auxiliary scripts are broader than the documented SEO audit workflow.

Mitigation: Prefer the documented SEO audit entrypoint and review any auxiliary script before running it.

## Reference(s):

- [Dataify Documentation](https://doc.dataify.com)
- [Dataify Support](https://www.dataify.com/)
- [Five-layer audit framework](references/audit-framework.md)
- [SEO checks](references/checks.md)
- [SEO finding contract](references/output-contract.md)
- [Site-type playbooks](references/site-type-playbooks.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown report, JSON report, raw evidence files, and concise terminal summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include scope, collection time, prioritized findings, page and SERP evidence, collection failures, and out-of-scope measurements.]

## Skill Version(s):

1.1.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
