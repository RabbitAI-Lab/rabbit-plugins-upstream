## Description: <br>
Pre-publish security self-audit for OpenClaw skills that walks the ClawHub publishing checklist and emits a scored pass/fail report with concrete fixes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kimmyplusli](https://clawhub.ai/user/kimmyplusli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill publishers use this skill to audit OpenClaw skill folders before publishing to ClawHub or before installing a third-party skill. It reviews code, SKILL.md instructions, release metadata, declaration mismatches, and semantic prompt-injection risks, then reports pass, warning, and failure findings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad input paths may cause the agent to inspect unrelated private projects or secrets. <br>
Mitigation: Invoke the skill with a specific skill folder path and avoid pointing it at broad parent directories. <br>
Risk: The audit automates mechanical checks and may miss semantic prompt-injection risks that require human judgment. <br>
Mitigation: Review the generated findings and manually read suspicious skill instructions before publishing or installing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kimmyplusli/skills/skill-audit) <br>
- [OpenClaw](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with PASS/WARN/FAIL findings, command evidence, scoring, and concrete fixes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a scored audit report; no file changes are made unless the user separately asks for fixes.] <br>

## Skill Version(s): <br>
0.1.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
