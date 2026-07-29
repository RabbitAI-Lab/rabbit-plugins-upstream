## Description: <br>
Determines whether an issue should be escalated and organizes impact, actions already taken, available options, a recommended path, and needed support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and internal collaborators use this skill to decide whether an issue should be escalated, document the current impact and actions taken, compare options, and identify what support is needed. It is intended to pause for missing or conflicting critical facts rather than turning incomplete information into a formal conclusion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recommendations could be acted on before the underlying business evidence is fully verified. <br>
Mitigation: Review the impact, evidence, options, and recommended support with the responsible human decision-maker before taking escalation actions. <br>
Risk: The artifact is marked as draft for testing and examples and test cases are still pending. <br>
Mitigation: Pilot the skill with real, desensitized cases and confirm parameter parsing, minimum run conditions, and output structure before broad use. <br>
Risk: Issue escalation may involve sensitive business records or customer impact details. <br>
Mitigation: Provide only necessary, reliable evidence and avoid treating unverified, conflicting, or missing information as fact. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-escalate) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>
- [Examples](artifact/examples.md) <br>
- [Tests](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown with structured sections and, when enough information is present, a parameter status table and escalation analysis.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill asks for missing critical parameters before issuing a formal conclusion and marks incomplete analysis as preliminary.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence; artifact documentation lists v0.1 draft rule version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
