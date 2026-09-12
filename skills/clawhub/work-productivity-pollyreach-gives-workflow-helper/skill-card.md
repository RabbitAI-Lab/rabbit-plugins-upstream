## Description:

Helps agent users, skill authors, maintainers, and teams create practical PollyReach-style workflows for bug fixing, setup hardening, reliability improvements, and adjacent skill development.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

AI-agent users, skill authors, maintainers, and teams use this skill to turn demand for PollyReach-style work-productivity workflows into actionable plans, checklists, analyses, code changes, or implementation support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger keywords such as phone, number, things, and done could activate the skill in unrelated conversations when implicit invocation is enabled.

Mitigation: Review and narrow trigger keywords before enabling implicit invocation, or require explicit invocation for deployments where accidental activation would be disruptive.

Risk: Workflow, checklist, code, or configuration suggestions may be incorrect or incomplete for a user's specific environment.

Mitigation: Validate outputs against the stated success criteria and review generated changes before deployment.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-pollyreach-gives-workflow-helper)
- [SkillScan demand signal](https://clawhub.ai/skills/skillscan)
- [PollyReach demand signal](https://clawhub.ai/skills/pollyreach)
- [Beacon job priority issue](https://github.com/NSWSESMembers/Lighthouse/issues/430)
- [Ask HN: How have interviews changed over the last year?](https://news.ycombinator.com/item?id=49578420)
- [Ask HN: Do you route only certain websites through a VPN?](https://news.ycombinator.com/item?id=49583757)
- [Ask HN: Are we normalizing surveillance in the name of safety?](https://news.ycombinator.com/item?id=49586069)
- [Cutting Claude Code token spend on dynamic workflows 80%](https://news.ycombinator.com/item?id=49587379)
- [Ask HN: Connecting Kubernetes dependencies to application telemetry](https://news.ycombinator.com/item?id=49588372)
- [How do you filter noise from signal in programming resources?](https://news.ycombinator.com/item?id=49580521)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with optional code, shell command, checklist, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assumptions, validation notes, remaining risks, or follow-up work when useful.]

## Skill Version(s):

0.20260907.40414 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
