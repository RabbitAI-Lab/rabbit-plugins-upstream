## Description:

Audit and reduce AI agent runtime spend in dollars across OpenClaw, Hermes, QM, Claude Code, Cursor, and generic event ingest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xerg](https://clawhub.ai/user/xerg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and FinOps teams use this skill to run local-first Xerg audits, interpret AI runtime spend findings, and compare compatible remediation results without treating modeled runtime costs as provider invoices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inspect sensitive local AI-agent usage records.

Mitigation: Require explicit approval before local data inspection and review the audit scope before running Xerg commands.

Risk: Hosted features can push summarized audit data to Xerg.

Mitigation: Keep local audit and hosted upload as separate decisions and ask for explicit approval before any push, connect, or hosted command.

Risk: First-run commands may fetch and execute the npm package.

Mitigation: Ask for separate approval before npm install or transient npx fetch, and use the published @xerg/cli package path described by the artifact.

## Reference(s):

- [Xerg homepage](https://xerg.ai)
- [Xerg documentation](https://xerg.ai/docs)
- [Xerg skill source](https://xerg.ai/skill.md)
- [Xerg service status](https://status.xerg.ai)
- [@xerg/cli npm package](https://www.npmjs.com/package/@xerg/cli)
- [OpenSSH](https://www.openssh.com/)
- [rsync](https://rsync.samba.org/)
- [Railway CLI](https://github.com/railwayapp/cli)
- [Fly CLI documentation](https://fly.io/docs/flyctl/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON-oriented audit instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local audit guidance is permission-gated; hosted upload guidance requires explicit user approval.]

## Skill Version(s):

0.24.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
