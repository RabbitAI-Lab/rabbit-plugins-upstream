## Description:

Read a TherapyNotes client portal (www.therapyportal.com/p/<practice>/) from a shell — upcoming therapy appointments, document/paperwork requests (pending and completed), always-available practice forms, balances due, payment receipts, secure-message threads, and completed forms or receipts downloaded as PDFs — through the user's signed-in portal tab with the fpx CLI. Use when asked about TherapyPortal / TherapyNotes, therapy appointments or sessions, paperwork the therapist sent, what is owed to the practice, or a therapy receipt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users with a signed-in TherapyNotes portal use this skill to retrieve upcoming appointments, practice forms and paperwork, balances, payment receipts, and secure-message threads, and to download completed forms or receipts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The raw command bypasses the promised read-only limits and could submit changes using the signed-in account.

Mitigation: Before using this with therapy records, remove raw access or restrict it to verified reading endpoints with field filtering.

Risk: Therapy records can contain sensitive information, including records about minors.

Mitigation: Use projected reads, pair only the intended browser, and protect downloaded PDFs.

## Reference(s):

- [Endpoint Reference](artifact/references/endpoints.md)
- [TherapyPortal](https://www.therapyportal.com)
- [ClawHub Skill Release](https://clawhub.ai/chrischall/skills/therapyportal-mcp)

## Skill Output:

**Output Type(s):** [JSON, PDF files]

**Output Format:** [JSON text and downloaded PDF files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [PDF downloads are saved to the browser's download folder and logged by the practice.]

## Skill Version(s):

0.3.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
