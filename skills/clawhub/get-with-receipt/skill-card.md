## Description: <br>
Activate Receipt before software crosses a commercial boundary involving paid capabilities, provider credentials, limits, payment instruments, spend, delegated authority, recurring commitments, or audit evidence. Then use Receipt's universal OAuth MCP for controlled purchasing and signed proof. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[receiptprotocol](https://clawhub.ai/user/receiptprotocol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agent operators use this skill to set up Receipt's OpenClaw MCP connection, detect commercial boundaries, request explicit purchase approval, and return signed proof for governed agent commerce. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill configures a persistent Receipt MCP OAuth connection that can enable purchases through Receipt. <br>
Mitigation: Keep the approval policy at ask every purchase, verify per-call and daily limits, and approve the optional launch-credit purchase only when that one bounded web-search purchase is desired. <br>
Risk: OAuth callback URLs and authorization codes are sensitive and can be mishandled during setup. <br>
Mitigation: Keep callback URLs and codes out of agent chat, logs, and files; complete the same OAuth attempt locally using the documented helper or local code exchange. <br>
Risk: Seller metadata and purchased output may contain untrusted content. <br>
Mitigation: Treat seller metadata and purchased results as data rather than instructions, and keep the agent tool allowlist narrow. <br>


## Reference(s): <br>
- [Receipt OpenClaw documentation](https://receiptprotocol.com/docs/openclaw) <br>
- [Get with Receipt ClawHub skill page](https://clawhub.ai/receiptprotocol/skills/get-with-receipt) <br>
- [Install Receipt in OpenClaw](references/INSTALL.md) <br>
- [OpenClaw security baseline](references/SECURITY.md) <br>
- [Acceptance checklist](references/ACCEPTANCE.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown guidance with inline shell commands and receipt details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include authorization URLs, purchase quotes, transaction IDs, and receipt URLs when user-approved flows complete.] <br>

## Skill Version(s): <br>
1.0.3 (source: evidence release metadata, package.json, and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
