## Description:

Audit and reduce AI agent runtime spend in dollars. Use for AI costs, agent spend, token waste, runtime attribution, detector coverage, and FinOps. Works with OpenClaw, Hermes, QM, Claude Code, Cursor, and generic event ingest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xerg](https://clawhub.ai/user/xerg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineering managers, and FinOps teams use this skill to run local Xerg CLI audits, identify evidence-strict AI runtime waste, review detector coverage, and compare compatible fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide the Xerg CLI to read local agent runtime records and cost-related logs.

Mitigation: Run local audits only in workspaces where that data access is acceptable, and review the CLI doctor output before auditing.

Risk: Hosted sync, push, and credential persistence can occur after explicit user approval.

Mitigation: Keep audits local by default and require a clear approval step before activation, push, or hosted MCP setup.

Risk: Using npx fetches and executes the published @xerg/cli package.

Mitigation: Review npm package trust implications or install a reviewed CLI version globally when repeated execution is needed.

Risk: Runtime cost findings are observed or locally estimated and are not authoritative provider invoices.

Mitigation: Present Xerg output as runtime audit evidence and avoid treating modeled spend as billing reconciliation.

## Reference(s):

- [Xerg Documentation](https://xerg.ai/docs)
- [Xerg Skill Source](https://xerg.ai/skill.md)
- [Xerg Homepage](https://xerg.ai)
- [Xerg Service Status](https://status.xerg.ai)
- [@xerg/cli npm Package](https://www.npmjs.com/package/@xerg/cli)
- [ClawHub Skill Page](https://clawhub.ai/xerg/skills/xerg)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, JSON, Configuration]

**Output Format:** [Markdown guidance with shell commands and JSON audit-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-first audit workflow; hosted sync and credential persistence require explicit user approval.]

## Skill Version(s):

0.20.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
