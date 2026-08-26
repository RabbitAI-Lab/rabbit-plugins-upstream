## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核；用户要求写申请、请示、报告、通知、通告、意见、决定、决议、议案、公报、命令、函、复函、批复、说明、方案、纪要、公告、公示、通报、制度、规定、办法、管理办法、细则、操作规程、工作要点、总结、调研、讲话、致辞、可研、审查材料、AI 算力等正式文本，或需校验这类材料的文种、格式、去口语化、降 AI 味时使用；适用于机关、企事业单位、学校、新闻机构。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, writers, editors, and institutional staff use this skill to draft, revise, condense, and review Chinese official documents, formal workplace materials, and news-style institutional copy. It helps check document genre, format, official tone, factual boundaries, and AI-like phrasing while keeping outputs grounded in user-provided materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Official-document drafts can be misleading if source materials are incomplete, outdated, or factually wrong.

Mitigation: Review outputs against the user-provided materials and authoritative sources before use, especially for dates, amounts, policies, decisions, and institutional names.

Risk: Generated format, tone, or document genre may not match a local institution's required template or approval process.

Mitigation: Verify document genre, routing, addressee, closing language, layout, and required formal elements before formal submission.

Risk: The optional prose checker can surface language, structure, and formatting signals, but it does not validate facts or official authorization.

Mitigation: Treat checker output as a review aid and keep final factual, legal, and institutional approval with a qualified human reviewer.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [workflow.md](references/workflow.md)
- [information-selection.md](references/information-selection.md)
- [genre-routing.md](references/genre-routing.md)
- [handling-elements.md](references/handling-elements.md)
- [argument-chains.md](references/argument-chains.md)
- [official-style.md](references/official-style.md)
- [anti-ai-patterns.md](references/anti-ai-patterns.md)
- [final-review-layers.md](references/final-review-layers.md)
- [review-checklist.md](references/review-checklist.md)
- [format-gbt9704.md](references/format-gbt9704.md)
- [genre-playbooks.md](references/genre-playbooks.md)
- [genre-checklist.md](references/genre-checklist.md)
- [ai-compute-docs.md](references/ai-compute-docs.md)
- [external-research.md](references/external-research.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown prose, with optional review comments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces drafted text, revised text, condensed text, or issue-location review guidance; public-source checks are limited to user-requested or time-sensitive cases.]

## Skill Version(s):

1.6.17 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
