## Description:

Analyzes a named company's patents in a specified technology area and generates a competitor landscape report with traceable patent references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Business analysts, patent teams, and decision-makers use this skill to compare a company's patent activity with competitors in a defined technology area and prepare a report for diligence or planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names, analysis objectives, target markets, and optional background materials are sent to the PatentMax cloud service.

Mitigation: Obtain approval before sharing confidential diligence materials and provide only necessary inputs.

Risk: Generating a report can incur charges; repeating a submission may charge again.

Mitigation: Confirm the quoted cost and scope before authorizing the paid request; resume an existing task instead of resubmitting it.

Risk: The trial key and task state are cached locally under ~/.patentmax.

Mitigation: Protect access to the local cache and remove it when retention is no longer appropriate.

Risk: Patent publication delays, applicant-name differences, and source gaps can make the analysis incomplete.

Mitigation: State search scope and quality limitations, trace claims to publication numbers, and seek qualified advice for legal conclusions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-competitor-analysis)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [Analysis workflow](references/workflow.md)
- [Input materials guide](references/materials-guide.md)
- [Troubleshooting FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise written analysis and a downloadable DOCX report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report findings should cite patent publication numbers and disclose coverage and data-quality limits.]

## Skill Version(s):

1.1.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
