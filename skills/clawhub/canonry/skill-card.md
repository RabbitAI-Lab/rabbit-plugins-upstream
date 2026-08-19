## Description:

Operate Canonry (the `cnry` / `canonry` CLI) for AEO tasks including project setup, provider integrations, sweeps, mention and citation analysis, technical audits, indexing submissions, server-side traffic, and related diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, marketers, and operations teams use this skill to guide an agent through Canonry CLI workflows for answer engine optimization, provider setup, measurement, technical audits, indexing, traffic evidence, and guarded content or ads operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide operations that use local provider credentials and Canonry API keys.

Mitigation: Keep ~/.canonry/config.yaml private, avoid syncing it into dotfiles or backups, and prefer scoped or read-only keys where possible.

Risk: Approved operations may change WordPress content, schedules, indexing submissions, traffic sources, or ads state.

Mitigation: Review every live read, probe, schedule, webhook, and mutation before approving it, and use dry-run previews where available.

Risk: Quota-consuming sweeps and provider probes can affect persisted measurement data or consume API quota.

Mitigation: Require explicit approval for sweeps, probes, and live provider reads, and bound any requested batch before execution.

Risk: Configuration changes can expose credentials or disrupt a Canonry installation.

Mitigation: Do not print raw keys or config contents, back up config before edits, and avoid replacing credentials to work around missing authorization.

## Reference(s):

- [Canonry Skill](SKILL.md)
- [Canonry CLI Reference](references/canonry-cli.md)
- [AEO Analysis: Interpreting Canonry Results](references/aeo-analysis.md)
- [Indexing Workflows for AEO](references/indexing.md)
- [WordPress Integration](references/wordpress-integration.md)
- [Server-side traffic (AI Visibility - Server-Side)](references/server-side-traffic.md)
- [Google Business Profile Integration](references/google-business-profile.md)
- [Google Ads and Google Tag Manager](references/google-marketing.md)
- [Canonry Website](https://canonry.ai)
- [Canonry Docs Repository](https://github.com/Canonry/canonry)
- [AINYC AEO Methodology](https://ainyc.ai/aeo-methodology)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, JSON-oriented command outputs, and review recommendations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or run Canonry CLI operations only within the agent's approval and credential boundaries.]

## Skill Version(s):

4.172.4+34bb80b (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
