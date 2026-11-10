## Description:

Helps agents draft, revise, and check Chinese documents and articles while preserving source traceability, uncertainty, and an auditable change record.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language writers and editors use the skill to draft or revise reports, guides, emails, and articles from supplied material, or to inspect documents for readability, source traceability, and numerical consistency.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The document checker may produce incorrect errors that could block delivery.

Mitigation: Treat checker findings as review prompts, confirm flagged numbers against source material, and use human review when a result appears incorrect; do not make the checker the sole delivery gate.

## Reference(s):

- [Product site and examples](https://huiyonghkw.github.io/hekouwang-writer-skill/)
- [ClawHub release](https://clawhub.ai/huiyonghkw/skills/hekouwang-writer-skill)
- [Document writing workflow](references/write-flow.md)
- [Evidence and delivery guidance](references/evidence-and-delivery.md)
- [Article writing guidance](references/article-writing.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Shell commands]

**Output Format:** [Chinese prose and Markdown documents, with structured review notes and checker reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the request. Checker scripts report findings and do not rewrite documents.]

## Skill Version(s):

1.6.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
