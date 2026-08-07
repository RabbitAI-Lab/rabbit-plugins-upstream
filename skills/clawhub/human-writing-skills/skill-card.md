## Description:

Write, rewrite, or audit natural, genre-aware prose with long-form continuity, world-rule compatibility, earned process and payoff, attention-budget and chapter-pattern review, character-fit dialogue and subtext, explicit reference-style matching, physical and relationship consistency, deterministic AI-pattern linting, and source-grounded serious writing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whh110112](https://clawhub.ai/user/whh110112)

### License/Terms of Use:

MIT

## Use Case:

Developers, writing agents, and authors use this skill pack to compile genre-specific writing instructions, revise drafts, run focused manuscript audits, preserve long-form continuity, and protect source-grounded or exact content during editing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tool reads drafts, context, references, and source files that the user explicitly passes to it.

Mitigation: Pass only the files needed for the writing task and avoid including secrets or unrelated private material.

Risk: Generated prompt packs and local audit files may carry incorrect or overbroad editing guidance into later model workflows.

Mitigation: Review generated instructions and audit output before using them downstream.

## Reference(s):

- [Human Writing Skills README](artifact/README.md)
- [Multi-Stage Audit Pipeline](artifact/docs/audit-pipeline.md)
- [Deterministic Writing-Pattern Linter](artifact/docs/pattern-linter.md)
- [Protected Content Verification](artifact/docs/protected-content.md)
- [Reference Style Alignment](artifact/docs/reference-style.md)
- [Physical Continuity](artifact/docs/physical-continuity.md)
- [Relationship Stance Continuity](artifact/docs/relationship-stance-continuity.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown prompt packs, audit reports, lint findings, local files, and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can optionally write local audit outputs; source-grounding and reference-style modules activate only when explicit files or task cues are supplied.]

## Skill Version(s):

0.8.1 (source: server release metadata and pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
