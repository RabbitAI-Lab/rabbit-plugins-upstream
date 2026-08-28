## Description:

Audit and reduce AI agent runtime spend in dollars. Use for AI costs, agent spend, token waste, runtime attribution, detector coverage, and FinOps. Works with OpenClaw, Hermes, QM, Claude Code, Cursor, and generic event ingest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xerg](https://clawhub.ai/user/xerg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineering managers, and FinOps teams use Xerg to audit AI-agent runtime costs, identify evidence-backed waste, and compare compatible fixes across supported local sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local audits may inspect AI agent logs, transcripts, usage exports, or runtime databases that can expose sensitive work patterns or content-derived metadata.

Mitigation: Ask for separate approval before local data access, keep analysis local by default, and summarize only the audit results the user approved.

Risk: Hosted push can share audit totals, rollups, source metadata, findings, recommendations, and comparison deltas with Xerg Cloud.

Mitigation: Run hosted pairing or push only after explicit approval, and explain what categories of audit data will be shared before upload.

Risk: Runtime costs may be observed, locally estimated, or unpriced and are not authoritative provider invoices.

Mitigation: Describe audit totals as runtime spend evidence rather than invoice reconciliation, and call out unpriced or limited-estimate coverage before conclusions.

## Reference(s):

- [Xerg homepage](https://xerg.ai)
- [Xerg documentation](https://xerg.ai/docs)
- [Xerg skill source](https://xerg.ai/skill.md)
- [@xerg/cli on npm](https://www.npmjs.com/package/@xerg/cli)
- [Xerg service status](https://status.xerg.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI output handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance emphasizes explicit approval before installs, local analysis, and hosted uploads; audit outputs may distinguish priced, estimated, and unpriced runtime costs.]

## Skill Version(s):

0.27.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
