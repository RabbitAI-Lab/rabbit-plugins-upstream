## Description:

Audit and reduce AI agent runtime spend in dollars. Use for AI costs, agent spend, token waste, runtime attribution, detector coverage, and FinOps. Works with OpenClaw, Hermes, QM, Claude Code, Cursor, and generic event ingest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xerg](https://clawhub.ai/user/xerg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform teams, and FinOps reviewers use Xerg to audit local agent runtime data, identify evidence-strict waste findings, inspect neutral spend signals, and compare compatible remediation results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external npm CLI can read local agent usage data such as logs, transcripts, databases, CSV exports, or snapshots during an approved audit.

Mitigation: Require explicit approval before package fetches and local data inspection, and keep audits local unless the user separately approves hosted pairing or push.

Risk: Hosted pairing or push can transmit audit summaries and related metadata to Xerg Cloud.

Mitigation: Run hosted commands only after explicit approval, use organization scoping when provided, and never ask users to paste API keys, DSNs, identity keys, or provider credentials into chat.

Risk: Runtime spend is observed, locally estimated, or unpriced and is not authoritative billing data.

Mitigation: Describe results as runtime audit findings rather than provider invoices, and disclose pricing coverage or unavailable monetary impact before drawing spend conclusions.

## Reference(s):

- [Xerg documentation](https://xerg.ai/docs)
- [Xerg skill](https://xerg.ai/skill.md)
- [Xerg homepage](https://xerg.ai)
- [@xerg/cli npm package](https://www.npmjs.com/package/@xerg/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text]

**Output Format:** [Markdown with inline shell commands and JSON-oriented CLI result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill asks for approval before package fetches, local data inspection, persistent installation, pairing, or hosted upload.]

## Skill Version(s):

0.25.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
