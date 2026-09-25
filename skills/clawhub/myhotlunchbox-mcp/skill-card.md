## Description:

Provides shell and curl guidance for reading and managing a My Hot Lunchbox school-lunch account, including sign-in, students, lunch calendar, cart, orders, deliveries, and payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with a My Hot Lunchbox account use this skill to script account reads and cautiously prepare account changes when the MCP server is unavailable. It is especially suited to shell workflows that need curl examples, endpoint notes, and payload guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shell/API commands can change lunch-account data or charge a saved payment card.

Mitigation: Review the full payload and payment total before any mutation or checkout, and prefer the MCP flow for mutations because it provides confirmation controls.

Risk: Repeated failed password sign-ins can escalate to a CAPTCHA and remove server-side sign-in for the account.

Mitigation: Stop after an invalid_grant response and check credentials instead of retrying.

Risk: Write request bodies are documented as unverified, and missing fields in read-modify-write payloads may clear existing account data.

Mitigation: Fetch the current model, inspect the edited payload, post it only after review, and re-read the resource afterward to confirm the result.

## Reference(s):

- [My Hot Lunchbox endpoints](references/endpoints.md)
- [My Hot Lunchbox API host](https://ordernow.myhotlunchbox.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/myhotlunchbox-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell command examples and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include curl and jq snippets that require user-provided credentials and review before execution.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
