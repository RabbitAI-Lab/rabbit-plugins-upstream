## Description: <br>
Distinguishes customer statements, confirmed facts, contract and warranty boundaries, and current responsibility status so agents avoid premature admissions when evidence is incomplete. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Customer support and aftersales teams use this skill to separate customer claims, verified facts, assumptions, contract or warranty limits, and the current responsibility status before drafting internal assessments or external replies. It is not a substitute for legal review, management approval, or a final service decision. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: External replies may delay or avoid responsibility admissions in ways that are incomplete or unfair if used without review. <br>
Mitigation: Review outputs for fairness, completeness, and customer-service or legal fit before sending them externally. <br>
Risk: Missing or conflicting evidence may be mistaken for a final responsibility conclusion. <br>
Mitigation: Preserve gaps and conflicts in the output and require human confirmation before final responsibility, refund, replacement, or compensation decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-responsibility) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>
- [Usage examples](examples.md) <br>
- [Test criteria](tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Structured Markdown analysis with parameter status tables and responsibility-boundary sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided issue, product or order, evidence, confirmed facts, unresolved items, and desired responsibility-boundary statement; stops or labels preliminary analysis when evidence is insufficient.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
