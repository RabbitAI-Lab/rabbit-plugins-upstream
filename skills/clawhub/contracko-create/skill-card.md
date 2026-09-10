## Description:

Takes a new contract from questionnaire to drafted, signed and filed in Contracko.

This skill is ready for commercial/non-commercial use.

## Publisher:

[contracko](https://clawhub.ai/user/contracko)

### License/Terms of Use:

MIT-0

## Use Case:

External users and teams use this skill to gather contract terms, prepare a reviewable draft workflow, coordinate signature steps in Contracko, and file the executed agreement with reminders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create local plaintext handoff records for confidential contract work.

Mitigation: Use an approved protected location, avoid source-controlled folders and counterparty-revealing filenames where possible, review what will be stored, and delete the handoff after the contract is filed and verified.

Risk: Draft contract text can look fluent while still containing incorrect, unenforceable, or conflicting terms.

Mitigation: Start from an organization-approved template when available and require legally competent human review before signature.

Risk: The final executed contract may differ from the questionnaire handoff or extracted filing data.

Mitigation: Reconcile the executed copy against the handoff and surface differences in notice period, renewal term, liability cap, and other material terms.

## Reference(s):

- [Contracko Create on ClawHub](https://clawhub.ai/contracko/skills/contracko-create)
- [Contracko import workflow](../contracko-import/SKILL.md)
- [Contracko review workflow](../contracko-review/SKILL.md)
- [Contracko filing workflow](../contracko/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with structured questionnaire answers and handoff records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local plaintext handoff records containing confidential contract details when the agent has filesystem access.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
