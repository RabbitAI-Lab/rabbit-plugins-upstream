## Description:

Build a delivery ledger entry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Project delivery operators and teams use this skill to turn supplied delivery handoff context into a concise ledger entry for routine project updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generated ledger entry could include unintended project details if the user supplies sensitive or excessive context.

Mitigation: Provide only the project context intended for the delivery ledger entry.

Risk: The ledger summary may be incomplete or misleading if the supplied handoff context is incomplete.

Mitigation: Review the generated entry against the source handoff before using it as an operational record.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wxt-ai/skills/project-code-notes-workbench)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Structured delivery_entry object with entry_id, project_code, and summary fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses only the project_context supplied in the current request.]

## Skill Version(s):

1.0.7 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
