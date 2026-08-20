## Description:

Use ezBookkeeping API Tools script to record new transactions, query transactions, retrieve account information, retrieve categories, retrieve tags, and retrieve exchange rate data in the self hosted personal finance application ezBookkeeping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mayswind](https://clawhub.ai/user/mayswind)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate a self-hosted ezBookkeeping instance for personal-finance workflows, including recording transactions, querying accounts, categories, and tags, and retrieving exchange-rate data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scripts can make authenticated financial or session-changing API calls, including adding records or revoking tokens.

Mitigation: Use a least-privilege ezBookkeeping API token when available and require confirmation before running commands that add records or revoke tokens.

Risk: The scripts can load EBKTOOL_SERVER_BASEURL and EBKTOOL_TOKEN from nearby .env files.

Mitigation: Prefer explicit environment variables, keep .env files secured, and run the scripts only from trusted directories and repositories.

## Reference(s):

- [ezBookkeeping API Tools OpenClaw page](https://ezbookkeeping.mayswind.net/agent/openclaw)
- [ezBookkeeping](https://ezbookkeeping.mayswind.net)
- [ClawHub skill page](https://clawhub.ai/mayswind/skills/ezbookkeeping)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell or PowerShell commands; API results may be returned as JSON or Markdown tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires EBKTOOL_SERVER_BASEURL and EBKTOOL_TOKEN; supports optional timezone settings and raw JSON responses.]

## Skill Version(s):

2.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
