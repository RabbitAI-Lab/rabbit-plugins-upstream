## Description:

技能诊所 helps agents diagnose, create, compare, validate, and maintain skills using modular scoring criteria, precedent research, quality gates, and feedback workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fslong520](https://clawhub.ai/user/fslong520)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this agent to review existing skills, create new skills, research similar skills, run release gates, and turn operational feedback into improvement suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and edit local skill files, so incorrect recommendations or edits could affect skill behavior.

Mitigation: Review proposed edits and run the skill's gate checks before publishing or deploying a changed skill.

Risk: Precedent research can use remote marketplace searches that may expose search terms.

Mitigation: Avoid sensitive private skill names or requirements in remote searches, or limit research to local sources.

Risk: Feedback workflows may store failure context in local feedback logs.

Mitigation: Do not record secrets, credentials, or sensitive project details in feedback entries.

## Reference(s):

- [Skill source](artifact/SKILL.md)
- [Evaluation criteria](artifact/reference/criteria.md)
- [Data source guide](artifact/reference/data-sources.md)
- [Skill IR specification](artifact/reference/skill-ir.md)
- [Theory and practice references](artifact/reference/theory.md)
- [From Procedural Skills to Strategy Genes](https://arxiv.org/abs/2604.15097)
- [Skill 101 article](https://my.feishu.cn/wiki/LWazwBXDUipUZVkYCK2c8JK3nEc)
- [ClawHub skill page](https://clawhub.ai/fslong520/skills/skillclinic)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, structured tables, code or configuration files, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write skill files and local feedback logs when the user asks it to create, edit, validate, or maintain a skill.]

## Skill Version(s):

3.0.0 (source: server release metadata and SKILL.md metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
