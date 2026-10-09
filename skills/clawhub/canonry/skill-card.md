## Description:

Guides agents using Canonry to inspect AI visibility evidence, diagnose changes, plan measurement, review integrations, and report results through connected tools or the optional CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and developers use this skill to interpret stored Canonry measurements, investigate changes in AI visibility, review connected marketing integrations, and prepare scoped operational plans and reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live reads, research runs, and syncs may consume provider quota or change stored evidence.

Mitigation: Start with stored evidence and obtain explicit, bounded approval before quota-spending or live actions.

Risk: Writes, deployments, ads actions, and webhook or telemetry changes may have external effects.

Mitigation: Require approval for the exact target and action; inspect saved state or operation receipts before retrying an uncertain write.

Risk: Canonry credentials or configuration may expose sensitive access if shared.

Mitigation: Use read-only or project-scoped keys where possible; keep API keys and ~/.canonry/config.yaml out of chat, source control, and shared backups.

Risk: Missing or incomparable measurements may produce misleading reports.

Mitigation: State missing inputs and preserve time windows, providers, sample sizes, and distinct mention and citation signals.

## Reference(s):

- [Canonry skill release](https://clawhub.ai/arberx/skills/canonry)
- [Canonry CLI reference](references/canonry-cli.md)
- [AEO analysis guide](references/aeo-analysis.md)
- [Indexing workflow](references/indexing.md)
- [Google marketing integration](references/google-marketing.md)
- [Google Marketing setup guide](https://github.com/Canonry/canonry/blob/main/docs/google-marketing.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations should state evidence scope and seek approval before live or modifying actions.]

## Skill Version(s):

7.17.0+292663b (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
