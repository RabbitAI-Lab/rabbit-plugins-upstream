## Description:

Discord DM or relay recipient binding: authenticate the requester, validate the recipient, and require agent-sent requester attribution before every recipient-specific send.

This skill is ready for commercial/non-commercial use.

## Publisher:

[daniel-refahi-ikara](https://clawhub.ai/user/daniel-refahi-ikara)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill in Discord forwarding workflows to bind each recipient-specific send to an approved requester and recipient, add requester attribution, and validate a delivery receipt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper cannot authenticate Discord requesters, enforce the target, insert attribution, or independently confirm delivery; a PASS alone does not establish those facts.

Mitigation: Use a trusted platform wrapper or before-tool hook to authenticate the requester, enforce the bound target, insert attribution, and provide genuine delivery evidence; test that integration before sending confidential content.

## Reference(s):

- [Approved roster schema](references/approved-roster.schema.json)
- [ClawHub skill release](https://clawhub.ai/daniel-refahi-ikara/skills/discord-recipient-safety)

## Skill Output:

**Output Type(s):** [Guidance, JSON, Shell commands]

**Output Format:** [Markdown instructions, shell command examples, and JSON binding or receipt records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Binding and receipt records omit message bodies.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
