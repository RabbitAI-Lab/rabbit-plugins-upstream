## Description: <br>
Organizes procurement, engineering, quality control, packaging, logistics, and customer deadline requirements into an actionable delivery plan with critical paths and warning points. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Operations, sourcing, and delivery teams use this Chinese-language skill to turn user-provided order, purchasing, QC, packaging, logistics, deadline, and owner information into a structured delivery plan. It helps identify parameter completeness, dependencies, critical paths, risk nodes, split-delivery options, warning conditions, and items that cannot yet be committed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Delivery plans may be mistaken for firm commitments when inputs are estimated, incomplete, conflicting, or unverified. <br>
Mitigation: Preserve uncertainty, label preliminary analysis clearly, and require manual verification before committing to dates, payments, logistics status, or responsible owners. <br>
Risk: Missing order, QC, packaging, logistics, deadline, or owner details can produce an incomplete critical path. <br>
Mitigation: Output a parameter status table first and stop or mark the analysis as preliminary until minimum operating conditions are met. <br>
Risk: Business facts may change after the user provides them. <br>
Mitigation: Treat outputs as planning support and re-check payment status, delivery dates, logistics facts, and accountable owners before external commitments. <br>


## Reference(s): <br>
- [zayn-delivery on ClawHub](https://clawhub.ai/zaynpeng/skills/zayn-delivery) <br>
- [Skill Rules](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>
- [Examples](artifact/examples.md) <br>
- [Tests](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with structured sections and parameter-status tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chinese-language planning support based on user-provided order, logistics, deadline, and responsible-owner facts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
