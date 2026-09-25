## Description:

Audits markdown knowledge bases for broken links, missing frontmatter, tag inconsistencies, orphaned files, and coverage gaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fortunto2](https://clawhub.ai/user/fortunto2)

### License/Terms of Use:

MIT

## Use Case:

Developers, maintainers, and content teams use this skill to assess markdown knowledge bases for metadata, link integrity, tagging, orphaned content, and coverage issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run a repository-provided link-checking script during an audit.

Mitigation: Inspect any project-provided link-checking script before execution and require explicit approval in untrusted or shared repositories.

Risk: Audit findings can be incomplete or misleading if inferred frontmatter schemas or tag conventions do not match the knowledge base owner's expectations.

Mitigation: Review the report against the repository's documented content standards before making bulk metadata or tag changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fortunto2/skills/solo-audit)
- [Publisher profile](https://clawhub.ai/user/fortunto2)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown audit report with tables and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include counts, file paths, issue tables, broken-link lists, tag summaries, orphaned files, and prioritized recommendations.]

## Skill Version(s):

1.4.1 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
