## Description:

Read a TherapyNotes client portal (www.therapyportal.com/p/<practice>/) from a shell — upcoming therapy appointments, document/paperwork requests (pending and completed), always-available practice forms, balances due, payment receipts, secure-message threads, and completed forms or receipts downloaded as PDFs — through the user's signed-in portal tab with the fpx CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Clients and caregivers with access to a TherapyNotes portal can use this skill to review upcoming appointments, paperwork, balances, receipts, and secure messages, or download completed forms and receipts. It is intended for retrieving only the records needed from the signed-in portal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review rates the skill suspicious: an authenticated portal command may change records despite the documented read-only purpose, and the scan was partial.

Mitigation: Review command behavior before use, limit use to the documented projected read commands, and confirm the command is read-only before running it against an authenticated portal.

Risk: Portal results can contain sensitive mental-health records, including records about minors and full demographic details from raw endpoints.

Mitigation: Request only the records needed, use projected commands, and do not print raw patient-demographic responses.

## Reference(s):

- [TherapyPortal wire protocol and endpoints](references/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/therapyportal-mcp)
- [TherapyPortal](https://www.therapyportal.com)

## Skill Output:

**Output Type(s):** [JSON, PDF files, Shell commands, Guidance]

**Output Format:** [Projected JSON results, downloaded PDF files, and Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Portal data may include sensitive mental-health information; downloads are saved through the signed-in browser.]

## Skill Version(s):

0.4.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
