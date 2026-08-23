## Description:

Helps AI-agent users, skill authors, maintainers, and teams create SkillScan-style workflows, checklists, analyses, and implementation support for bug fixing, setup hardening, safety, and reliability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

AI-agent users, skill authors, maintainers, and teams use this skill to turn SkillScan-style security and reliability needs into practical plans, checklists, workflows, code changes, and verification notes. It is intended for local-hardware friendly support around bug fixing, setup hardening, safety review, and adjacent workflow creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Overbroad implicit invocation can route unrelated tasks into this workflow helper.

Mitigation: Tighten or disable implicit invocation, and narrow trigger keywords to terms that clearly indicate SkillScan-style security or reliability workflow support.

Risk: Generated workflow guidance can be incomplete or mismatched to a user's actual security requirements.

Mitigation: Review outputs against the stated success criteria, scan any produced skill or code artifacts before deployment, and document assumptions and remaining risks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-skillscan-security-workflow-helper)
- [Requirement Plan](references/requirement-plan.md)
- [Skill Vetter Demand Signal](https://clawhub.ai/skills/skill-vetter)
- [SkillScan Demand Signal](https://clawhub.ai/skills/skillscan)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with optional code blocks, shell commands, checklists, configuration snippets, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assumptions, limits, remaining risks, and follow-up work when relevant.]

## Skill Version(s):

0.20260823.40325 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
