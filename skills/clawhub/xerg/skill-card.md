## Description:

Audit and reduce AI agent runtime spend in dollars across OpenClaw, Hermes, QM, Claude Code, Cursor, and generic event ingest sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xerg](https://clawhub.ai/user/xerg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform operators, and AI FinOps teams use this skill to run local Xerg audits, explain runtime spend findings, and compare compatible remediation results. It helps separate evidence-strict monetary waste from neutral signals while keeping hosted upload optional and approval-based.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The closed-source npm CLI may read local AI runtime logs, transcripts, state databases, approved snapshots, or audit payloads.

Mitigation: Start with the local audit path, request explicit approval before npm execution or local data inspection, and inspect only the sources selected by the user or by doctor output.

Risk: Audit data may be uploaded to Xerg Cloud if hosted sync or push commands are run.

Mitigation: Keep audits local by default and require separate explicit approval before activate, push, hosted MCP setup, or any hosted write.

Risk: Credentials, API keys, DSNs, workspace keys, provider tokens, or deployment secrets could be exposed if pasted into chat or commands.

Mitigation: Do not request secrets in chat; use browser pairing, local credential storage, or the target platform's secret manager for non-interactive automation.

## Reference(s):

- [Xerg documentation](https://xerg.ai/docs)
- [Xerg skill source](https://xerg.ai/skill.md)
- [Xerg homepage](https://xerg.ai)
- [Xerg service status](https://status.xerg.ai)
- [@xerg/cli npm package](https://www.npmjs.com/package/@xerg/cli)
- [ClawHub xerg skill page](https://clawhub.ai/xerg/skills/xerg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command blocks and JSON-oriented CLI output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local audit summaries may include pricing coverage, known spend, waste spend, detector coverage, findings, neutral signals, and per-agent spend when present.]

## Skill Version(s):

0.21.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
