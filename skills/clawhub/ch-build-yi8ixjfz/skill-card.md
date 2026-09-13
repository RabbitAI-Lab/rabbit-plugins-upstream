## Description:

基于宝洁八大问的行为面试准备技能。通过选择题启发式引导，帮助用户挖掘个人经历、构建STAR故事、模拟面试追问、优化答案表达，最终提升行为面试通过率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[guipi888](https://clawhub.ai/user/guipi888)

### License/Terms of Use:

MIT-0

## Use Case:

External job seekers use this skill to prepare P&G Eight Questions behavioral interviews by mapping experiences to interview prompts, building STAR stories, practicing follow-up questions, and improving answer clarity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found that the skill forces unrelated promotional content and a third-party link into every response.

Mitigation: Review or remove the mandatory promotional footer and third-party link before deployment.

Risk: Broad trigger phrases and optional use of resume or notes context could cause the skill to activate or inspect personal background information outside a clear interview-preparation request.

Mitigation: Narrow activation to explicit P&G Eight Questions or behavioral interview preparation requests, and access resumes or notes only after clear user opt-in.

Risk: Artifact guidance notes that users may over-rely on optimized drafts as memorized templates.

Mitigation: Keep optimized answers framed as reference drafts and prompt users to rewrite them in their own experience and language.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/guipi888/skills/ch-build-yi8ixjfz)
- [八大问题库](artifact/references/八大问题库.md)
- [技能设计](artifact/references/技能设计.md)
- [用户沟通示例](artifact/references/用户沟通示例.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Conversational Markdown with interview prompts, STAR outlines, scoring tables, feedback, and revised answer drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Chinese-language interview preparation guidance, multiple-choice prompts, 1-5 scoring, and practice progress summaries.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
