## Description:

简历优化两步走编排器：第一步调用 resume-assistant 按 JD 重组内容并量化成果，第二步调用 humanizer 去除 AI 写作痕迹。解决直连 AI 重写导致的「空洞修饰词+千篇一律句式」问题，产出既专业又像本人写的简历。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bettermen](https://clawhub.ai/user/bettermen)

### License/Terms of Use:

MIT-0

## Use Case:

求职者、跳槽者和应届毕业生使用该 skill 将简历素材和可选 JD 编排给 resume-assistant 和 humanizer，生成量化、贴合岗位且更自然的可投递 Markdown 简历。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generated resume may contain placeholders such as [待补充] or missing contact details.

Mitigation: Review the final resume carefully and fill every placeholder before using it for job applications.

Risk: Resume materials can include sensitive personal or employment information that will be passed to dependent resume-writing skills.

Mitigation: Provide only details you are comfortable sharing with the dependent resume-assistant and humanizer skills.

Risk: Dependent skills may alter facts or numbers during rewriting.

Mitigation: Compare the final Markdown against the source material and confirm all dates, numbers, project names, technologies, and contact details before submission.

## Reference(s):

- [场景 #18 · 简历优化 — 两步走消除 AI 味](references/scene-18-overview.md)
- [Before/After 写法对比](references/before-after-examples.md)
- [ClawHub skill page](https://clawhub.ai/bettermen/skills/resume-optimizer)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown resume content with a placeholder checklist and concise next-step guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May coordinate dependent skills to produce Markdown resume files under resume-output/.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
