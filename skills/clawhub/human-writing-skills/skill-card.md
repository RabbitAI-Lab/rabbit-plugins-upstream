## Description:

Advanced multilingual AI humanizer for de-AI writing, natural rewriting, fiction editing, and long-form continuity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whh110112](https://clawhub.ai/user/whh110112)

### License/Terms of Use:

MIT

## Use Case:

External users, writers, editors, and developers use this skill to produce or revise natural multilingual prose, compile writing-agent instruction packs, and audit drafts for continuity, fidelity, protected content, and recurring writing patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads user-named draft, reference, source, original, and context files, so unintended files could be exposed to the writing agent if selected by mistake.

Mitigation: Use it only with files the agent is intended to read, and keep factual sources, originals, style references, and continuity context separate.

Risk: Previewed fixes or generated audit outputs can replace or create local files when explicit write options are used.

Mitigation: Preview fixes before using apply behavior, and avoid output paths or output directories that contain files you cannot replace.

Risk: Rewriting and humanization can unintentionally alter numbers, citations, URLs, code fragments, quotations, required terms, or claim polarity.

Mitigation: Use the documented protected-content and source/original verification workflows for important revisions.

Risk: Pattern and naturalness diagnostics can be misunderstood as authorship or detector-evasion evidence.

Mitigation: Treat findings as editing evidence only; the artifact explicitly says not to claim detector evasion or infer authorship from stylistic patterns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/whh110112/skills/human-writing-skills)
- [README](README.md)
- [Deterministic Writing-Pattern Linter](docs/pattern-linter.md)
- [Multi-Stage Audit Pipeline](docs/audit-pipeline.md)
- [Protected Content Verification](docs/protected-content.md)
- [Reference Style Alignment](docs/reference-style.md)
- [Fidelity, Statistics, and Conservative Fixes](docs/editing-tools.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Plain text and Markdown instruction packs, audit prompts, JSON diagnostics, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read user-supplied drafts, originals, references, sources, and context files; file writes occur through explicit CLI output options.]

## Skill Version(s):

0.10.6 (source: release evidence and pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
