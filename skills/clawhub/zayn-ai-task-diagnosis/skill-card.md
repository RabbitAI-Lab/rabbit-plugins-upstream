## Description:

在用户准备创建 Skill、自动化、程序工具、工作流或 AI 助手前，通过目标、变化频率、数据证据和最终责任四问诊断真实需求；跨岗位判断应采用普通对话、Skill、定时或条件自动化、程序、模板、人工、人机协作或暂时不做，并优先给出低成本最小版本。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zaynpeng](https://clawhub.ai/user/zaynpeng)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this Chinese-language skill before creating an AI assistant, workflow, automation, program, template, or Skill to diagnose the real goal, evidence, change frequency, and human responsibility. It helps choose a low-cost minimum path such as ordinary conversation, a Skill, timed or conditional automation, a program, a template/SOP, human handling, human-AI collaboration, or doing nothing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can influence whether users automate high-risk work such as finance, legal, HR, customer-facing communication, privacy, security, public posting, deletion, or irreversible actions.

Mitigation: Keep the skill's required human approval points and confirm applicable compliance rules before applying its recommendations.

Risk: Recommendations may be incomplete when the task, evidence, frequency, or responsible human owner is unclear.

Mitigation: Use the parameter status table and ask the most important missing questions before issuing a formal recommendation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-ai-task-diagnosis)
- [Skill definition](artifact/SKILL.md)
- [README](artifact/README.md)
- [Risk levels](artifact/config/risk-levels.md)
- [Solution types](artifact/config/solution-types.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown task-diagnosis report with a parameter status table, four-question analysis, risk notes, recommendation, and minimum viable version.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language output that separates confirmed facts, grounded judgments, open questions, and AI assumptions.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
