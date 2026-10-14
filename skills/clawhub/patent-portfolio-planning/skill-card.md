## Description:

Helps teams compare technology routes and plan patent portfolios, filing priorities, budgets, and disclosure timing using PatentMax reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, product teams, and patent-planning professionals use this skill to compare development routes and prepare patent filing plans informed by their technical goals, budgets, and disclosure dates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential patent topics, technical materials, budgets, and disclosure dates may be sent to PatentMax.

Mitigation: Review inputs before submission and omit confidential details unless sharing them with PatentMax is approved.

Risk: A configured API endpoint may receive sensitive planning data and credentials.

Mitigation: Do not set PATENTMAX_BASE_URL unless the destination is fully trusted.

Risk: Trial API credentials and task history persist locally under ~/.patentmax.

Mitigation: Protect access to that directory and handle its contents as sensitive credentials and records.

Risk: Patent coverage and design-around recommendations may miss unpublished applications or legal constraints.

Mitigation: Treat reports as planning guidance and obtain jurisdiction-specific advice from a qualified patent professional before filing or relying on freedom-to-operate conclusions.

## Reference(s):

- [PatentMax skill release](https://clawhub.ai/ip930/skills/patent-portfolio-planning)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [Business context guide](references/context-guide.md)
- [Analysis workflow](references/workflow.md)
- [Troubleshooting and FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Files]

**Output Format:** [Markdown summary and downloadable Word report (.docx)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous report generation; may include quality caveats when evidence is limited.]

## Skill Version(s):

1.1.2 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
