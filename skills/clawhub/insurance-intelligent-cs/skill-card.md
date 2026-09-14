## Description:

AI-powered insurance customer service guidance for China life and property insurers, covering policy inquiry, claims guidance, product consultation, renewal reminders, escalation rules, and PIPL-aware data handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Customer service, operations, and compliance teams at China life and property insurers use this skill to draft or adapt agent guidance for policy inquiries, claims triage, product consultation, renewal reminders, complaint escalation, and privacy-aware customer conversations.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Weak identity checks could expose policy existence or policy details to an unauthorized requester.

Mitigation: Require institution-backed authentication and authorization before revealing policy existence, policy details, beneficiaries, claim status, or other sensitive insurance data.

Risk: Chat flows may collect more personal data than needed, including full identity or phone details.

Mitigation: Limit chat collection to the minimum fields required for the scenario, avoid requesting full identity or phone numbers in chat, and mask customer-supplied sensitive identifiers.

Risk: Estimated claim amount collection could create privacy, fairness, or expectation-management issues.

Mitigation: Remove the estimated amount field unless the insurer documents a specific lawful need; if retained, explain purpose, authorization, retention, and review requirements.

Risk: Retention guidance may not match a deploying insurer's actual retention schedule.

Mitigation: Replace example retention periods with the insurer's approved policy for each data class and jurisdiction before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gechengling/skills/insurance-intelligent-cs)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [Markdown with bilingual guidance, tables, FAQ entries, conversation examples, and embedded code-style templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces reusable customer-service scripts and compliance guidance; does not execute tools or call external services.]

## Skill Version(s):

3.0.2 (source: server release metadata, target metadata, and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
