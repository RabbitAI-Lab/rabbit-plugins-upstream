## Description:

Xerg audits and helps reduce AI agent runtime spend in dollars across OpenClaw, Hermes, QM, Claude Code, Cursor, and generic event ingest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xerg](https://clawhub.ai/user/xerg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineering leaders, and AI FinOps teams use Xerg to audit local agent-runtime spend, identify evidence-strict waste findings and neutral signals, and compare compatible changes. The skill can guide local-only audits and optional approved hosted follow-up without treating modeled runtime spend as provider-invoice authority.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can inspect local AI-agent runtime data and can push summarized audit results to Xerg Cloud when explicitly approved.

Mitigation: Run local audits first, review the requested scope before approving hosted push, and avoid hosted, remote, QM, Linear, or MCP actions unless they match the intended audit.

Risk: The npx @latest path fetches and executes the currently published npm package.

Mitigation: Review or pin the @xerg/cli version for repeatable automation instead of routinely executing @latest.

Risk: Remote SSH/Railway and QM collection paths can touch private runtime infrastructure when authorized.

Mitigation: Require operator approval and use bounded configured collection paths; do not provide database URLs, Fly tokens, provider credentials, or Xerg credentials in chat.

## Reference(s):

- [Xerg homepage](https://xerg.ai)
- [Xerg documentation](https://xerg.ai/docs)
- [Xerg skill instructions](https://xerg.ai/skill.md)
- [Xerg service status](https://status.xerg.ai)
- [@xerg/cli on npm](https://www.npmjs.com/package/@xerg/cli)
- [OpenSSH](https://www.openssh.com/)
- [rsync](https://rsync.samba.org/)
- [Railway CLI](https://github.com/railwayapp/cli)
- [Fly CLI documentation](https://fly.io/docs/flyctl/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local audits may produce summarized monetary findings, neutral signals, comparison output, and configuration guidance; hosted push requires explicit approval.]

## Skill Version(s):

0.32.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
