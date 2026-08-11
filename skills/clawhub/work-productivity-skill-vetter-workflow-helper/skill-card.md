## Description:

Helps AI-agent users, skill authors, maintainers, and teams create practical workflows, artifacts, checklists, analysis, or implementation support for Skill Vetter-style work such as fixing bugs, hardening setup and safety, improving reliability, or creating adjacent skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

AI-agent users, skill authors, maintainers, and teams use this skill to turn Skill Vetter-style needs into a practical local workflow, checklist, analysis, code change, or decision aid. It is intended for work-productivity tasks where the user needs visible assumptions, constraints, validation notes, and actionable next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger terms and implicit invocation may activate the skill during unrelated security, GitHub, or bug-fix work.

Mitigation: Prefer explicit invocation by skill name and narrow the trigger metadata if accidental activation would disrupt the user's workflow.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [Work Productivity Skill Vetter Workflow Helper](https://clawhub.ai/kyro-ma/skills/work-productivity-skill-vetter-workflow-helper)
- [Self-improving Agent demand signal](https://clawhub.ai/skills/self-improving-agent)
- [Skill Vetter demand signal](https://clawhub.ai/skills/skill-vetter)
- [GitHub skill demand signal](https://clawhub.ai/skills/github)
- [SkillScan demand signal](https://clawhub.ai/skills/skillscan)
- [Ask HN demand signal](https://news.ycombinator.com/item?id=49235224)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise prose, checklists, code blocks, shell commands, or configuration snippets as appropriate to the user request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include assumptions, limits, validation notes, and remaining risks when helpful.]

## Skill Version(s):

0.20260811.40534 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
