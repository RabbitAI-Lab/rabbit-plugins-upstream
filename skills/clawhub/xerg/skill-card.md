## Description:

Audit and reduce AI agent runtime spend in dollars. Use for AI costs, agent spend, token waste, runtime attribution, detector coverage, and FinOps. Works with OpenClaw, Hermes, QM, Claude Code, Cursor, and generic event ingest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xerg](https://clawhub.ai/user/xerg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineering leads, and FinOps teams use this skill to run local-first AI runtime spend audits, identify evidence-strict waste findings, review neutral spend signals, and compare compatible fixes across supported agent runtimes and exported event payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run a proprietary npm CLI against AI-runtime logs, transcripts, snapshots, exports, or event payloads.

Mitigation: Use only approved source paths in a restricted environment and obtain explicit permission before package download, installation, local inspection, remote access, or upload.

Risk: Runtime spend is observed, locally estimated, or unpriced and is not an authoritative provider invoice.

Mitigation: Present audit totals as runtime audit estimates, disclose pricing coverage limits, and avoid treating unpriced usage as free.

Risk: Hosted pairing and push can transmit audit summaries and source metadata outside the local environment.

Mitigation: Review a dry-run payload before upload, use browser pairing instead of chat-provided credentials, and keep API keys or remote credentials out of conversation and source files.

## Reference(s):

- [Xerg homepage](https://xerg.ai)
- [Xerg documentation](https://xerg.ai/docs)
- [Xerg skill](https://xerg.ai/skill.md)
- [@xerg/cli on npm](https://www.npmjs.com/package/@xerg/cli)
- [Xerg service status](https://status.xerg.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and summarized JSON audit results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a reviewed @xerg/cli 0.34.0 command path; hosted pairing, preview, and upload are optional staged actions.]

## Skill Version(s):

0.34.1 (source: server evidence release.version; reviewed CLI: 0.34.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
