## Description:

Use ezBookkeeping API Tools script to record new transactions, query transactions, retrieve account information, retrieve categories, retrieve tags, and retrieve exchange rate data in the self hosted personal finance application ezBookkeeping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mayswind](https://clawhub.ai/user/mayswind)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and personal finance users use this skill to let an agent call ezBookkeeping APIs for account, transaction, category, tag, token, and exchange-rate workflows on a configured self-hosted ezBookkeeping server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scripts can use credentials from nearby .env files and send authenticated financial API requests to any configured ezBookkeeping server URL.

Mitigation: Set EBKTOOL_SERVER_BASEURL and EBKTOOL_TOKEN explicitly in a trusted environment, prefer HTTPS URLs, and avoid running the tools from untrusted workspaces.

Risk: Some commands can modify financial records or revoke tokens.

Mitigation: Review write actions and token-revoke commands before allowing an agent to execute them.

## Reference(s):

- [ezBookkeeping](https://ezbookkeeping.mayswind.net)
- [ezBookkeeping OpenClaw agent page](https://ezbookkeeping.mayswind.net/agent/openclaw)
- [ClawHub skill page](https://clawhub.ai/mayswind/skills/ezbookkeeping)

## Skill Output:

**Output Type(s):** [shell commands, markdown, configuration, guidance]

**Output Format:** [Markdown with shell and PowerShell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires EBKTOOL_SERVER_BASEURL and EBKTOOL_TOKEN for authenticated API calls.]

## Skill Version(s):

2.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
