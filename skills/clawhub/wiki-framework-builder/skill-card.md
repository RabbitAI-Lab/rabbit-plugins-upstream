## Description: <br>
Builds Chinese consulting-style report frameworks from an upstream scoped JSON handoff, producing external-facing Word and Markdown report outlines plus a structured JSON handoff while keeping internal routing labels out of client-facing outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leadleo](https://clawhub.ai/user/leadleo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Analysts, consultants, and research teams use this skill after task scoping to turn a scoped research brief into a client-ready Chinese report framework for market insight, feasibility, government research, ranking, diligence, or strategy reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated report frameworks may still include internal labels, assumptions, or confidence details if not reviewed before external sharing. <br>
Mitigation: Review the generated Word, Markdown, and JSON outputs before sending them externally, confirming that internal labels, assumptions, and confidence details are excluded. <br>


## Reference(s): <br>
- [Engineering Dimension Database](references/engineering_dimension_database.md) <br>
- [External Framework Standard](references/external_framework_standard.md) <br>
- [Framework Generation Rules](references/framework_generation_rules.md) <br>
- [Output Contract](references/output_contract.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, shell commands] <br>
**Output Format:** [Chat summary, report_framework.docx, report_framework.md, and report_framework_handoff.json] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Word output is generated from the JSON handoff; external-facing Word and Markdown outputs should not expose internal routing labels, hidden confidence details, or pricing information.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
