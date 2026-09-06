## Description:

Audits a public webpage or website for crawlability, indexing signals, metadata, canonical URLs, headings, structured data, and evidence-backed SEO fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External site owners, SEO practitioners, and developers use this skill to run bounded public-site audits that collect live page evidence and prioritize crawlability, indexing, metadata, structured-data, and on-page SEO fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can submit target URLs and keyword queries to Dataify and can write raw HTML evidence into the output directory.

Mitigation: Use only public sites you are authorized to audit, avoid confidential URLs or sensitive keywords, keep DATAIFY_API_TOKEN in the environment, and review or clean the output directory after use.

Risk: The public-URL boundary is not fully enforced for private, staging, cloud-metadata, or redirected internal targets.

Mitigation: Do not provide localhost, private-network, cloud-metadata, staging, or confidential URLs, and review scope and redirects before increasing page limits.

## Reference(s):

- [Dataify Documentation](https://doc.dataify.com)
- [Dataify Support](https://www.dataify.com/)
- [Five-layer audit framework](references/audit-framework.md)
- [SEO checks](references/checks.md)
- [SEO finding contract](references/output-contract.md)
- [Site-type playbooks](references/site-type-playbooks.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands plus generated report.json, raw HTML evidence, and report.md files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DATAIFY_API_TOKEN in the environment; audit scope is bounded by page limits and output is written to a selected local directory.]

## Skill Version(s):

1.1.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
