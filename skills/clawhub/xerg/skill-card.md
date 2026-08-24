## Description:

Xerg audits and helps reduce AI agent runtime spend in dollars across OpenClaw, Hermes, QM, Claude Code, Cursor, and generic event ingest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xerg](https://clawhub.ai/user/xerg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and AI operations teams use this skill to run local-first audits of agent runtime spend, identify evidence-backed waste, inspect neutral cost signals, and compare compatible fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local audits may inspect sensitive agent runtime records such as transcripts, logs, state databases, CSV exports, and snapshots.

Mitigation: Run the skill only when that audit is intended, and approve local runtime data access explicitly before analysis.

Risk: First-run commands may fetch and execute the @xerg/cli npm package.

Mitigation: Approve npm or package execution only when the publisher and package source are trusted.

Risk: Hosted push can send disclosed audit summary data to Xerg Cloud.

Mitigation: Keep audits local unless hosted sync is desired, and approve any push or hosted pairing separately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xerg/skills/xerg)
- [Xerg homepage](https://xerg.ai)
- [Xerg documentation](https://xerg.ai/docs)
- [Canonical skill file](https://xerg.ai/skill.md)
- [@xerg/cli npm package](https://www.npmjs.com/package/@xerg/cli)
- [Xerg service status](https://status.xerg.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-oriented audit guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs emphasize local audit setup, result interpretation, explicit approval before uploads, and conservative treatment of pricing or detector coverage gaps.]

## Skill Version(s):

0.27.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
