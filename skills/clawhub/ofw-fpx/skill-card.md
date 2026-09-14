## Description:

Access OurFamilyWizard messages, calendar, expenses, and journal data from a shell by using the fpx CLI to capture a signed-in web app bearer token and then calling the OFW REST API with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable OFW users use this skill to inspect and manage OFW messages, calendar entries, expenses, journal entries, and attachments through shell commands without running the OFW MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles a live OFW browser session bearer token.

Mitigation: Use a dedicated browser profile, verify package and extension provenance, and revoke the pairing or sign out when finished.

Risk: The skill can perform immediate write and delete actions on sensitive family-court records without enforced confirmation.

Mitigation: Manually review write/delete commands before execution and avoid agent-run write/delete examples unless the action is deliberate.

Risk: Some read operations can change OFW-visible state, such as marking unread messages as read or updating dashboard last-seen status.

Mitigation: Limit detail and dashboard reads when preserving read status matters, and verify important effects in the OFW web app.

## Reference(s):

- [OurFamilyWizard request examples](artifact/references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell command examples and JSON-oriented curl/jq snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance includes token capture, request headers, endpoint examples, write confirmation steps, and auth-error handling.]

## Skill Version(s):

2.16.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
