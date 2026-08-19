## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核，并帮助校验文种、格式、去口语化和降 AI 味。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees and professional writers use this skill to draft, revise, compress, and review Chinese official documents, formal workplace materials, and news-style releases. It is intended for organizations such as public agencies, enterprises, schools, and news organizations that need formal Chinese document structure, tone, and review guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process sensitive Chinese official or formal drafts, including DOCX comments and headers, when asked to review files.

Mitigation: Only provide drafts the user is authorized to process with an agent, and redact confidential content, comments, and headers when needed.

Risk: Time-sensitive facts, policies, or current data can become stale if not explicitly verified.

Mitigation: Request public-source verification for current or latest facts and keep source notes separate from the formal document body.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [workflow.md](references/workflow.md)
- [genre-routing.md](references/genre-routing.md)
- [handling-elements.md](references/handling-elements.md)
- [review-checklist.md](references/review-checklist.md)
- [format-gbt9704.md](references/format-gbt9704.md)
- [prose_lint.py](scripts/prose_lint.py)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown, depending on the requested document or review mode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include drafted or revised Chinese formal text, review findings, formatting guidance, or concise revision notes.]

## Skill Version(s):

1.6.10 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
