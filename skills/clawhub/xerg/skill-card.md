## Description:

Xerg audits AI agent runtime spend in dollars, identifying evidence-strict waste, detector coverage, runtime attribution, and FinOps signals across OpenClaw, Hermes, QM, Claude Code, Cursor, and generic event ingest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xerg](https://clawhub.ai/user/xerg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform teams, and FinOps reviewers use Xerg to audit local or explicitly provided AI runtime evidence, explain spend and waste findings, and compare compatible fixes before optional hosted follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or execute the @xerg/cli npm package.

Mitigation: Install only if you trust Xerg and the npm package source; prefer pinned or preinstalled CLI use in higher-assurance environments.

Risk: Audits may read local AI runtime logs, transcripts, snapshots, or exports.

Mitigation: Require explicit approval before local analysis, review the selected source, and keep the audit local unless upload is separately approved.

Risk: Hosted push, MCP setup, remote SSH, QM collection, and CI API-key use introduce additional data flows.

Mitigation: Approve only the specific requested flow and store any CI API key in the CI provider's secret manager.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xerg/skills/xerg)
- [Xerg Homepage](https://xerg.ai)
- [Xerg Documentation](https://xerg.ai/docs)
- [Xerg Skill Source](https://xerg.ai/skill.md)
- [@xerg/cli npm Package](https://www.npmjs.com/package/@xerg/cli)
- [Xerg Service Status](https://status.xerg.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON-aware result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local audit summaries, coverage warnings, comparison guidance, and optional hosted setup instructions after explicit approval.]

## Skill Version(s):

0.32.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
