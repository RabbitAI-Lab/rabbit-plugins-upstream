## Description:

Audit and reduce AI agent runtime spend in dollars. Use for AI costs, agent spend, token waste, runtime attribution, detector coverage, and FinOps. Works with OpenClaw, Hermes, QM, Claude Code, Cursor, and generic event ingest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xerg](https://clawhub.ai/user/xerg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, AI platform operators, and FinOps teams use Xerg to run local AI runtime spend audits, attribute agent costs, identify evidence-strict waste, and compare fixes across OpenClaw, Hermes, QM, Claude Code, Cursor, and exported event payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inspect local agent logs, databases, snapshots, transcripts, exports, or ingest payloads during an audit.

Mitigation: Ask for explicit permission before reading local runtime data, confirm the intended source, and describe local-only audit behavior before running analysis.

Risk: Hosted pairing or push commands intentionally send summarized audit data to Xerg.

Mitigation: Run hosted pairing, connect, push, or MCP setup only after explicit user approval and keep local audits as the default path.

Risk: The first-run path may fetch and execute the published @xerg/cli package through npm or npx.

Mitigation: Ask separately before any npm download or install, then run doctor in JSON mode and follow the returned recommended command instead of reconstructing it.

Risk: Runtime costs may be observed, locally estimated, or unpriced rather than authoritative provider invoices.

Mitigation: Present pricing coverage and limitations before conclusions, avoid treating modeled runtime spend as invoice reconciliation, and disclose unpriced usage.

## Reference(s):

- [Xerg homepage](https://xerg.ai)
- [Xerg documentation](https://xerg.ai/docs)
- [Xerg skill source](https://xerg.ai/skill.md)
- [Xerg service status](https://status.xerg.ai)
- [@xerg/cli npm package](https://www.npmjs.com/package/@xerg/cli)
- [OpenSSH](https://www.openssh.com/)
- [rsync](https://rsync.samba.org/)
- [Flyctl documentation](https://fly.io/docs/flyctl/)
- [ClawHub skill page](https://clawhub.ai/xerg/skills/xerg)
- [ClawHub publisher profile](https://clawhub.ai/user/xerg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local audit summaries, detector coverage, and suggested next commands; hosted pairing or push commands require explicit user approval.]

## Skill Version(s):

0.27.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
