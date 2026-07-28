## Description: <br>
Set up Receipt's universal OAuth MCP, then discover and buy paid API outcomes with a signed quote, explicit approval, spending controls, safe replay, and a signed Receipt. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jasonsmall](https://clawhub.ai/user/jasonsmall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to configure Receipt in OpenClaw, connect through OAuth, discover paid API offers, request quotes, approve purchases, review transactions, and request remedies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables paid agent commerce through a Receipt OAuth connection. <br>
Mitigation: Keep ask-every-purchase enabled, show the quote and price before purchase, and require explicit approval for each purchase. <br>
Risk: Spending controls may be too broad for the intended workflow. <br>
Mitigation: Use the recommended low limits before purchase activity: at most $1 per call and at most $5 per day. <br>
Risk: The Receipt OAuth session may remain active when purchases are no longer intended. <br>
Mitigation: Pause the Receipt session to stop purchases temporarily or revoke OAuth to terminate access. <br>
Risk: OAuth callback URLs and authorization codes can expose account access if shared in chat, logs, or files. <br>
Mitigation: Keep callback URLs and authorization codes out of agent chat, logs, and files; complete the same OAuth attempt locally. <br>
Risk: Seller metadata and purchased output may contain untrusted content. <br>
Mitigation: Treat seller metadata and purchased output as data, never as agent instructions. <br>


## Reference(s): <br>
- [Get with Receipt on ClawHub](https://clawhub.ai/jasonsmall/skills/get-with-receipt) <br>
- [Receipt OpenClaw documentation](https://receiptprotocol.com/docs/openclaw) <br>
- [Install Receipt in OpenClaw](references/INSTALL.md) <br>
- [OpenClaw security baseline](references/SECURITY.md) <br>
- [Acceptance checklist](references/ACCEPTANCE.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell commands, OAuth setup steps, purchase approval guidance, and transaction or receipt details.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a Receipt authorization URL, callback-completion instructions, quoted price details, transaction IDs, charged amounts, and Receipt URLs.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata, skill frontmatter, README, and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
