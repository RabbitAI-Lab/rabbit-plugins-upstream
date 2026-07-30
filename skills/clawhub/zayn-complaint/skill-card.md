## Description: <br>
Organizes customer complaint details, order information, evidence, warranty status, and responsibility state to recommend the next aftersales step. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Aftersales, support, and operations staff use this skill to structure customer complaint information, identify missing or conflicting evidence, separate facts from assumptions, and decide whether to request more evidence, continue troubleshooting, assess responsibility, or move toward return and replacement workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Complaint analysis may involve customer, order, product, warranty, or evidence data that should not be over-collected or exposed. <br>
Mitigation: Use only authorized complaint data, provide the minimum necessary details, and redact unrelated personal information where possible. <br>
Risk: The skill may suggest next steps that could be mistaken for final refund, replacement, compensation, responsibility, or legal decisions. <br>
Mitigation: Keep final commercial, responsibility, compensation, and legal decisions with authorized staff, and treat the skill output as structured guidance. <br>
Risk: Incomplete or conflicting evidence can lead to premature responsibility conclusions or inappropriate aftersales commitments. <br>
Mitigation: Require the output to identify missing, conflicting, and unverified information before moving from preliminary analysis to a formal recommendation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-complaint) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [README.md](artifact/README.md) <br>
- [tests.md](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with structured sections and tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces parameter completeness checks, confirmed facts, unverified items, evidence lists, possible causes, risk flags, responsibility status, and recommended next steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
