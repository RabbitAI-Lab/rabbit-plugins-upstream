## Description: <br>
Connect Receipt once, then discover and buy paid tools with spending limits, purchase approval, delivery checks, and signed proof. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[receiptprotocol](https://clawhub.ai/user/receiptprotocol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to connect a Receipt MCP commerce account, discover paid tools, quote purchases, require approval for buyer-funded spending, and return signed proof of completed transactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: OAuth callback codes or authorization details could be exposed in chat, logs, or files. <br>
Mitigation: Review the OAuth screen, keep callback codes out of chat, and use the documented local completion flow. <br>
Risk: Buyer-funded purchases could proceed without clear spending controls. <br>
Mitigation: Use low per-call and daily spending limits and rely on the Receipt-hosted approval page before buyer-funded purchases. <br>
Risk: Seller metadata or purchased output may be untrusted. <br>
Mitigation: Treat seller-provided metadata and purchased results as data, not agent instructions. <br>


## Reference(s): <br>
- [Receipt OpenClaw documentation](https://receiptprotocol.com/docs/openclaw) <br>
- [Install Receipt in OpenClaw](references/INSTALL.md) <br>
- [OpenClaw security baseline](references/SECURITY.md) <br>
- [Acceptance checklist](references/ACCEPTANCE.md) <br>
- [ClawHub skill page](https://clawhub.ai/receiptprotocol/skills/get-with-receipt) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and returned Receipt transaction details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include authorization URLs, quote details, spending limits, transaction IDs, validation status, and public, signed, or verification Receipt URLs.] <br>

## Skill Version(s): <br>
1.0.6 (source: server evidence release.version, metadata.openclaw.version, and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
