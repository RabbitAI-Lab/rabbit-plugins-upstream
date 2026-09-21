## Description:

Navigate Canonry through connected MCP tools or the `cnry` CLI to inspect evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and marketing teams use this skill to operate Canonry through MCP or the CLI, inspect AI visibility evidence, diagnose changes, plan measurement, review integrations, and prepare reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Canonry workflows can involve public-site edits, ads changes, schedules, webhooks, provider syncs, or live quota-consuming reads.

Mitigation: Review commands before running them and get explicit approval for the exact target, action, and bounded work.

Risk: Credentials, API keys, app passwords, and local Canonry configuration can be exposed if copied into chat, transcripts, or reports.

Mitigation: Keep secrets in secure setup flows, protect ~/.canonry/config.yaml, and prefer read-only or project-scoped credentials.

Risk: AI visibility evidence can be misread when missing data, stale samples, mention signals, and citation signals are combined incorrectly.

Mitigation: Use server-returned metrics, preserve provider and time-window context, and report missing evidence separately from negative results.

## Reference(s):

- [AEO Analysis: Interpreting Canonry Results](references/aeo-analysis.md)
- [Canonry CLI Reference](references/canonry-cli.md)
- [Google Business Profile Integration](references/google-business-profile.md)
- [Google Ads and Google Tag Manager](references/google-marketing.md)
- [Indexing Workflows for AEO](references/indexing.md)
- [Server-side traffic (AI Visibility - Server-Side)](references/server-side-traffic.md)
- [WordPress Integration](references/wordpress-integration.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are scoped to Canonry MCP or CLI workflows and approval-bound operations.]

## Skill Version(s):

5.6.0+f2d9ae1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
