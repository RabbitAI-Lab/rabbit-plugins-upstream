## Description:

Searches Tencent Cloud public documentation through TCCLI portal SearchDocuments and helps agents present returned titles, snippets, URLs, totals, and request IDs without managing cloud resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencent-adm](https://clawhub.ai/user/tencent-adm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and support agents use this skill to search Tencent Cloud product documentation, operation guides, API docs, best practices, and troubleshooting material from an agent workflow. It is for portal information retrieval only and does not operate or manage cloud resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tencent Cloud credentials may be exposed if an agent asks users to share SecretId or SecretKey or runs commands that print credentials.

Mitigation: Prefer OAuth login, do not request SecretId or SecretKey unless the user intentionally chooses that path, and refuse commands that reveal configured credentials.

Risk: Installing or upgrading TCCLI dependencies with pip may change local Python packages.

Mitigation: Install only in an environment where TCCLI and Tencent Cloud authentication are acceptable, and review package updates before use on shared or production machines.

## Reference(s):

- [TCCLI Authentication](references/auth.md)
- [Install TCCLI](references/install.md)
- [portal SearchDocuments API Reference](references/search-documents.md)
- [Tencent Cloud API Key Console](https://console.cloud.tencent.com/cam/capi)
- [Tencent Cloud CLI Installation Documentation](https://cloud.tencent.com/document/product/440/34011)

## Skill Output:

**Output Type(s):** [Shell commands, Markdown, Guidance]

**Output Format:** [Markdown with inline shell commands and returned search-result fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports only data returned by Tencent Cloud, including Total, document fields, and RequestId; asks before fetching additional pages.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
