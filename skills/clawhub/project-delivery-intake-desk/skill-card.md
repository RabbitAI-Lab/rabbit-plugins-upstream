## Description:

Prepares project context from an intake note and builds a delivery ledger entry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Project delivery teams use an intake note to prepare concise project context, then turn that context into a delivery ledger entry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Intake notes may contain sensitive project details processed by the active assistant.

Mitigation: Remove sensitive details from notes unless you are comfortable sharing them with the active assistant.

## Reference(s):

- [Project Delivery Intake Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/project-delivery-intake-desk)

## Skill Output:

**Output Type(s):** [Text, Structured data]

**Output Format:** [JSON-like objects in the requested output fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [project_context contains project_code, source_title, and note_digest; delivery_entry contains entry_id, project_code, and summary.]

## Skill Version(s):

2.1.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
