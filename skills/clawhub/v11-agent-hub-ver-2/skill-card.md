## Description:

Creates a one-page A4 executive summary of PDF or DOCX reports, with key findings and board discussion questions tailored to Sber.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dariaakimov](https://clawhub.ai/user/dariaakimov)

### License/Terms of Use:

MIT-0

## Use Case:

Executives and analysts use the skill to condense PDF and Word reports into a concise briefing and prepare discussion questions for Sber’s board. It supports scanned and foreign-language documents and checks summary claims against the source; reviewers should independently verify the final claims and outside sources before sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crafted Word files may exhaust memory during processing.

Mitigation: Use trusted Word files or isolate conversion with memory limits.

Risk: A summary may overstate how thoroughly its claims or sources were verified.

Mitigation: Independently check final claims, warnings, and outside sources before sharing with decision-makers.

Risk: Research involving confidential reports could expose sensitive information through search terms.

Mitigation: Keep research offline or approve sanitized search terms.

Risk: Retained job data may remain available after it is no longer needed.

Mitigation: Remove retained job data when it is no longer needed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dariaakimov/skills/v11-agent-hub-ver-2)
- [Summary guidance](artifact/references/summary_canon.md)
- [Fact-checking guide](artifact/references/factcheck_guide.md)
- [Translation guide](artifact/references/translation_guide.md)
- [Humanization guide](artifact/references/humanize_guide.md)

## Skill Output:

**Output Type(s):** [PDF document, Text, Analysis, Guidance]

**Output Format:** [One-page A4 PDF executive summary with key findings and board discussion questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Source-document claims and external context require independent review before sharing.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
