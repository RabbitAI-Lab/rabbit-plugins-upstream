## Description:

Xerg helps agents audit and reduce AI runtime spend by analyzing costs, token waste, detector coverage, runtime attribution, and FinOps signals across OpenClaw, Hermes, QM, Claude Code, Cursor, and generic event ingest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xerg](https://clawhub.ai/user/xerg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineering teams, and AI FinOps users use this skill to run Xerg CLI audits, interpret AI runtime spend, identify evidence-strict waste, and compare compatible fixes. It is intended for approved local runtime evidence and optional explicit hosted follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may require npm package execution and access to local runtime logs, transcripts, databases, snapshots, or exports.

Mitigation: Install and run it only after explicit approval for npm execution and for the specific local data source being audited.

Risk: Hosted pairing or push sends summarized audit data to Xerg Cloud.

Mitigation: Keep audits local by default, ask before uploads, and review the approved source before running hosted commands.

Risk: Runtime costs may be observed, locally estimated, or unpriced rather than authoritative provider invoices.

Mitigation: Present audit totals as runtime audit estimates and disclose pricing coverage before drawing savings conclusions.

## Reference(s):

- [Xerg homepage](https://xerg.ai)
- [Xerg documentation](https://xerg.ai/docs)
- [Canonical Xerg skill](https://xerg.ai/skill.md)
- [@xerg/cli npm package](https://www.npmjs.com/package/@xerg/cli)
- [Xerg service status](https://status.xerg.ai)
- [OpenSSH](https://www.openssh.com/)
- [rsync](https://rsync.samba.org/)
- [Railway CLI](https://github.com/railwayapp/cli)
- [flyctl documentation](https://fly.io/docs/flyctl/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented audit summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require explicit approval before npm execution, local data inspection, persistent installation, or hosted upload.]

## Skill Version(s):

0.30.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
