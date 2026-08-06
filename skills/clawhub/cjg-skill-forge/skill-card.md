## Description: <br>
Skill Forge helps WorkBuddy users create, improve, review, and consolidate agent skills through structured forge, review, recast, and clarity workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[j-levee](https://clawhub.ai/user/j-levee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, skill authors, and agent operators use this skill to design new skills, audit existing skills with a rubric, consolidate overlapping local skills, and prepare releases with validation and review steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may observe usage patterns, write local signal logs, and anonymously upload feedback to configured cloud endpoints unless the user opts out. <br>
Mitigation: Review the packaged cloud_config.json endpoints before installation and opt out of cloud upload or local logging when those feedback flows are not acceptable. <br>
Risk: Registration, proposal review, and publishing workflows rely on local creator credentials or platform tokens. <br>
Mitigation: Use your own email and credentials, keep creator tokens local, and confirm which local credential files or platform logins will be used before running registration or publishing commands. <br>
Risk: Semantic scan mode may send local skill metadata to an embedding provider. <br>
Mitigation: Avoid semantic scan mode unless sending that metadata to the configured provider is acceptable for the skill being analyzed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/j-levee/skills/cjg-skill-forge) <br>
- [Skill review rubric](references/skill-review-rubric.md) <br>
- [Quality iteration playbook](references/quality-iteration-playbook.md) <br>
- [Coverage audit and real-material ID extraction](references/coverage-audit.md) <br>
- [Feedback loop](references/feedback-loop.md) <br>
- [Skill consolidation](references/skill-consolidation.md) <br>
- [Cloud configuration schema](references/cloud-config-schema.md) <br>
- [Simulation testing](references/simulation-testing.md) <br>
- [Project governance](references/project-governance.md) <br>
- [Clarity fidelity template](references/clarity-fidelity-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Analysis] <br>
**Output Format:** [Markdown guidance with command examples, generated skill files, configuration snippets, and local analysis reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local reports, proposed skill changes, release checks, registration commands, and publishing commands.] <br>

## Skill Version(s): <br>
2.9.7 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
