## Description:

Provides structured strategic analysis, risk assessment, and multi-option comparison using three complementary decision perspectives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnsmithfan](https://clawhub.ai/user/johnsmithfan)

### License/Terms of Use:

GPL-3.0

## Use Case:

People and teams facing consequential decisions use this skill to compare options, assess risks, and develop conditional recommendations from rational, risk-focused, and intuitive perspectives.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad comparison and risk-assessment triggers may invoke the framework when a simpler answer would suffice.

Mitigation: Use the framework only when structured decision analysis is useful for the user's request.

Risk: Recommendations may be mistaken for professional advice on legal, financial, compliance, or other high-impact decisions.

Mitigation: Treat conclusions as advisory and validate assumptions and implications with qualified people before acting.

Risk: The optional risk-matrix script writes an HTML report to a selected path.

Mitigation: Review the output path before running the script to avoid overwriting an unintended file.

## Reference(s):

- [MAGI framework](references/magi-framework.md)
- [Decision matrix](references/decision-matrix.md)
- [Method patterns](references/method-patterns.md)
- [Source repository (server-resolved provenance)](https://github.com/JohnSmithfan/MAGI-Strategic-Advisor)
- [ClawHub release](https://clawhub.ai/johnsmithfan/skills/magi-strategic-advisor)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Markdown decision analysis; optional code, text or JSON risk matrices, and HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes three-perspective judgments, vote and veto outcomes, prerequisites, and monitoring indicators.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata and CHANGELOG, released 2026-09-12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
