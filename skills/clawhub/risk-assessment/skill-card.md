## Description: <br>
Framework-directable information security risk assessment that identifies threats, evaluates likelihood and impact with a 3x3 matrix, maps findings to compliance controls, and recommends prioritized risk treatments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dangsllc](https://clawhub.ai/user/dangsllc) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers, security assessors, and compliance teams use this skill to turn system or environment context into structured information security risk findings mapped to a selected compliance framework. It is suited for producing risk register inputs, executive summaries, and prioritized remediation actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Assessment inputs may include secrets, regulated data, or confidential security details. <br>
Mitigation: Review and redact sensitive documents or context before using the skill, especially with hosted model workflows. <br>
Risk: The included API example sends assessment context to an external AI provider. <br>
Mitigation: Use the example only where the provider and data handling path are approved for the information being assessed. <br>


## Reference(s): <br>
- [ClawHub Risk Assessment Skill](https://clawhub.ai/dangsllc/skills/risk-assessment) <br>
- [Skill Definition](artifact/SKILL.md) <br>
- [Example Output](artifact/examples/example_output.json) <br>
- [Usage Example](artifact/examples/usage.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance] <br>
**Output Format:** [Structured JSON with risk findings, scores, treatment recommendations, an executive summary, and prioritized actions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Findings use a 3x3 likelihood-impact matrix and include framework control mappings when a framework is provided or defaulted.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
