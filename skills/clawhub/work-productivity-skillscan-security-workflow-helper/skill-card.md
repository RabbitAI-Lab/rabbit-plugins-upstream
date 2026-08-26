## Description:

Helps agent users and skill authors create practical SkillScan-style workflows for fixing bugs, hardening setup and safety, improving reliability, and shaping adjacent skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

AI-agent users, skill authors, maintainers, and teams use this skill to turn security or SkillScan-style workflow needs into practical plans, checklists, analysis, code changes, or decision support. It is intended for local-friendly workflow help rather than cloud-only automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan notes broad trigger wording that may activate the skill for unrelated security or productivity requests.

Mitigation: Review invocation context before using the skill and narrow trigger wording to explicit SkillScan-style workflow or skill-hardening requests in a future release.

Risk: The skill provides workflow and implementation guidance, so incorrect recommendations could be carried into downstream skill or security work.

Mitigation: Review generated plans, checklists, commands, and code changes before applying them, and scan updated skills before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-skillscan-security-workflow-helper)
- [Requirement Plan](references/requirement-plan.md)
- [Skill Vetter demand signal](https://clawhub.ai/skills/skill-vetter)
- [SkillScan demand signal](https://clawhub.ai/skills/skillscan)
- [AdMapix demand signal](https://clawhub.ai/skills/admapix)
- [PollyReach demand signal](https://clawhub.ai/skills/pollyreach)
- [Ask HN security demand signal](https://news.ycombinator.com/item?id=49408476)
- [GitHub workflow issue demand signal](https://github.com/cobuildwithus/murph/issues/2245)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with optional code, shell command, checklist, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include assumptions, limits, validation notes, and remaining risks when relevant.]

## Skill Version(s):

0.20260825.44155 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
