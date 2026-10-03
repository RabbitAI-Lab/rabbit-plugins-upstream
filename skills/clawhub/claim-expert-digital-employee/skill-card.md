## Description:

Provides a Chinese-language reference workflow and draft analysis for insurance claims, from intake and medical review through settlement review and customer communication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Insurance claims staff use this Chinese-language reference to structure claim intake, review supporting and medical materials, assess coverage and fraud indicators, and draft decision or notification text for qualified human review. Authorized staff perform all system actions and make final decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposure of personal identifiers, bank account details, or medical records in claim inputs.

Mitigation: Minimize and mask sensitive information before providing it to the skill.

Risk: Incorrect settlement, denial, fraud, or notification drafts could affect customers if treated as final decisions.

Mitigation: Have qualified staff check drafts against the institution's authorized systems and approve any resulting decision or communication.

Risk: Treating workflow descriptions as authorization to send notices or close and archive cases.

Mitigation: Require authorized personnel to perform and record these actions in institutional systems; do not rely on the skill to execute them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/gechengling/skills/claim-expert-digital-employee)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown reports, tables, checklists, and draft notification text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts only; no customer-system access, file creation, notification delivery, or case closure.]

## Skill Version(s):

2.1.9 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
