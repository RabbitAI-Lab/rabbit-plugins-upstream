## Description: <br>
Verified Task is a legacy verification-guided workflow aid that helps agents and operators structure task claims for review against evidence, receipts, or acceptance criteria without certifying completion or performing cryptographic checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nutstrut](https://clawhub.ai/user/nutstrut) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agent workflow owners use this skill to add a PASS, FAIL, or INDETERMINATE gate before payments, publishing, automation steps, or other consequential actions proceed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat the skill as a proof, receipt verifier, or autonomous approval authority. <br>
Mitigation: Use it as a workflow checklist and require explicit human approval for FAIL or INDETERMINATE results; use a dedicated receipt verifier for cryptographic checks. <br>
Risk: Optional external verification could expose secrets or sensitive task content. <br>
Mitigation: Send only the minimum structured metadata needed for optional verification and avoid sending secrets or sensitive content. <br>


## Reference(s): <br>
- [OpenClaw Integration Notes](artifact/references/openclaw-integration.md) <br>
- [ClawHub skill page](https://clawhub.ai/nutstrut/skills/verified-task) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, JSON, Shell commands] <br>
**Output Format:** [Markdown guidance with JSON verification records and a shell reminder script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Verdicts use PASS, FAIL, or INDETERMINATE with a reason and confidence level.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
