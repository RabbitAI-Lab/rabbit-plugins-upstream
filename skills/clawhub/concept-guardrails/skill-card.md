## Description:

Runs explicitly invoked concept-spec guardrails for audit, concept, drift, pipeline, sync, and architecture-map workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create and audit CONCEPT.md, PIPELINE.md, and SYNCS.md specifications, detect drift between those specifications and code, and derive ARCHITECTURE.md maps for modular systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional hook runtime can run shell commands automatically on session start and before or after file edits.

Mitigation: Enable the runtime only in trusted repositories, review any .claude/settings.json hook merge, and remove it if automatic command execution is not desired.

Risk: Optional hooks can feed local repository text into the agent as boundary context.

Mitigation: Review repository contents before enabling hooks and use the base skill without the runtime when automatic context injection is not desired.

Risk: Hooks are advisory and do not fully validate Jackson-format concept or sync boundaries.

Mitigation: Use audit and drift modes for checks, and review generated specification changes before accepting writes.

## Reference(s):

- [Concept Guardrails homepage](https://github.com/ontology-of-everything/SemanticSkills/tree/main/skills/concept-guardrails)
- [ClawHub skill page](https://clawhub.ai/agenticweb4/skills/concept-guardrails)
- [Audit mode](references/audit.md)
- [Concept mode](references/concept.md)
- [Drift detection mode](references/drift-detection.md)
- [Hooks runtime](references/hooks-runtime.md)
- [Architecture map mode](references/map.md)
- [Pipeline mode](references/pipeline.md)
- [Sync mode](references/sync.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional shell commands and specification file content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update CONCEPT.md, PIPELINE.md, SYNCS.md, and ARCHITECTURE.md when explicitly authorized; audit and drift modes are read-only.]

## Skill Version(s):

0.30.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
