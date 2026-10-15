## Description:

Search and analyze patents across major jurisdictions using PatentMax, including patent details, citations, similar documents, and portfolio trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, inventors, patent professionals, and developers use this skill to find and review patents, explore citations and related documents, and summarize company portfolios or technology trends. Search reports are preliminary research, not legal opinions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent queries and technical descriptions are sent to PatentMax and may disclose confidential invention details.

Mitigation: Obtain user approval before sending sensitive material; omit source code, formulas, trade secrets, and unpublished invention details unless disclosure is authorized.

Risk: Trial or API credentials and results may remain in local files or be exposed through shared configuration.

Mitigation: Keep API keys out of shared files and review local ~/.patentmax files when removing cached trial credentials or results.

Risk: Changing the API base URL could send patent queries or credentials to an untrusted service.

Mitigation: Use the official default API endpoint unless the user intentionally trusts another endpoint.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/global-patent-search)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [Search workflow](artifact/references/search-workflow.md)
- [Query syntax](artifact/references/query-syntax.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Markdown patent-search reports and summaries, with optional patent PDFs or drawings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include patent identifiers, source citations, claims analysis, and trend statistics.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
