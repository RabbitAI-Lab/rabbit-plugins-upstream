## Description:

Refiner (refiner.io) supports reading, creating, updating, and deleting data through the Refiner connector rather than direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Refiner contacts, forms, segments, survey responses, reporting, and account information from an OOMOL-connected Refiner workspace. It supports read workflows plus user-confirmed contact, segment, response-tagging, and event-tracking changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends executing mutable remote installer scripts directly in a shell.

Mitigation: Install the oo CLI from a pinned release and verify a checksum or signature before use.

Risk: The skill can access Refiner contacts, forms, responses, reporting, and account information, and it can make explicitly approved contact or segment changes.

Mitigation: Use it only with a Refiner workspace where those reads and approved changes are acceptable; confirm exact payloads and effects before write or destructive actions.

## Reference(s):

- [Refiner homepage](https://refiner.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Refiner skill page](https://clawhub.ai/oomol/skills/oo-refiner)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are requested as JSON and include data plus meta.executionId.]

## Skill Version(s):

1.0.3 (source: artifact metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
