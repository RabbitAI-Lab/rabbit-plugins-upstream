## Description:

Generates a warm-yellow DOCX retirement and inheritance solution guide from a risk assessment report and second-meeting notes, mapping P0-P3 risks to implementable planning actions without recommending specific products or brands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hukaiyi777](https://clawhub.ai/user/hukaiyi777)

### License/Terms of Use:

MIT

## Use Case:

External retirement, inheritance, and insurance-planning advisors use this skill after client follow-up discussions to turn risk findings into an actionable client solution guide. The output supports human advisor review, compliance approval, and later product selection without placing specific product or brand recommendations in the main plan.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill expects client financial, family, and health information that may be sensitive.

Mitigation: Use it only in an approved environment, redact unnecessary identifiers before providing source materials, and handle generated DOCX files as sensitive client records.

Risk: Generated plans may require insurance, legal, trust, underwriting, or regulatory review before client use.

Mitigation: Review the output for compliance before sharing and keep specific product selections in the reserved page only after institutional compliance approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hukaiyi777/skills/hky-insure-solution)
- [hky-meeting-notes upstream skill](https://github.com/hukaiyi777/hky-meeting-notes)
- [hky-insure-risk-report upstream skill](https://github.com/hukaiyi777/hky-insure-risk-report)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance and Python-generated DOCX document structure]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a zero-third-party-dependency Python OOXML generator; generated client documents may contain sensitive financial, family, and health information.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
