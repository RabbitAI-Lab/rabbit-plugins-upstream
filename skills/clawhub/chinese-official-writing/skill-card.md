## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核；用户要求写申请、请示、报告、通知、通告、意见、决定、决议、议案、公报、命令、函、复函、批复、说明、方案、纪要、公告、公示、通报、制度、规定、办法、管理办法、细则、操作规程、工作要点、总结、调研、讲话、致辞、可研、审查材料、AI 算力等正式文本，或需校验这类材料的文种、格式、去口语化、降 AI 味时使用；适用于机关、企事业单位、学校、新闻机构。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, and communications or administrative staff use this skill to draft, revise, shorten, format, and review Chinese official documents, workplace materials, and news-style organizational copy. It is suited to Chinese public-agency, enterprise, school, and news-organization writing workflows that need genre routing, formal tone, fact-bound drafting, and document review guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Formal documents can become misleading if the agent adds unsupported facts, policies, amounts, dates, responsible parties, or approval conclusions.

Mitigation: Keep drafting grounded in user-provided materials and use public-source verification only when the user requests it or when current facts are required.

Risk: The optional prose_lint.py script reads draft files passed to it, including .txt, .md, and .docx inputs.

Mitigation: Run the script locally only on intended draft files and avoid passing sensitive documents unless local processing is approved for the deployment.

Risk: Lint findings are heuristic review cues and do not replace document-owner review of facts, authority, document type, or final approval requirements.

Mitigation: Use lint output as a prompt for human review, then validate genre, facts, citations, formatting, and approval-sensitive language before release.

## Reference(s):

- [Writing Workflow](references/workflow.md)
- [Genre Routing](references/genre-routing.md)
- [Handling Elements](references/handling-elements.md)
- [Information Selection](references/information-selection.md)
- [Argument Chains](references/argument-chains.md)
- [Official Style](references/official-style.md)
- [Final Review Layers](references/final-review-layers.md)
- [Review Checklist](references/review-checklist.md)
- [GB/T 9704-2012 Format Reference](references/format-gbt9704.md)
- [AI Compute and Technical Service Materials](references/ai-compute-docs.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Plain text or Markdown drafts, review notes, and optional command-line lint findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The optional lint script can emit plain text findings or JSON findings.]

## Skill Version(s):

1.6.20 (source: SKILL.md metadata and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
