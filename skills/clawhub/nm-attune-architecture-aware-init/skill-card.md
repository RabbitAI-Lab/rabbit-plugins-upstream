## Description:

Selects architecture paradigm via research before scaffolding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when starting a project with an undecided architecture and need research-backed paradigm selection, scaffold guidance, and an architecture decision record.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Architecture recommendations, scaffold choices, or ADR content may not fit the project's actual constraints.

Mitigation: Review the captured project context, research synthesis, selected paradigm, and generated ADR before accepting changes.

Risk: The skill may create or modify project files during initialization.

Mitigation: Inspect generated diffs and run the project's normal tests and scans before committing scaffold or configuration changes.

Risk: Online research may surface stale or weak sources.

Mitigation: Prefer current authoritative sources and include reviewed references in the final ADR.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-architecture-aware-init)
- [Project homepage from ClawHub metadata](https://github.com/athola/claude-night-market/tree/master/plugins/attune)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with code blocks, directory layouts, and ADR content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce project scaffold files, configuration changes, research synthesis, and architecture decision records.]

## Skill Version(s):

1.9.18 (source: release evidence; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
