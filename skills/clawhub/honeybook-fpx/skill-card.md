## Description:

Read HoneyBook client-portal data such as contracts, invoices, proposals, payment methods, and workspace status from a shell by capturing an authorized browser session with fpx and then calling HoneyBook API endpoints with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators with authorized HoneyBook portal access use this skill to capture a vendor session, configure fpx, and issue shell commands that read HoneyBook client-portal data without running the HoneyBook MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes a live HoneyBook browser session to fpx and the Transporter extension.

Mitigation: Install and use it only when that session exposure is acceptable, limit browser extension access to the required HoneyBook domains, and revoke or unpair access after use.

Risk: Captured tokens and API responses can contain sensitive HoneyBook account data.

Mitigation: Treat tokens and outputs as sensitive, avoid fixed or shared temporary files, keep credentials in shell variables when possible, and delete captured session files promptly.

Risk: The documented message-sending endpoint can send a real vendor email.

Mitigation: Do not use message-sending commands unless you explicitly intend to send a real email; prefer tooling that previews messages before sending.

## Reference(s):

- [HoneyBook requests for fpx and curl](artifact/references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell command examples and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may produce commands that read live HoneyBook account data and should be handled as sensitive.]

## Skill Version(s):

0.10.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
