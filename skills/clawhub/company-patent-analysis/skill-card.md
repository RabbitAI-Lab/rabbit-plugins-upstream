## Description:

Generates a competitive patent landscape report for a named company and technology area using PatentMax data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and business teams use this skill to compare a company's patents with competitors in a specified technology area and obtain a decision-support report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent-analysis inputs and optional uploaded materials are sent to PatentMax/ip930.com.

Mitigation: Obtain approval before sending confidential company information or files.

Risk: Report creation may incur a charge.

Mitigation: Confirm the fee and obtain user approval before submitting a paid report.

Risk: Trial credentials and task state may persist in ~/.patentmax.

Mitigation: Delete cached trial and task files when local report state should not be retained.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ip930/skills/company-patent-analysis)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [Analysis workflow](artifact/references/workflow.md)
- [Troubleshooting and report quality](artifact/references/faq.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files]

**Output Format:** [Progress and findings in text or Markdown; downloadable Word (.docx) report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report is generated asynchronously and saved locally when complete.]

## Skill Version(s):

1.1.2 (source: SKILL.md frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
