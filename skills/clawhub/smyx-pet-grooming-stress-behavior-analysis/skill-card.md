## Description:

Analyzes pet grooming session videos to identify stress-related behaviors such as struggling, panting, and tail tucking, then reports a stress level to help groomers decide when to intervene.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet groomers, veterinary clinics, and pet-care teams can use grooming-session videos to review visible stress signals and stress-level assessments, helping them respond during grooming. The report is for behavioral observation and does not provide a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account handling may expose credentials, and account tokens are saved locally.

Mitigation: Wait for account-handling fixes before use with sensitive accounts, and use a separate workspace for each user.

Risk: Videos are sent to LifeEmergence, and export-only mode may still upload footage; the --api-url option should not be relied on to change the processing destination.

Mitigation: Wait for the export-only fix before using private footage, and check LifeEmergence's retention and report-access rules before uploading.

## Reference(s):

- [API interface reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Report links]

**Output Format:** [Structured behavior analysis report in JSON or readable text; historical reports may be presented as a Markdown table.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Behavior observations and a stress level from 1 to 5; observational guidance only, with no medical diagnosis.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
