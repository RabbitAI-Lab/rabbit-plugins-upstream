## Description:

Access OurFamilyWizard (OFW) messages, calendar, expenses, and journal from a shell by using the fpx CLI to capture a signed-in browser bearer token, then using curl against OFW REST endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical OFW users use this skill to retrieve OFW account data and issue direct OFW API calls from shell workflows without running the ofw-mcp server. It is intended for careful, authorized account access where the user can inspect and control each command before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill retrieves and uses an OFW browser bearer token for direct account access.

Mitigation: Use it only for an OFW account you are authorized to access, avoid exposing tokens in logs or shared shells, and recapture tokens only when needed.

Risk: Write and delete commands can immediately change or remove sensitive OFW records without an enforced confirmation step.

Mitigation: Prefer read-only operations unless a change is intentional, and manually verify IDs, recipients, payloads, dates, amounts, and filenames before running any write, upload, or delete command.

Risk: Some message POST responses may look successful even when the intended content did not land.

Mitigation: After sending or saving a draft, re-fetch the returned message ID and confirm the subject and body match the intended content.

Risk: Some read operations can affect account-visible state, such as marking unread messages read or updating last-seen status.

Mitigation: Treat detail and dashboard reads as potentially state-changing and avoid them when preserving unread or last-seen state matters.

## Reference(s):

- [OurFamilyWizard request examples](artifact/references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes commands that may perform live API reads, writes, uploads, and deletes when executed by an authorized user.]

## Skill Version(s):

2.18.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
