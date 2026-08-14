## Description:

Helps agent users and skill maintainers create practical SkillScan-style workflows for bug fixing, setup hardening, safety review, reliability improvements, and adjacent skill development.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

AI-agent users, skill authors, maintainers, and teams use this skill to turn broad SkillScan-style security and productivity needs into actionable workflows, checklists, analyses, code changes, or implementation plans. It is intended for practical local-hardware-friendly support around bug fixing, hardening setup and safety, improving reliability, and creating adjacent skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad implicit activation may route unrelated productivity or security prompts to this skill.

Mitigation: Invoke the skill explicitly for SkillScan-style workflow requests, or narrow trigger terms and implicit-invocation policy before deployment.

Risk: Workflow guidance can be too generic if the user's desired artifact, constraints, or success criteria are underspecified.

Mitigation: State the intended outcome, available inputs, constraints, and validation criteria before relying on the generated workflow or checklist.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-skillscan-security-workflow-helper)
- [SkillScan Demand Signal](https://clawhub.ai/skills/skillscan)
- [Skill Vetter Demand Signal](https://clawhub.ai/skills/skill-vetter)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with optional code blocks, checklists, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are tailored to the user's immediate situation and should surface assumptions, limits, validation steps, and remaining risks.]

## Skill Version(s):

0.20260814.40500 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
