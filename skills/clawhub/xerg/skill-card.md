## Description:

Audit and reduce AI agent runtime spend in dollars. Use for AI costs, agent spend, token waste, runtime attribution, detector coverage, and FinOps. Works with OpenClaw, Hermes, QM, Claude Code, Cursor, and generic event ingest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xerg](https://clawhub.ai/user/xerg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineering managers, and FinOps teams use Xerg to audit AI agent runtime spend, identify evidence-strict waste, inspect neutral cost signals, and compare fixes across supported agent runtimes and exported event payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local audits may read AI runtime logs, transcripts, exports, state databases, or ingest payloads that can contain sensitive operational data.

Mitigation: Use local audit mode first, approve local data inspection explicitly, and review the command before execution.

Risk: Hosted pairing or push can send audit summaries to Xerg Cloud when explicitly approved.

Mitigation: Do not run hosted pairing, push, connect, or MCP setup unless the user has approved that hosted action.

Risk: Runtime costs are observed, locally estimated, or unpriced and are not authoritative provider invoices.

Mitigation: Describe pricing coverage and unpriced areas clearly, and avoid presenting modeled runtime spend as billing reconciliation.

Risk: Advanced credentials such as XERG_API_KEY are intended for non-interactive CI or automation.

Mitigation: Store credentials in a secret manager and do not place keys in chat, source files, logs, URLs, or inline shell commands.

## Reference(s):

- [Xerg homepage](https://xerg.ai)
- [Xerg documentation](https://xerg.ai/docs)
- [Xerg skill source](https://xerg.ai/skill.md)
- [Xerg service status](https://status.xerg.ai)
- [@xerg/cli npm package](https://www.npmjs.com/package/@xerg/cli)
- [OpenSSH](https://www.openssh.com/)
- [rsync](https://rsync.samba.org/)
- [Fly CLI documentation](https://fly.io/docs/flyctl/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-oriented audit guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides local audit execution, summarizes spend findings, and recommends follow-up commands only after user approval.]

## Skill Version(s):

0.24.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
