## Description:

Advanced Human Writing & AI Humanizer helps agents humanize and revise multilingual drafts, compile writing prompts, and audit fiction, long-form prose, dialogue, continuity, style, source grounding, and protected content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whh110112](https://clawhub.ai/user/whh110112)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and writing agents use this skill to convert vague writing requests into genre-aware prompts, improve AI-assisted drafts, preserve meaning during rewrites, and generate staged audits for long-form manuscripts or serious documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided drafts, sources, references, and originals can be read by the CLI and included in model prompt material.

Mitigation: Only pass files intended for the writing workflow; keep inputs in the project workspace and avoid private files unless their contents may be used in prompts.

Risk: Commands that apply fixes or write audits can create generated audit or cleanup files.

Mitigation: Use --preview before --apply and direct staged audits to an explicit output directory.

## Reference(s):

- [README](README.md)
- [Multi-Stage Audit Pipeline](docs/audit-pipeline.md)
- [Fidelity, Statistics, and Conservative Fixes](docs/editing-tools.md)
- [Chunked Long-Form Audit, Style Unification, and Character Consistency](docs/long-form-consistency.md)
- [Deterministic Writing-Pattern Linter](docs/pattern-linter.md)
- [Protected Content Verification](docs/protected-content.md)
- [Reference Style Alignment](docs/reference-style.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text, including instruction packs, lint findings, audit prompts, staged audit files, fix previews, and protected-content comparison reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI workflows can read named draft, source, reference, context, and original files, and can write generated audit or cleanup outputs.]

## Skill Version(s):

0.13.0 (source: pyproject.toml and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
