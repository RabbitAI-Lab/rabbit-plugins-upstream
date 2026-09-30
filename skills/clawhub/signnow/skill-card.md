## Description:

Guides agents in using SignNow through Maton to upload documents, send signature invites, manage templates, and automate e-signature workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to assist users with SignNow documents, signature invitations, templates, and approved automations through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document or recipient changes may affect the wrong account or person.

Mitigation: Check the account, document, and recipient, and get explicit approval before each write.

Risk: Hosted functions, triggers, and destinations can continue running or forward sensitive event data.

Mitigation: Confirm the automation's scope, lifetime, and destination URL before enabling it; do not forward payloads to third-party hosts without informed approval.

Risk: Raw API keys can expose long-lived access to SignNow through Maton.

Mitigation: Prefer the CLI OAuth flow; avoid printing, persisting, or sharing credentials.

## Reference(s):

- [SignNow Skill on ClawHub](https://clawhub.ai/byungkyu/skills/signnow)
- [Maton](https://maton.ai)
- [SignNow API Reference](https://docs.signnow.com/docs/signnow/reference)
- [Maton Documentation](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with CLI commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and an authorized Maton connection; confirm writes and automations with the user.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
