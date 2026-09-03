## Description:

Compare overlapping or conflicting sources, datasets, policies, documents, definitions, or records and resolve what can be resolved while surfacing irreducible disagreement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and other agents use this skill to reconcile conflicting policies, records, datasets, definitions, or documents into a defensible view. It helps classify agreement, conflict, missing data, semantic mismatch, and stale sources before resolving what evidence and authority can resolve.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A source may be treated as authoritative because it is newer, familiar, or more complete.

Mitigation: Use explicit authority, recency, and governing-rule checks, and preserve conflicts when no defensible rule resolves them.

Risk: Similar labels across sources can hide different scopes or definitions.

Mitigation: Normalize comparable concepts while preserving meaningful differences in scope, units, time, and terminology.

Risk: Unclear source authority can produce an unsupported resolution.

Mitigation: Identify the smallest additional evidence or human decision needed, or consult another skill when source authority is unclear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/raguets/skills/reconcile)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown comparison table with summary bullets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The expected output includes reconciled facts safe to use, unresolved conflicts that can change the outcome, and sources that should no longer drive the decision.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter metadata.version is 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
