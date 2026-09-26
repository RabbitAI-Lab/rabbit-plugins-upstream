## Description:

Helps agents use ezBookkeeping APIs to record and query transactions and retrieve accounts, categories, tags, and exchange rates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mayswind](https://clawhub.ai/user/mayswind)

### License/Terms of Use:

MIT-0

## Use Case:

People using a self-hosted ezBookkeeping instance can ask an agent to look up financial records or create bookkeeping entries through its API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Nearby .env files may silently provide the server URL and API token for authenticated financial requests.

Mitigation: Use only in trusted workspaces; explicitly set both settings from the same trusted source, avoid repository or parent-directory .env files, and check the printed API URL before running commands.

Risk: An untrusted server endpoint could receive the API token or financial information.

Mitigation: Verify the destination server and prefer HTTPS.

Risk: Add commands can immediately modify bookkeeping records.

Mitigation: Review the intended record and command arguments before execution.

## Reference(s):

- [ezBookkeeping OpenClaw integration](https://ezbookkeeping.mayswind.net/agent/openclaw)
- [ezBookkeeping](https://ezbookkeeping.mayswind.net)
- [ClawHub skill listing](https://clawhub.ai/mayswind/skills/ezbookkeeping)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with command examples and API response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated API results may contain financial information; add commands can change bookkeeping records.]

## Skill Version(s):

2.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
