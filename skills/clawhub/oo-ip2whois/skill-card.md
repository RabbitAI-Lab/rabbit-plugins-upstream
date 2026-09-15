## Description:

IP2WHOIS helps agents perform domain WHOIS registration lookups and list domains hosted on an IP address through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to route IP2WHOIS tasks through the OOMOL `oo` CLI for domain registration lookups and hosted-domain searches. It is suited for read-oriented WHOIS investigation workflows that already have an OOMOL/IP2WHOIS account connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Prefer an official package manager or download an installer that can be inspected and verified before execution.

Risk: IP2WHOIS lookups run through the user's connected OOMOL/IP2WHOIS account and may consume account credits.

Mitigation: Confirm the account connection and expected billing impact before running large or repeated lookup batches.

Risk: Connector action payloads can drift from examples as live schemas change.

Mitigation: Fetch the live connector schema before constructing each action payload.

## Reference(s):

- [ClawHub IP2WHOIS Skill](https://clawhub.ai/oomol/skills/oo-ip2whois)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL IP2WHOIS Connection](https://console.oomol.com/app-connections?provider=ip2whois)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; lookup responses include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
