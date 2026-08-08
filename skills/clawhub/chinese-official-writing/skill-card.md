## Description:

Drafts, revises, compresses, and reviews Chinese official documents and formal workplace materials, including requests, reports, notices, plans, meeting minutes, institutional rules, feasibility materials, AI-compute procurement materials, and related style or format checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, writers, reviewers, and agent users use this skill to draft or review Chinese official and formal work documents while preserving document type, administrative relationship, required handling elements, and concise official style. It is also used to reduce AI-like phrasing, check format risks, and prepare AI-compute or procurement-related formal materials from user-provided facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Formal documents can affect administrative, legal, financial, procurement, audit, or signing decisions if inaccurate or unsupported content is accepted.

Mitigation: Require human review before official use, especially for legal, financial, procurement, audit, or final-signature conclusions.

Risk: Drafts or DOCX files may contain sensitive workplace information when users ask the agent or optional lint script to process them.

Mitigation: Use the skill only on documents the user intends the agent to process, and avoid submitting unnecessary confidential content.

Risk: The skill can help polish official tone, but source materials may omit facts needed for a complete or valid formal document.

Mitigation: Keep outputs tied to user-provided facts and verify missing dates, amounts, policy bases, signers, seals, and approval conclusions before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [README](README.md)
- [Workflow](references/workflow.md)
- [Genre routing](references/genre-routing.md)
- [Handling elements](references/handling-elements.md)
- [Review checklist](references/review-checklist.md)
- [Anti-AI patterns](references/anti-ai-patterns.md)
- [GB/T 9704 formatting](references/format-gbt9704.md)
- [AI compute documents](references/ai-compute-docs.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands]

**Output Format:** [Plain text or Markdown, with optional shell commands for local prose linting when the user asks to check a draft file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include drafted formal body text, revised text, review findings, format guidance, or local lint command suggestions; the skill instructs agents not to invent unsupported facts.]

## Skill Version(s):

1.5.39 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
