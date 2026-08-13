## Description:

Helps AI-agent users, skill authors, maintainers, and teams create practical workflows, checklists, analysis, or implementation support for Skill Vetter-style tasks such as fixing bugs, hardening setup and safety, improving reliability, or creating adjacent skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

External AI-agent users, skill authors, maintainers, and teams use this skill to turn Skill Vetter-style demand into actionable local workflows, reusable checklists, planning aids, analysis, code changes, or verification notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad implicit invocation wording may route unrelated tasks through this skill when common terms such as security, github, before, or bug fix appear.

Mitigation: Narrow or disable implicit invocation before deployment, and invoke the skill explicitly for Skill Vetter-style workflow support.

Risk: The skill produces guidance, checklists, code changes, shell commands, or configuration snippets that may be incomplete or incorrect for a specific environment.

Mitigation: Review generated outputs against the stated success criteria and test proposed commands or code changes before applying them to production workflows.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-skill-vetter-workflow-helper)
- [Skill Vetter demand signal](https://clawhub.ai/skills/skill-vetter)
- [SkillScan demand signal](https://clawhub.ai/skills/skillscan)
- [GitHub skill demand signal](https://clawhub.ai/skills/github)
- [Self-improving agent demand signal](https://clawhub.ai/skills/self-improving-agent)
- [Hacker News botnet discussion signal](https://news.ycombinator.com/item?id=49270205)
- [Hacker News agent workflow discussion signal](https://news.ycombinator.com/item?id=49273269)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text with optional code, shell command, checklist, workflow, or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include visible assumptions, limits, validation notes, and remaining risks when helpful.]

## Skill Version(s):

0.20260813.40345 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
