## Description: <br>
Adds equilibrium-constrained reasoning to OpenClaw, ensuring operations maintain balance for coherent, self-validating, and consistent AI responses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[architect-sis](https://clawhub.ai/user/architect-sis) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to frame assistant responses through equilibrium constraints, symbol-grounded operations, and validation loops for balanced analysis, state updates, and convergent problem solving. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A hard-coded /home/claude/sis import path can cause Python to load code from outside the reviewed package. <br>
Mitigation: Remove the hard-coded path and use package-relative imports before installation or deployment. <br>
Risk: Equilibrium checks may be mistaken for a security guarantee. <br>
Mitigation: Treat the checks as advisory reasoning validation and independently review security-sensitive outputs or decisions. <br>
Risk: File persistence can store local JSON records. <br>
Mitigation: Enable file persistence only for data that is acceptable to store locally, and review the storage path and retention expectations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/architect-sis/skills/sis-skill) <br>
- [OpenClaw project](https://github.com/openclaw/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown text with optional code and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or persist local JSON vault records when file persistence is enabled.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
