## Description:

Audit and reduce AI agent runtime spend in dollars. Use for AI costs, agent spend, token waste, runtime attribution, detector coverage, and FinOps. Works with OpenClaw, Hermes, QM, Claude Code, Cursor, and generic event ingest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xerg](https://clawhub.ai/user/xerg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and FinOps teams use Xerg to audit local or explicitly provided AI runtime data, identify evidence-strict waste findings, review neutral usage signals, and compare compatible fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to inspect local AI runtime logs, transcripts, exports, or snapshots.

Mitigation: Use only the specific data sources the user approves, and keep audits local unless the user explicitly approves hosted pairing or upload.

Risk: Hosted pairing, push, QM, remote, or credential-related workflows can involve sensitive operational access.

Mitigation: Require explicit approval for those workflows, review requested commands carefully, and keep credentials in appropriate secret storage rather than chat or command text.

Risk: Runtime cost estimates can be observed, locally estimated, or unpriced rather than invoice-authoritative.

Mitigation: Present pricing coverage and limitations with audit results, and do not treat Xerg runtime totals as provider bills or invoice reconciliation.

## Reference(s):

- [Xerg Homepage](https://xerg.ai)
- [Xerg Documentation](https://xerg.ai/docs)
- [Xerg Skill](https://xerg.ai/skill.md)
- [Xerg Service Status](https://status.xerg.ai)
- [@xerg/cli npm Package](https://www.npmjs.com/package/@xerg/cli)
- [OpenSSH](https://www.openssh.com/)
- [rsync](https://rsync.samba.org/)
- [Fly CLI Documentation](https://fly.io/docs/flyctl/)
- [Railway CLI Repository](https://github.com/railwayapp/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask for approval before package fetches, local data inspection, hosted pairing, or uploads; local audit results are not provider invoices.]

## Skill Version(s):

0.31.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
