## Description:

Health monitoring for AI agent infrastructure. Checks API key validity, wallet gas balances, and service endpoint reachability, and sends threshold-based alerts via Telegram/Discord. No mining, earning, revenue reporting, or background workers — this skill only observes and alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[manteclaw](https://clawhub.ai/user/manteclaw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use the skill to check configured API keys, service reachability, and wallet gas balances, then receive threshold-based alerts when checks fail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports unpinned dependencies and incomplete scan evidence because some referenced paths could not be resolved.

Mitigation: Review dependency sources and pin versions before installation; assess the permissions and credentials the setup requires.

Risk: Telegram and Discord alerts include operational details such as service failures, truncated wallet addresses, balances, and short error details.

Mitigation: Use a private chat or channel and restrict access to the bot token or webhook; leave remote alert channels unconfigured for local-only output.

## Reference(s):

- [Configuration reference](CONFIGURATION.md)
- [Alert Configuration Guide](references/alert-config.md)
- [ClawHub skill page](https://clawhub.ai/manteclaw/skills/agent-health-monitor)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Plain-text status and alert messages, optional JSON export, and Markdown setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Checks and alert channels are configured through environment variables.]

## Skill Version(s):

1.0.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
