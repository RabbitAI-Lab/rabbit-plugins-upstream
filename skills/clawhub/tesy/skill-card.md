## Description: <br>
Conducts adversarial analysis by decomposing claims and coordinating multiple expert perspectives to produce steelman arguments and counterarguments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kipasdinding6969-alt](https://clawhub.ai/user/kipasdinding6969-alt) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to stress-test arguments, plans, architecture decisions, and content through structured adversarial review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local customization files can override the skill's default behavior. <br>
Mitigation: Keep the RedTeam customization folder trusted and review custom preferences before enabling the skill. <br>
Risk: Sensitive user material may be copied into multi-agent analysis prompts. <br>
Mitigation: Avoid giving the workflow secrets or private material unless all participating agent contexts are approved for that data. <br>
Risk: The skill sends a localhost notification when workflows run. <br>
Mitigation: Use the skill only in environments where the localhost notification behavior is expected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kipasdinding6969-alt/skills/tesy) <br>
- [RedTeam Skill](artifact/SKILL.md) <br>
- [Red Team Parallel Analysis Workflow](artifact/Workflows/ParallelAnalysis.md) <br>
- [Adversarial Validation Pattern](artifact/Workflows/AdversarialValidation.md) <br>
- [Red Team Philosophy](artifact/Philosophy.md) <br>
- [Red Team Integration Guide](artifact/Integration.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with structured analysis sections and numbered points] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The primary outputs are steelman arguments, counterarguments, critique summaries, and synthesized recommendations.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
