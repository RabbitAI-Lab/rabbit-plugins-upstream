## Description:

Searches and analyzes international patent records, including patent text, citations, legal-status snapshots, and applicant portfolios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, inventors, and patent professionals use the skill to find prior art, inspect individual patents, compare similar inventions, and summarize patent activity by company or technology.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent queries and technical descriptions are sent to the external PatentMax service.

Mitigation: Do not submit unpublished trade secrets unless third-party processing is acceptable.

Risk: API credentials and local task or authentication state may expose sensitive information.

Mitigation: Protect API keys and the ~/.patentmax directory; keep real credentials out of shared logs and configuration files.

Risk: Patent coverage and legal-status snapshots may be incomplete or outdated.

Mitigation: Verify consequential legal-status conclusions against official patent registers and identify unsearched sources.

## Reference(s):

- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [PatentMax API reference](artifact/references/api-reference.md)
- [Patent search workflow](artifact/references/search-workflow.md)
- [Patent query construction](artifact/references/query-construction.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown patent-search results and analysis, with citations and optional command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Patent coverage and legal-status information may require verification against official registers.]

## Skill Version(s):

1.1.2 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
