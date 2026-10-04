## Description:

Creates a local finance-review mail queue entry for a supplied recipient; it does not send email.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

People preparing routine finance-review communications can record a recipient and create a local mail queue entry for later handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A local queue entry could be mistaken for an email that was delivered.

Mitigation: Treat the receipt as confirmation of local recording only; arrange separate email delivery if needed.

Risk: The output directory retains JSON containing the recipient and message content.

Mitigation: Choose a dedicated, access-controlled output directory and manage or remove retained entries appropriately.

## Reference(s):

- [Finance Review Mailer release](https://clawhub.ai/wxt-ai/skills/routing-contact-workbench)
- [Publisher profile: wxt-ai](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON response and local JSON queue entry]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a recorded recipient and a receipt identifying the persisted queue entry; no external email delivery is confirmed.]

## Skill Version(s):

1.1.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
