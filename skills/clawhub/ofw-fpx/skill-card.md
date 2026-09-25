## Description:

Access OurFamilyWizard messages, calendar, expenses, and journal data from a shell by using the fpx CLI to capture a signed-in web session bearer token and then issuing direct curl requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable OFW users use this skill to retrieve OFW records and prepare shell commands for messages, calendar events, expenses, journal entries, attachments, and related read/write workflows without running the ofw-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a captured signed-in OFW bearer token and provides shell commands that can read sensitive family, legal, and financial records.

Mitigation: Install only when this access is intended, protect the token as a live credential, and run commands in a controlled shell session.

Risk: Write and delete examples can immediately change shared OFW records, including messages, calendar events, expenses, journal entries, and attachments.

Mitigation: Prefer read-only use by default; before any write or delete, manually verify the target IDs and JSON or multipart payloads, and use an added confirmation wrapper for routine use.

Risk: Some OFW message POST responses can look successful even when the intended content was not persisted.

Mitigation: After every message send or draft save, re-fetch the returned message ID and compare the subject and body against the intended content.

Risk: Certain read calls can update OFW-visible state, such as marking unread messages as read or changing last-seen status.

Mitigation: Warn operators before detail or dashboard reads and avoid those calls when preserving unread or last-seen state matters.

## Reference(s):

- [OurFamilyWizard requests for fpx + curl](artifact/references/requests.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, curl examples, jq filters, and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes examples for live OFW read, write, upload, and delete operations; users should review IDs, payloads, and side effects before execution.]

## Skill Version(s):

2.19.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
