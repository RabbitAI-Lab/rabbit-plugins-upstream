## Description:

Audit and reduce AI agent runtime spend in dollars. Use for AI costs, agent spend, token waste, runtime attribution, detector coverage, and FinOps. Works with OpenClaw, Hermes, QM, Claude Code, Cursor, and generic event ingest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xerg](https://clawhub.ai/user/xerg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineering leaders, and FinOps teams use this skill to audit local and pushed AI-agent runtime spend, identify evidence-backed waste, inspect detector coverage, and compare compatible fixes across supported agent runtimes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local audits can inspect sensitive agent runtime records and write local comparison snapshots.

Mitigation: Approve local inspection only for intended sources, keep source mounts scoped, and review audit outputs before sharing.

Risk: Package installation, remote collection, hosted pairing, and upload are separate actions with different data exposure.

Mitigation: Require explicit approval for each stage and use the pinned reviewed CLI version shown by the skill.

Risk: Runtime cost estimates may be observed, locally estimated, or unpriced rather than invoice-authoritative.

Mitigation: Present audit results as runtime-spend analysis, disclose pricing coverage, and avoid treating modeled spend as provider billing reconciliation.

## Reference(s):

- [Xerg homepage](https://xerg.ai)
- [ClawHub skill page](https://clawhub.ai/xerg/skills/xerg)
- [Xerg documentation](https://xerg.ai/docs)
- [Canonical Xerg skill](https://xerg.ai/skill.md)
- [@xerg/cli package](https://www.npmjs.com/package/@xerg/cli)
- [Service status](https://status.xerg.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented audit outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local audit, comparison, setup, and hosted-sync guidance; users approve installation, local inspection, remote access, and upload stages separately.]

## Skill Version(s):

0.35.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
