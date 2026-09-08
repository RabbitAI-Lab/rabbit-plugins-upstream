## Description:

将模糊意图转换为结构化 Brief、可执行 Prompt 和下游 Skill 路由；适用于网站、海报、PPT、视频、报告、产品方案和研究任务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[taogeo](https://clawhub.ai/user/taogeo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent builders use this skill to turn vague goals into structured briefs, executable prompts, acceptance criteria, and downstream handoff suggestions. It is intended for planning creative, product, research, and content-generation work before another agent or skill executes the task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake draft prompts and routing suggestions for executed downstream work.

Mitigation: Treat outputs as planning artifacts and require a separate user request before any capable host modifies files, calls tools, uploads content, or runs downstream skills.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/taogeo/skills/prompt-compiler)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with structured brief, status labels, executable prompt, acceptance criteria, and routing suggestion]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces draft planning and handoff content only; it does not modify files, call external tools, upload content, or execute downstream skills.]

## Skill Version(s):

0.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
