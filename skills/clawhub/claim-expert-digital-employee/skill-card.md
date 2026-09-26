## Description:

Provides draft guidance and review frameworks for insurance claims intake, document and medical review, coverage and payment assessment, fraud screening, and customer communications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Insurance claims staff use this Chinese-language reference to prepare draft intake records, review findings, calculation checks, fraud indicators, and customer notices for qualified human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conflicting workflow language could be read as authorizing claim decisions, customer notices, fraud actions, case closure, or archiving.

Mitigation: Require explicit approval by authorized staff for each consequential action; keep system lookups, sending, payments, closure, and archiving within institution-controlled workflows.

Risk: Claims analysis may expose medical histories and customer identifiers.

Mitigation: Minimize and de-identify inputs, restrict access to authorized personnel, and do not connect customer or medical-history tools without institution-specific controls.

Risk: Draft calculations and fraud indicators may be mistaken for final adjudications.

Mitigation: Have qualified staff verify findings against policy terms and institution systems; use approved calculation results for payment decisions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/gechengling/skills/claim-expert-digital-employee)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Chinese-language draft reports, checklists, and notice text in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts for human review; no files, customer messages, case changes, or payments are produced by the skill.]

## Skill Version(s):

2.1.8 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
