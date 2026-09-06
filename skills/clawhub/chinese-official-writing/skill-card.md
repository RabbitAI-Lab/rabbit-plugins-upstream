## Description:

Assists agents with drafting, rewriting, compressing, and reviewing Chinese official documents, formal workplace materials, and news-style releases while checking genre, structure, style, and evidence boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, and agents use this skill to produce or review Chinese official documents, institutional materials, news messages, formal reports, requests, notices, meeting minutes, plans, summaries, feasibility materials, and AI-compute related formal text. It is intended to keep generated text aligned with user-provided facts, document genre, official tone, and formatting expectations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional prose linter reads the draft files provided to it and prints local review findings.

Mitigation: Run it only on documents the user has authorized the agent to inspect, especially when drafts contain sensitive official or workplace material.

Risk: Official documents can become misleading if generated text adds unsupported facts, dates, amounts, approvals, or institutional conclusions.

Mitigation: Review final text against the user's source material and keep missing facts as gaps rather than inventing official details.

Risk: Incorrect document genre, addressee relationship, or formal ending can change the intent of an official document.

Mitigation: Check the selected genre, routing relationship, required elements, and final format before using generated text in a formal setting.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [论证链条](references/argument-chains.md)
- [联网搜索与公开来源核验](references/external-research.md)
- [总审层级](references/final-review-layers.md)
- [敬谦称谓和机关用语](references/formal-addressing.md)
- [GB/T 9704-2012 常用格式参考](references/format-gbt9704.md)
- [公文行文用语](references/formulaic-language.md)
- [报告/情况说明 Playbook 与检查项](references/genre-checklist-report.md)
- [文种清单](references/genre-checklist.md)
- [文种与专项 Playbook](references/genre-playbooks.md)
- [文种路由](references/genre-routing.md)
- [办理要素](references/handling-elements.md)
- [信息选择](references/information-selection.md)
- [公文语言风格](references/official-style.md)
- [AI 写稿轻量校对](references/proofreading-checklist.md)
- [复核清单](references/review-checklist.md)
- [写作流程](references/workflow.md)
- [AI 算力与技术服务材料](references/ai-compute-docs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Natural-language text or Markdown, with optional code blocks and shell commands when the task involves local proofreading tools or configuration.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are shaped by the user's requested drafting, rewriting, review, compression, or formatting mode.]

## Skill Version(s):

1.6.28 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
