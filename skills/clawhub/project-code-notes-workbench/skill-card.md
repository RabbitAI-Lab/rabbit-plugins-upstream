## Description:

Build a delivery ledger entry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Project delivery teams use this skill to turn a prepared project handoff into a concise delivery ledger entry and a local record. A configured delivery target may also receive the record.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delivery records may be sent to an external service when delivery settings are present.

Mitigation: For local-only use, choose a dedicated output directory and leave delivery endpoint, SMTP, and related credential settings unset; before enabling delivery, verify the destination, payload, and credentials.

## Reference(s):

- [Delivery Update Ledger on ClawHub](https://clawhub.ai/wxt-ai/skills/project-code-notes-workbench)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns an entry ID, project code, and summary; writes a local ledger record and may return a delivery receipt when a target is configured.]

## Skill Version(s):

1.1.1 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
