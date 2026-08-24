## Description:

Helps AI-agent users, skill authors, maintainers, and teams create practical SkillScan-style workflows for bug fixes, security hardening, reliability improvements, and adjacent skill development.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, maintainers, and teams use this skill to turn SkillScan-style security or reliability requests into local-friendly plans, checklists, implementation artifacts, and validation notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger wording may cause the skill to activate in situations where a narrower security workflow helper was not intended.

Mitigation: Invoke the skill explicitly by name or narrow trigger keywords before deployment; review outputs before applying them.

Risk: Documentation workflow outputs may include incorrect or incomplete security or reliability guidance if the input context is thin.

Mitigation: Validate recommendations against the stated success criteria and run the relevant scan or review before deploying any generated changes.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Release Page](https://clawhub.ai/kyro-ma/skills/work-productivity-skillscan-security-workflow-helper)
- [Skill Vetter Demand Signal](https://clawhub.ai/skills/skill-vetter)
- [SkillScan Demand Signal](https://clawhub.ai/skills/skillscan)
- [AdMapix Demand Signal](https://clawhub.ai/skills/admapix)
- [PollyReach Demand Signal](https://clawhub.ai/skills/pollyreach)
- [Local Deployment Discussion](https://www.v2ex.com/t/1236723)
- [Full-Stack Security Discussion](https://news.ycombinator.com/item?id=49408476)
- [Device Connection History Issue](https://github.com/barry-ran/QuickDesk/issues/18)
- [Gate Reserved Pods Validation Issue](https://github.com/kubernetes-sigs/kueue/issues/14763)
- [MSVC Runtime Conflict Issue](https://github.com/jim-easterbrook/python-exiv2/issues/68)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, optionally with code blocks, shell commands, configuration snippets, and checklist items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a verification note and remaining risks or follow-up work.]

## Skill Version(s):

0.20260824.40429 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
