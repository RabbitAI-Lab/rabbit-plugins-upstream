## Description:

Audit and reduce AI agent runtime spend in dollars. Use for AI costs, agent spend, token waste, runtime attribution, detector coverage, and FinOps. Works with OpenClaw, Hermes, QM, Claude Code, Cursor, and generic event ingest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xerg](https://clawhub.ai/user/xerg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform teams, and FinOps users use this skill to audit AI agent runtime spend across supported local runtimes, exports, traces, and remote sources, then explain evidence-backed waste findings, neutral signals, detector coverage, and compatible before-and-after deltas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Xerg CLI inspects selected AI runtime logs, state databases, exports, remote sources, or ingest payloads during local audits.

Mitigation: Install and run it only after explicit approval for npm/package use and separate approval for the specific local or remote data source to inspect.

Risk: Hosted pairing or upload can send audit summaries and source metadata to Xerg Cloud.

Mitigation: Keep audits local by default and require explicit user approval before activation, push, hosted MCP setup, or any other hosted write.

Risk: Runtime costs may be observed, locally estimated, or unpriced, so reported spend is not an authoritative provider invoice.

Mitigation: Present pricing coverage and invoice boundaries with spend conclusions, and avoid treating modeled runtime spend as billing reconciliation.

## Reference(s):

- [Xerg homepage](https://xerg.ai)
- [Xerg documentation](https://xerg.ai/docs)
- [Xerg skill source](https://xerg.ai/skill.md)
- [Xerg service status](https://status.xerg.ai)
- [@xerg/cli npm package](https://www.npmjs.com/package/@xerg/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and summarized JSON-oriented audit results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local spend findings, neutral signals, detector coverage, pricing-coverage caveats, compare deltas, and optional hosted follow-up instructions when explicitly approved.]

## Skill Version(s):

0.26.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
