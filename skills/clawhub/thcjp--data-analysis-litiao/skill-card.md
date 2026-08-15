## Description:

提供数据分析方法论框架，帮助代理在分析前明确决策目标、检查统计严谨性、识别常见分析陷阱并规范输出。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to guide data analysis, reporting, statistical insight, and visualization tasks. It helps select an appropriate method, flag common pitfalls such as p-hacking and Simpson's Paradox, and structure findings with assumptions, uncertainty, and limitations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for broad read, write, and exec tooling even though its primary behavior is Markdown data analysis guidance.

Mitigation: Install it in an agent profile where exec and write access are disabled or require explicit approval, and review proposed commands or file changes before they run.

Risk: Data analysis tasks may involve sensitive or regulated datasets.

Mitigation: Use approved datasets and environments, avoid exposing secrets or personal data in prompts, and apply local data handling controls before using the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/data-analysis-litiao)
- [Artifact homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown guidance with structured checklists and analysis recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports Chinese interaction and may include method-selection advice, statistical checks, limitations, and escalation flags.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence; artifact frontmatter states 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
