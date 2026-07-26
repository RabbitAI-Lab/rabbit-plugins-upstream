## Description: <br>
Run a security review workflow for Codex or ClawHub skills before activation or publication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, skill authors, maintainers, and teams use this skill to statically review Codex or ClawHub skill folders for unsafe scripts, credential exposure, dependency risks, broad activation triggers, and publish-readiness issues before activation or release. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Language-version and README scope mismatch could lead users to expect a stricter security-review workflow than some instructions provide. <br>
Mitigation: Align the English, Chinese, README, and reference workflow text to the same security-gate purpose before relying on the skill for release decisions. <br>
Risk: Broad triggers and implicit invocation could activate the skill for requests that are not explicit security reviews. <br>
Mitigation: Tighten trigger keywords and constrain implicit invocation to explicit skill-security-review, pre-activation, or pre-publication requests. <br>
Risk: Skill review output is advisory and may miss issues if users execute untrusted scripts during validation. <br>
Mitigation: Use static inspection first, avoid executing untrusted code by default, and run any dynamic checks only in an appropriate isolated environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-skillscan-security-workflow-helper-130902) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Skill Vetter demand signal](https://clawhub.ai/skills/skill-vetter) <br>
- [SkillScan demand signal](https://clawhub.ai/skills/skillscan) <br>
- [AdMapix demand signal](https://clawhub.ai/skills/admapix) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown scan report with findings, remediation checklist, pass/block recommendation, and optional validation commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses static inspection first and avoids executing untrusted scripts unless the user explicitly asks in an appropriate environment.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
