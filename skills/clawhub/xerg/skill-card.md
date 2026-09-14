## Description:

Audit and reduce AI agent runtime spend in dollars across OpenClaw, Hermes, QM, Claude Code, Cursor, and generic event ingest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xerg](https://clawhub.ai/user/xerg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineering managers, and FinOps teams use this skill to run local-first AI runtime audits, separate evidence-strict monetary waste findings from neutral signals, and compare compatible changes after remediation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can execute a pinned npm CLI and inspect approved local AI runtime data.

Mitigation: Install or fetch the pinned package only after approval, keep audits local by default, and use a sandbox or prefetched verified package in sensitive environments.

Risk: Runtime audit costs may be observed, locally estimated, or unpriced and are not authoritative provider invoices.

Mitigation: Present pricing coverage and limitations before spend conclusions, and avoid treating modeled runtime spend as invoice reconciliation.

Risk: Hosted connection and upload could send approved audit summaries outside the local environment.

Mitigation: Review dry-run payloads before pushing, keep workspace connection separate from upload, and require explicit approval for each hosted stage.

## Reference(s):

- [Xerg documentation](https://xerg.ai/docs)
- [Xerg homepage](https://xerg.ai)
- [Xerg skill source](https://xerg.ai/skill.md)
- [Xerg service status](https://status.xerg.ai)
- [@xerg/cli npm package](https://www.npmjs.com/package/@xerg/cli)
- [ClawHub skill page](https://clawhub.ai/xerg/skills/xerg)

## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown, JSON, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON audit output from the Xerg CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-first audit workflow; hosted connection, payload preview, and upload require separate approval.]

## Skill Version(s):

0.35.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
