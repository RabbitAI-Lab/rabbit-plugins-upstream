## Description:

面向初中至高中必修起点的化学题，以定物质、三重表征、写式列式和守恒检验四步引导学生独立解题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

简体中文环境中的中国大陆初高中学生用它练习具体化学题，包括物质推断、化学方程式和溶液计算。它默认只辅导当前题目；档案读取、错题交接和提醒须分别获得明确同意。

### Deployment Geography for Use:

Mainland China (Simplified Chinese K12); localize curriculum, crisis contacts and consent rules before use elsewhere.

## Known Risks and Mitigations:

Risk: Chemistry explanations or calculations may be inaccurate or inappropriate for the student's level.

Mitigation: Check equations, conservation and worked steps against the question; keep instruction within the documented curriculum scope.

Risk: Optional profile memory, wrong-answer sharing or reminders may expose a minor's learning data without valid consent.

Mitigation: Keep these functions off by default; enforce separate student and, where required, guardian consent and field-level access controls in the host platform.

Risk: Crisis support contacts and consent requirements may be unsuitable outside mainland China.

Mitigation: Localize the curriculum, crisis contacts and consent rules before deployment elsewhere; direct students in danger to appropriate local human help.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-chemistry-problem-coach)
- [Chemistry four-step guide](references/chemistry-4step-guide.md)
- [Hint ladder](shared/hint-ladder.md)
- [Laboratory safety](shared/lab-safety.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Conversational text or Markdown with stepwise hints, equations and checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional wrong-answer handoff or reminder guidance only after separate consent; no persistent profile by default.]

## Skill Version(s):

2.4.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
