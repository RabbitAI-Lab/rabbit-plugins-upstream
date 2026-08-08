## Description:

Set up and operate Canonry AEO projects: inspect mention and citation coverage, diagnose regressions, run technical audits, and act through the Canonry CLI or MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and AEO operators use this skill to run Canonry workflows for AI visibility measurement, indexing diagnosis, technical audits, reporting, and approved operational changes through the Canonry CLI or MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate real Canonry projects, WordPress sites, ads, webhooks, schedules, and integrations.

Mitigation: Require explicit operator approval for every site edit, ads action, webhook change, schedule change, and quota-consuming run; prefer read-only or dry-run actions where possible.

Risk: Canonry credentials and connected-service secrets may be stored in ~/.canonry/config.yaml.

Mitigation: Protect the config file, never print or paste secrets, and prefer read-only or project-scoped keys whenever the task allows.

Risk: A write-capable key can expose write tools and may affect shared instance settings.

Mitigation: Use the narrowest available credential scope and do not work around missing tools or authorization errors by switching credentials.

Risk: Visibility sweeps, probes, syncs, and provider operations can consume quota or create persistent records.

Mitigation: Get approval for each bounded run, avoid tight retry loops, and clearly distinguish probes from metric-producing sweeps.

## Reference(s):

- [Canonry website](https://canonry.ai)
- [Canonry documentation](https://github.com/Canonry/canonry)
- [AINYC AEO Methodology](https://ainyc.ai/aeo-methodology)
- [AEO Analysis: Interpreting Canonry Results](references/aeo-analysis.md)
- [Canonry CLI Reference](references/canonry-cli.md)
- [Indexing Workflows for AEO](references/indexing.md)
- [WordPress Integration](references/wordpress-integration.md)
- [Server-side traffic (AI Visibility - Server-Side)](references/server-side-traffic.md)
- [Google Business Profile Integration](references/google-business-profile.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON or JSONL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or run Canonry operations only within the operator's approved credential scope and approval boundaries.]

## Skill Version(s):

4.154.1+578a1dc (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
