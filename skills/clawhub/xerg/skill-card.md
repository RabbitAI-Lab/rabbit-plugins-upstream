## Description:

Audit and reduce AI agent runtime spend in dollars. Use for AI costs, agent spend, token waste, runtime attribution, detector coverage, and FinOps. Works with OpenClaw, Hermes, QM, Claude Code, Cursor, and generic event ingest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xerg](https://clawhub.ai/user/xerg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and FinOps teams use Xerg to audit AI agent runtime spend, identify waste patterns, report detector coverage, and compare compatible fixes in supported local or explicitly provided runtime data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill drives a third-party CLI that reads selected local or remote AI runtime data.

Mitigation: Install and run it only when that data access is acceptable; run doctor first, keep audits local by default, and review the reported sources before auditing.

Risk: Hosted activation or push can send audit summaries to Xerg Cloud.

Mitigation: Require explicit user approval before activation, push, or hosted MCP setup, and use workspace-bound activation when an exact organization is intended.

Risk: Secrets such as workspace keys, DSNs, provider credentials, Fly tokens, or Xerg API keys could be exposed if copied into chat or commands.

Mitigation: Never request or paste secrets in chat; use browser pairing, owner-only local storage, private administrator scopes, or CI secret managers.

Risk: Runtime costs may be observed, locally estimated, or unpriced rather than invoice-authoritative.

Mitigation: Present spend results with their coverage and pricing status, and do not describe modeled runtime spend as provider billing reconciliation.

## Reference(s):

- [Xerg documentation](https://xerg.ai/docs)
- [Xerg skill source](https://xerg.ai/skill.md)
- [Xerg homepage](https://xerg.ai)
- [Xerg service status](https://status.xerg.ai)
- [@xerg/cli npm package](https://www.npmjs.com/package/@xerg/cli)
- [ClawHub skill page](https://clawhub.ai/xerg/skills/xerg)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and summarized JSON audit results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local audit output may include dollar totals, detector coverage, findings, recommendations, per-agent spend, and compare deltas; hosted push is optional and approval-gated.]

## Skill Version(s):

0.19.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
