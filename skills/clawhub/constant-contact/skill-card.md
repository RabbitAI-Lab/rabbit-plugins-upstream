## Description:

Helps agents manage Constant Contact contacts, campaigns, lists, and marketing analytics through an authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and their agents use this skill to review Constant Contact data and, with explicit approval, manage contacts, campaigns, and related automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Campaign sends, bulk changes, imports, or deletions could affect the wrong contacts or account.

Mitigation: Require explicit approval and verify the connected account, exact resource IDs, recipient lists, and scope before execution.

Risk: Bulk exports can disclose contact information beyond the intended task.

Mitigation: Confirm export fields and destination with the user; limit output to the data needed.

Risk: Persistent triggers may continue running actions after the current task.

Mitigation: Confirm the trigger, destination, and intended schedule or event with the user before enabling automation.

## Reference(s):

- [Constant Contact skill on ClawHub](https://clawhub.ai/byungkyu/skills/constant-contact)
- [Maton homepage](https://maton.ai)
- [Constant Contact V3 API overview](https://developer.constantcontact.com/api_guide/getting_started.html)
- [Constant Contact API reference](https://developer.constantcontact.com/api_reference/index.html)
- [Maton documentation](https://docs.maton.ai)
- [Time trigger reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide approved Constant Contact changes and scheduled automations.]

## Skill Version(s):

1.2.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
