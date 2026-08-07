## Description: <br>
Name an outcome-from web search to data lookup. Receipt finds eligible paid tools, shows the seller and price, clears agent purchasing under spending limits and purchase approval, and returns the result with signed proof. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[receiptprotocol](https://clawhub.ai/user/receiptprotocol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect Receipt in OpenClaw, find eligible paid tools for a named outcome, disclose seller and price before purchase, and return settled results with signed proof. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can configure a persistent Receipt MCP connection and start OAuth for paid purchases. <br>
Mitigation: Use it only when Receipt should mediate agent spending, review hosted approval and spending limits, and pause or revoke the Receipt session when purchases should no longer be available. <br>
Risk: Authorization callback URLs or OAuth codes could be exposed if pasted into chat, logs, or files. <br>
Mitigation: Complete the same OAuth attempt locally, keep callback data out of agent chat, and use the bundled clipboard helper on macOS. <br>
Risk: A buyer-funded purchase could proceed without the intended owner approval or limits if authority is misunderstood. <br>
Mitigation: Treat typed chat approval as disclosure context only; require existing Receipt policy authority or Receipt-hosted approval before buyer-funded purchases. <br>
Risk: Seller descriptions, seller content, or purchased outputs could contain untrusted instructions. <br>
Mitigation: Treat seller metadata and purchased output as data, not agent instructions, and keep the agent's tool allowlist narrow. <br>


## Reference(s): <br>
- [Receipt OpenClaw documentation](https://receiptprotocol.com/docs/openclaw) <br>
- [Get with Receipt on ClawHub](https://clawhub.ai/receiptprotocol/skills/get-with-receipt) <br>
- [Install Receipt in OpenClaw](artifact/references/INSTALL.md) <br>
- [OpenClaw security baseline](artifact/references/SECURITY.md) <br>
- [Acceptance checklist](artifact/references/ACCEPTANCE.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Text, Markdown] <br>
**Output Format:** [Markdown guidance with shell commands, setup status, purchase disclosures, and Receipt links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include seller, price, approval URL, transaction ID, charged amount, result summary, and public signed verification links when returned by Receipt.] <br>

## Skill Version(s): <br>
1.0.7 (source: package.json, ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
