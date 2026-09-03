## Description:

Canonry helps agents operate the `cnry` / `canonry` CLI for AEO workflows, including project setup, provider integrations, sweeps, audits, indexing, traffic sources, and mention/citation reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and agency operators use this skill to guide agent-driven Canonry CLI work for answer engine optimization, search/indexing diagnostics, traffic source setup, and reporting. It is intended for operators who already plan to run Canonry locally and connect relevant marketing or business accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad local and third-party marketing or business account access through Canonry.

Mitigation: Install it only when you intend to run Canonry locally and connect those accounts; prefer scoped or read-only keys where possible.

Risk: Canonry configuration may contain sensitive local credentials or API keys.

Mitigation: Protect ~/.canonry/config.yaml with restrictive permissions and avoid sharing it in logs, chat, or backups.

Risk: Mutations, schedules, live provider reads, WordPress actions, and ads actions can affect connected services or consume quota.

Mitigation: Review each requested action before approval and use dry-run or stored-read paths when available.

## Reference(s):

- [ClawHub canonry skill page](https://clawhub.ai/arberx/skills/canonry)
- [Canonry website](https://canonry.ai)
- [Canonry documentation](https://github.com/Canonry/canonry)
- [AINYC AEO Methodology](https://ainyc.ai/aeo-methodology)
- [AEO Analysis: Interpreting Canonry Results](references/aeo-analysis.md)
- [Canonry CLI Reference](references/canonry-cli.md)
- [Google Business Profile Integration](references/google-business-profile.md)
- [Google Ads and Google Tag Manager](references/google-marketing.md)
- [Indexing Workflows for AEO](references/indexing.md)
- [Server-side traffic (AI Visibility - Server-Side)](references/server-side-traffic.md)
- [WordPress Integration](references/wordpress-integration.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with CLI command examples and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 22.14+ and a globally installed @canonry/canonry runtime.]

## Skill Version(s):

4.178.2+d76fb5a (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
