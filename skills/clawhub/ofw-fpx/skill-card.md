## Description:

Access OurFamilyWizard messages, calendar, expenses, and journal records from shell workflows by using fpx to capture a signed-in Bearer token and curl to call OFW REST endpoints directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically capable OFW users use this skill to script access to messages, calendar events, expenses, journal entries, and attachments from a shell without running the OFW MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill teaches direct use of a live OFW session token for sensitive family-court records.

Mitigation: Install only for workflows that intentionally use the signed-in OFW session token, keep the token local, and prefer read-only or confirmation-gated execution.

Risk: Write, delete, upload, expense, journal, calendar, and message-send commands can affect shared records without an enforced confirmation gate.

Mitigation: Manually review the exact endpoint, recipients or record IDs, payload, and expected consequence before running any write-capable command.

## Reference(s):

- [OurFamilyWizard requests for fpx + curl](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell command examples, curl requests, and JSON payload snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may perform live read, write, upload, and delete operations against OFW when run with a valid signed-in session token.]

## Skill Version(s):

2.17.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
