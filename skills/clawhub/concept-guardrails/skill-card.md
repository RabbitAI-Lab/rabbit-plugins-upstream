## Description:

Helps agents create and check repository-local CONCEPT, PIPELINE, SYNCS, and ARCHITECTURE documents for wyx-style module boundaries and drift.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to declare module boundaries, data-flow contracts, cross-concept coordination, drift reports, and derived architecture maps in Chinese-language wyx-style specifications. It is intended for explicit invocation during repository maintenance and architecture review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional hook runtime scans local project files and injects repository-controlled specification text into agent context.

Mitigation: Enable the hook runtime only in trusted repositories and review CONCEPT.md, PIPELINE.md, and SYNCS.md before editing with hooks active.

Risk: Generated architecture maps can become stale after specification changes.

Mitigation: Treat ARCHITECTURE.md as generated output and review its diff or rerun wyx:map after specification updates.

Risk: The hook checks are advisory and can be bypassed by shell commands or other file-writing tools.

Mitigation: Use wyx:concept drift and code review to confirm boundary compliance before relying on the resulting specifications.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agenticweb4/skills/concept-guardrails)
- [Upstream wyx project](https://github.com/jlifyio/wyx)
- [Audit workflow](references/audit.md)
- [Concept specification workflow](references/concept.md)
- [Drift detection workflow](references/drift-detection.md)
- [Hook runtime notes](references/hooks-runtime.md)
- [Architecture map workflow](references/map.md)
- [Pipeline specification workflow](references/pipeline.md)
- [Sync mapping workflow](references/sync.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown specifications, drift reports, action plans, architecture maps, and optional shell hook guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes repository-local specification files only after user review, except derived architecture maps; optional Claude Code hooks add context around edit operations.]

## Skill Version(s):

0.27.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
