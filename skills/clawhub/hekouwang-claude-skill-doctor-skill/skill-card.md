## Description: <br>
Audits Claude or Agent Skill directories for SKILL.md trigger quality, size, progressive disclosure, externalized scripts, portability, and hardcoded secret risks, then produces a prioritized scorecard and repair guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huiyonghkw](https://clawhub.ai/user/huiyonghkw) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and skill authors use this skill to inspect Claude or Agent Skill packages, produce local text or JSON audit reports, and decide which SKILL.md structure, trigger, portability, and safety issues to fix first. It can also propose or perform skill refactors after the user approves the target path and intended edits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can suggest or carry out rewrites of a target skill directory. <br>
Mitigation: Approve rewrite steps only after confirming the exact target path and intended edits. <br>
Risk: Optional SkillSpector, Docker, and CI commands may run external tools or containerized workflows. <br>
Mitigation: Review those commands before execution and run them only against skill directories intended for inspection. <br>
Risk: Audit recommendations could be incorrect or overly broad if treated as final decisions. <br>
Mitigation: Use the report as review guidance and verify proposed changes before deployment. <br>


## Reference(s): <br>
- [Skill writing vocabulary and advanced review criteria](references/skill-writing-vocab.md) <br>
- [NVIDIA SkillSpector](https://github.com/NVIDIA/skillspector) <br>
- [ClawHub release page](https://clawhub.ai/huiyonghkw/skills/hekouwang-claude-skill-doctor-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain-text audit report, optional JSON report, and proposed edits or commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports prioritize findings and may include rewrite recommendations; any file-changing rewrite step requires user approval.] <br>

## Skill Version(s): <br>
1.3.0 (source: frontmatter, changelog, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
