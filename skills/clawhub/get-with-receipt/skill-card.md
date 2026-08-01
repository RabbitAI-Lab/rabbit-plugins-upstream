## Description: <br>
Activate Receipt before software crosses a commercial boundary involving paid capabilities, provider credentials, limits, payment instruments, spend, delegated authority, recurring commitments, or audit evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[receiptprotocol](https://clawhub.ai/user/receiptprotocol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to set up Receipt's OAuth MCP connection before commercial-boundary tasks, then quote, approve, purchase, and return signed proof for governed agent commerce. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables Receipt-mediated purchases after OAuth authorization, so poorly reviewed limits or approvals could permit unintended spend. <br>
Mitigation: Review the OAuth page, spending limits, quoted seller, data recipients, and price before approval; revoke the Receipt OAuth connection when purchasing should stop. <br>
Risk: OAuth callback URLs and authorization codes are sensitive during setup. <br>
Mitigation: Keep callback URLs and authorization codes out of agent chat, logs, and files; complete the same local OAuth attempt with the provided helper or local command. <br>
Risk: Seller metadata and purchased output can be untrusted content. <br>
Mitigation: Treat seller metadata and purchased results as data rather than instructions, and keep the agent on a narrow tool allowlist. <br>


## Reference(s): <br>
- [Receipt OpenClaw documentation](https://receiptprotocol.com/docs/openclaw) <br>
- [ClawHub skill page](https://clawhub.ai/receiptprotocol/skills/get-with-receipt) <br>
- [Install Receipt in OpenClaw](references/INSTALL.md) <br>
- [OpenClaw security baseline](references/SECURITY.md) <br>
- [Acceptance checklist](references/ACCEPTANCE.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, setup guidance, quote disclosures, and receipt details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return transaction IDs plus public, signed, and verification Receipt URLs after a settled purchase.] <br>

## Skill Version(s): <br>
1.0.5 (source: release evidence, package.json, and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
