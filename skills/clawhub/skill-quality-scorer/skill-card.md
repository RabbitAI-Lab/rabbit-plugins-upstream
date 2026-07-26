## Description: <br>
Deterministic TRACE+ quality scorer for Agent Skill packages that audits SKILL.md directories across six dimensions and returns JSON plus Markdown findings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chris1wang3](https://clawhub.ai/user/chris1wang3) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill publishers use this skill to score, audit, compare, or batch-review Agent Skill packages before publication or iteration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Batch mode can read SKILL.md files and related references or scripts under each target directory. <br>
Mitigation: Point the skill only at directories intended for review, especially when working with private or sensitive skill packages. <br>
Risk: Quality scores and recommendations can influence publication or remediation decisions. <br>
Mitigation: Review the generated JSON and Markdown findings before relying on them for release decisions. <br>


## Reference(s): <br>
- [Skill Quality Scorer on ClawHub](https://clawhub.ai/chris1wang3/skills/skill-quality-scorer) <br>
- [Deterministic Scoring Engine](references/scoring-engine-deterministic.md) <br>
- [Audit Playbook](references/audit-playbook.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [JSON and Markdown with scoring tables and findings] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May run a local read-only static audit script before producing the skill-quality report.] <br>

## Skill Version(s): <br>
1.1.9 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
