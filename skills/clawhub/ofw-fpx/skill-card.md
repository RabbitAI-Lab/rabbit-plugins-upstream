## Description:

Access OurFamilyWizard messages, calendar, expenses, and journal data from a shell by using the fpx CLI to capture a signed-in web session token, then calling the OFW REST API with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable OFW users use this skill to retrieve OFW records and run scripted message, calendar, expense, journal, attachment, and dashboard workflows without running the OFW MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses a live OFW browser session token for direct shell API access to sensitive family-court records.

Mitigation: Use the token only in trusted shells, avoid sharing logs or shell history that may expose it, and revoke or reset the session when finished.

Risk: Write and delete examples can make real, visible, and potentially permanent changes to OFW records without a built-in dry run or confirmation gate.

Mitigation: Prefer read-only use, manually verify every ID and payload before write or delete calls, and re-fetch changed records to confirm the expected result.

Risk: Some read operations can change OFW state, including marking unread inbox messages as read or updating dashboard last-seen status.

Mitigation: Treat reads as potentially stateful and avoid detail or dashboard requests when preserving unread or last-seen state matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw-fpx)
- [OurFamilyWizard request examples](references/requests.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes curl, jq, and fpx command patterns for direct OFW API access.]

## Skill Version(s):

2.16.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
