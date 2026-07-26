## Description: <br>
Skill Compliance checks skills before publication for domestic-platform compliance issues, including financial sensitive terms, required disclaimers, security red lines, privacy, and regulatory concerns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwumit](https://clawhub.ai/user/wwumit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill publishers use this agent to run local preflight checks before publishing skills to SkillHub or similar domestic platforms. It reports legal-compliance findings, platform advisories, scores, and remediation guidance for single skills or batches of skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plugin files execute as code during scans when loaded by the local compliance checker. <br>
Mitigation: Keep the bundled plugins unchanged unless you trust and review replacement plugin files before running the scanner. <br>
Risk: Compliance findings are automated preflight signals and may not cover every legal or platform-specific requirement. <br>
Mitigation: Use the report as review guidance and have the skill owner or qualified reviewer confirm final publication readiness. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/wwumit/skills/skill-compliance) <br>
- [Publisher Profile](https://clawhub.ai/user/wwumit) <br>
- [README.md](artifact/README.md) <br>
- [Rule Reference Catalog](artifact/rules/skillhub-rules.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Terminal text reports or JSON report files with scores, findings, and recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally with Python standard library only; no network access is described by the artifact.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
