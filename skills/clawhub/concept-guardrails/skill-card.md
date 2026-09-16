## Description:

Runs concept-spec guardrails in audit, concept, drift, pipeline, sync, or map mode when explicitly invoked to create, backfill, compare, or map colocated concept specifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to audit, create, backfill, compare, synchronize, and map concept specifications against implementation evidence. It helps keep CONCEPT, SYNCS, PIPELINE, and derived architecture maps aligned without treating specifications as proof of implementation correctness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic Claude Code hooks can add behavior beyond explicit $concept-guardrails commands.

Mitigation: Review runtime/hooks/hooks.json and the hook scripts before enabling them, and enable hooks only for projects where that behavior is wanted.

Risk: Broad local scanning and a project-boundary weakness could read nearby external specification files into session context.

Mitigation: Keep hook installation project-scoped, inspect edited paths and project boundaries, and disable the optional hook runtime where nearby specifications should not be surfaced.

Risk: Hook output surfaces specification context but does not validate semantic correctness or freshness.

Mitigation: Use audit and drift modes for explicit review, keep generated maps rebuilt from current content, and treat reports as guidance that needs human review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/agenticweb4/skills/concept-guardrails)
- [OpenClaw Homepage](https://github.com/ontology-of-everything/concept-skills/tree/main/skills/en/concept-guardrails)
- [Specification Coverage Audit](references/audit.md)
- [Concept Specification](references/concept.md)
- [Drift Detection](references/drift-detection.md)
- [Optional Hooks Runtime](references/hooks-runtime.md)
- [Architecture Map](references/map.md)
- [Data Quality Specification](references/pipeline.md)
- [Concept and Synchronization Specification Contract](references/spec-format.md)
- [Synchronization Specification](references/sync.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, specification drafts or diffs, command plans, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Explicit invocation only; read-only modes report scope and findings, while write-oriented modes present drafts or diffs before unapproved writes.]

## Skill Version(s):

0.30.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
