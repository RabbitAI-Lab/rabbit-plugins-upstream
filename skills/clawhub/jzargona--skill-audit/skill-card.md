## Description: <br>
Audit locally installed agent skills for security and policy issues using the SkillLens CLI or a manual fallback workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jzargona](https://clawhub.ai/user/jzargona) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and reviewers use this skill to audit local Codex or Claude skill directories, prioritize suspicious findings, and produce risk-focused reports with concrete evidence and fix recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The audit workflow may read skill files under the selected directory, which can expose more local content than intended if the scan root is too broad. <br>
Mitigation: Review the target path before scanning and prefer a concrete skill directory or configured skill root. <br>
Risk: The workflow may require installing or running the external SkillLens CLI. <br>
Mitigation: Confirm the CLI source and use the manual audit fallback when the CLI is unavailable or not trusted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jzargona/skills/skill-audit) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown audit report with inline shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include verdicts, risk scores, evidence quotes, and fix recommendations.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
