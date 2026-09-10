## Description:

Audit and reduce AI agent runtime spend in dollars across OpenClaw, Hermes, QM, Claude Code, Cursor, and generic event ingest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xerg](https://clawhub.ai/user/xerg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and FinOps teams use this skill to inspect local or explicitly selected agent-runtime evidence, identify evidence-strict AI spend waste, review neutral cost signals, and compare compatible remediation results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The pinned CLI can read selected AI runtime logs, transcripts, local databases, snapshots, or remote sources under the user's account.

Mitigation: Require explicit approval for local inspection, scope the target data source deliberately, and sandbox execution for highly sensitive production data.

Risk: Skill-directed execution depends on npm-delivered @xerg/cli code and the reviewed pin does not cryptographically lock transitive dependencies.

Mitigation: Use the reviewed CLI version specified by the skill, verify the CLI version before audit actions, and avoid mutable or unpinned bootstrap commands when a pinned install is available.

Risk: Hosted pairing or push actions can upload audit summaries and source metadata after user approval.

Mitigation: Keep local audits as the default, ask before any hosted write, and use an exact organization identifier when the intended hosted workspace is known.

Risk: Automation credentials such as XERG_API_KEY could expose hosted access if pasted into chat, logs, source files, or shell history.

Mitigation: Use XERG_API_KEY only for non-interactive CI or deployment automation and store it in the CI provider's secret manager.

## Reference(s):

- [Xerg Homepage](https://xerg.ai)
- [Xerg Documentation](https://xerg.ai/docs)
- [Xerg Skill](https://xerg.ai/skill.md)
- [Xerg Service Status](https://status.xerg.ai)
- [@xerg/cli npm package](https://www.npmjs.com/package/@xerg/cli)
- [OpenSSH](https://www.openssh.com/)
- [rsync](https://rsync.samba.org/)
- [Railway CLI](https://github.com/railwayapp/cli)
- [Fly.io flyctl](https://fly.io/docs/flyctl/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and summarized audit results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill asks for separate approval before npm installation, local inspection, remote access, or hosted upload. Local audit results may include priced, estimated, or unpriced runtime costs and are not provider invoices.]

## Skill Version(s):

0.32.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
