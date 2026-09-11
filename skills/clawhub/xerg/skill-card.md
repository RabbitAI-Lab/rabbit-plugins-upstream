## Description:

Audit and reduce AI agent runtime spend in dollars. Use for AI costs, agent spend, token waste, runtime attribution, detector coverage, and FinOps. Works with OpenClaw, Hermes, QM, Claude Code, Cursor, and generic event ingest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xerg](https://clawhub.ai/user/xerg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineering managers, and FinOps teams use this skill to audit local or approved remote AI-agent runtime data, attribute spend, identify evidence-strict waste, and compare compatible remediation results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approved audits can let the pinned closed-source npm CLI inspect sensitive agent runtime logs or snapshots.

Mitigation: Install only after approval, run local audits in a restricted environment when possible, and approve uploads separately.

Risk: Hosted sync may share summarized audit data with Xerg Cloud.

Mitigation: Use hosted pairing or push only when the summarized audit data is appropriate to share, and avoid exposing API keys in chat or shell history.

Risk: Runtime costs are observed, locally estimated, or unpriced rather than authoritative provider invoices.

Mitigation: Present audit spend as runtime analysis, preserve pricing-coverage limitations, and avoid using it as invoice reconciliation evidence.

## Reference(s):

- [Xerg homepage](https://xerg.ai)
- [Xerg documentation](https://xerg.ai/docs)
- [Xerg skill source](https://xerg.ai/skill.md)
- [Xerg service status](https://status.xerg.ai)
- [@xerg/cli npm package](https://www.npmjs.com/package/@xerg/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON-producing CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local audit results may include spend summaries, detector coverage, findings, neutral signals, and compare deltas; hosted upload is optional and permission-gated.]

## Skill Version(s):

0.33.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
