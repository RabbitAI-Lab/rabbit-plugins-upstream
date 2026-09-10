## Description:

Assists agents with drafting, rewriting, condensing, and reviewing Chinese official documents, workplace materials, news drafts, and related formal texts while preserving user-provided facts and document conventions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, and writing-focused agent workflows use this skill to produce or review Chinese official documents and formal workplace materials such as requests, reports, notices, summaries, plans, minutes, speeches, feasibility-review materials, and AI-compute service documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional linter can consume excessive resources when run on untrusted or unusually large txt, md, or docx files.

Mitigation: Run the linter only on trusted, reasonably sized drafts, preferably in an environment with memory and time limits.

Risk: Formal document drafts may contain unsupported or misleading statements if source materials are sparse or ambiguous.

Mitigation: Review generated drafts against the user's supplied facts, dates, amounts, responsible parties, document genre, and approval posture before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [README](README.md)
- [Reference Index](references/reference-index.md)
- [Workflow](references/workflow.md)
- [Document Genre Routing](references/genre-routing.md)
- [Handling Elements](references/handling-elements.md)
- [GB/T 9704 Formatting](references/format-gbt9704.md)
- [Final Review Layers](references/final-review-layers.md)
- [Proofreading Checklist](references/proofreading-checklist.md)
- [AI Compute and Technical Service Materials](references/ai-compute-docs.md)
- [Optional Hook Usage](https://github.com/gongyu0918-debug/chinese-official-writing-skill/blob/main/chinese-official-writing/hooks/README.md)
- [SkillHub Listing](https://skillhub.cn/skills/user_f3d82da7/chinese-official-writing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Plain text or Markdown, with optional shell commands for the linter]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce full formal-document drafts, revised text, concise review findings, formatting guidance, and optional linter commands for txt, md, or docx drafts.]

## Skill Version(s):

1.6.32 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
