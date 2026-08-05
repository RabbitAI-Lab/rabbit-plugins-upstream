## Description:

Set up and operate Canonry AEO projects: inspect mention and citation coverage, diagnose regressions, run technical audits, and act through the Canonry CLI or MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, developers, and marketing or SEO teams use this skill to operate Canonry AEO projects, track AI mention and citation visibility, diagnose regressions, run audits, and manage integrations through CLI-oriented workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help operate connected Canonry sites and services with broad read and write capabilities.

Mitigation: Use read-only or project-scoped keys when possible and review every write, schedule, webhook, browser connection, and ads action before approval.

Risk: Local Canonry configuration can contain API keys, OAuth tokens, and WordPress credentials.

Mitigation: Protect ~/.canonry/config.yaml, never paste credentials into chat, and avoid printing raw configuration or API keys.

Risk: Quota-consuming sweeps and live integrations can change persisted project state or consume external service quota.

Mitigation: Prefer reads and dry runs first, then require explicit approval before sweeps, mutations, WordPress changes, or ads actions.

## Reference(s):

- [Canonry Website](https://canonry.ai)
- [Canonry Documentation](https://github.com/Canonry/canonry)
- [AINYC AEO Methodology](https://ainyc.ai/aeo-methodology)
- [AEO Analysis](references/aeo-analysis.md)
- [Canonry CLI Reference](references/canonry-cli.md)
- [Google Business Profile Integration](references/google-business-profile.md)
- [Indexing Workflows for AEO](references/indexing.md)
- [Server-side Traffic](references/server-side-traffic.md)
- [WordPress Integration](references/wordpress-integration.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline shell commands, JSON snippets, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose actions that require explicit operator approval before execution.]

## Skill Version(s):

4.148.0+74f3be3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
