## Description:

Persistent Skill Memory provides an offline stdlib-only CLI for indexing installed skills and idempotently injecting a deterministic skill index into an agent system prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to keep an installed-skill index synchronized with an agent system prompt, so models can see available skills without loading each skill file. It supports indexing, prompt-block generation, idempotent injection, drift verification, statistics, and hook generation for local skill directories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill modifies an agent prompt to persist a skill index, so incorrect or unsafe prompt content can remain active across future agent sessions.

Mitigation: Review the exact prompt file and generated index before injection, keep a backup, and use only skill roots you control.

Risk: The security summary reports insufficient validation around persistent prompt content and generated hook behavior.

Mitigation: Prefer releases that validate skill names, reject marker, newline, and control characters, and add a confirmation or backup flow before prompt injection.

Risk: Generated hooks run an installer command before reindexing and injecting prompt content.

Mitigation: Use hooks only with trusted installer commands, fully controlled paths, and a reviewed generated script.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/persistent-skill-memory)
- [README](README.md)
- [CHANGELOG](CHANGELOG.md)
- [Frontmatter parsing](references/frontmatter_parsing.md)
- [Categorization](references/categorization.md)
- [Injection semantics](references/injection_semantics.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON status lines, Markdown index files, plaintext prompt blocks, and bash scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline stdlib-only CLI; writes occur only for explicit index --write, inject --prompt-file, or hook --out operations.]

## Skill Version(s):

2.0.0 (source: frontmatter and changelog, released 2026-09-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
