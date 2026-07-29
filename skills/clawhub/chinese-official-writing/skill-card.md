## Description: <br>
Drafts, revises, condenses, and reviews Chinese official documents and formal workplace materials, including genre checks, format review, formal tone, and reduced AI-style phrasing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, writers, reviewers, and agent users use this skill to draft or review Chinese notices, requests, reports, plans, meeting minutes, institutional rules, procurement materials, AI-compute service materials, and other formal work documents while preserving provided facts and required document elements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may inspect drafts provided for review or linting, including DOCX files, which can contain sensitive official or workplace information. <br>
Mitigation: Avoid using it on sensitive documents unless agent-side document access is acceptable, and keep confidential drafts within approved handling environments. <br>
Risk: Generated official, legal, procurement, financial, or signing material may still contain factual, policy, or approval errors. <br>
Mitigation: Manually verify facts, dates, amounts, policy references, approval language, and signing authority before official use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing) <br>
- [GitHub repository](https://github.com/gongyu0918-debug/chinese-official-writing-skill) <br>
- [Issues and feedback](https://github.com/gongyu0918-debug/chinese-official-writing-skill/issues) <br>
- [写作流程](references/workflow.md) <br>
- [文种路由](references/genre-routing.md) <br>
- [办理要素](references/handling-elements.md) <br>
- [GB/T 9704-2012 常用格式参考](references/format-gbt9704.md) <br>
- [AI 算力与技术服务材料](references/ai-compute-docs.md) <br>
- [复核清单](references/review-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Plain text or Markdown, with optional shell commands for local prose linting] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce draft text, revised text, review findings, document-structure guidance, or local lint commands depending on the user's task.] <br>

## Skill Version(s): <br>
1.5.28 (source: SKILL.md frontmatter, README.md, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
