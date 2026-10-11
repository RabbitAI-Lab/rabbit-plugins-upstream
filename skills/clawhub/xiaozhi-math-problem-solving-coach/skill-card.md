## Description:

通过循序追问和分层提示，帮助中国大陆初高中学生解决数学题、订正错误并进行考前梳理。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and educators use this agent for guided, single-question middle- and high-school math tutoring, similar practice problems, and exam review. It prompts students to find their own next step rather than immediately supplying answers.

### Deployment Geography for Use:

China (mainland)

## Known Risks and Mitigations:

Risk: Prior weakness records and wrong-answer summaries can expose student learning data across skills.

Mitigation: Require explicit current-session consent before accessing profiles or sharing summaries; honor pause, delete, export, and stop-sharing requests.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-math-problem-solving-coach)
- [Four-step tutoring workflow](references/photo-4step-statemachine.md)
- [Socratic question guide](references/math-socrates-guide.md)
- [Hint ladder](shared/hint-ladder.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Practice problems]

**Output Format:** [Conversational text or Markdown; optional structured handover data with student consent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to the current session; optional profile access and sharing require explicit consent.]

## Skill Version(s):

2.11.1 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
