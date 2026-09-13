## Description:

Provides a human-reviewed insurance claims workflow reference covering intake, document handling, medical review, liability assessment, adjustment checks, fraud-risk detection, adjudication review, and closure communications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Insurance claims employees use this skill as a reference workflow for drafting and checking claim intake records, material review outputs, medical and liability assessments, adjustment summaries, fraud-risk notes, adjudication recommendations, and customer communications. Outputs are drafts and must be reviewed and acted on only by authorized personnel in the institution's controlled systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authoritative security verdict is suspicious because the workflow includes contradictory references to local logs, retention, and high-impact claims actions.

Mitigation: Install only in a controlled insurance environment after removing or overriding local file, log, and retention instructions and confirming that institution systems handle all audit trails.

Risk: Claims-system, notification, archive, fraud, customer-history, and medical-history actions can affect customers, money, or sensitive records.

Mitigation: Require explicit authorized human approval for every claims-system query, notification, archive, fraud review, customer-history lookup, and medical-history action.

Risk: Claims workflows may process personal, medical, financial, and customer business data.

Mitigation: Apply data minimization and masking before use, and keep any retention or external communication within approved institutional systems and policies.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gechengling/skills/claim-expert-digital-employee)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Configuration instructions, Guidance]

**Output Format:** [Markdown with structured claim workflow drafts, checklists, risk notes, and JSON-style examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [All outputs require human review before use and should avoid direct handling of sensitive customer, medical, or payment data unless the data is minimized and authorized.]

## Skill Version(s):

2.1.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
