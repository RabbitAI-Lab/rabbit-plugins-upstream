## Description:

Helps developers and creators with a coding agent discover, validate, plan, and track worthwhile open-source project ideas without taking over feature implementation or business-code development.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wanghaonan3333-web](https://clawhub.ai/user/wanghaonan3333-web)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill when they have a coding agent but need structured help choosing a project direction, validating demand, producing an implementation plan, or tracking progress against an approved plan. It is intended for guided project decision-making and read-only progress review, not for writing production code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Adapter installation documentation may encourage unsafe or inconsistent download-and-execute behavior.

Mitigation: Inspect the source locally before installation, review the installer path, run installation in dry-run mode first, and avoid relying on download-and-execute statements in adapter documentation.

Risk: The skill can read and write local profile or project state when used as designed.

Mitigation: Require explicit user authorization for non-default reads, show diffs or summaries before state changes, and write state only after user confirmation.

Risk: Progress tracking could be mistaken for permission to modify a development workspace.

Mitigation: Keep Track phase activity read-only, limit evidence collection to authorized sources, and hand off implementation work to a separate development workflow.

## Reference(s):

- [Carpe Diem ClawHub Skill Page](https://clawhub.ai/wanghaonan3333-web/skills/carpe-diem)
- [ClawHub Publisher Profile](https://clawhub.ai/user/wanghaonan3333-web)
- [Homepage](https://github.com/wanghaonan3333-web/carpe-diem)
- [Methodology](references/methodology.md)
- [Safety Boundaries](references/safety-boundaries.md)
- [Stage Transition Graph](references/stage-transition-graph.md)
- [State Schema](references/state-schema.md)
- [Wisdom Library](references/wisdom/README.md)
- [Wisdom Distillation Summary](docs/wisdom-distillation-summary.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Conversational guidance and Markdown planning or tracking artifacts, with occasional shell commands for deterministic local helper scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose project plans, handoff summaries, progress reports, state diffs, and read-only evidence summaries; local state writes require user confirmation.]

## Skill Version(s):

0.3.0 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
