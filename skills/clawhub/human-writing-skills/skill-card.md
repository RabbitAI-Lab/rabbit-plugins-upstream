## Description:

Advanced Human Writing & AI Humanizer helps agents humanize and edit multilingual prose, build genre-aware prompt packs, and audit long-form writing for continuity, style, source fidelity, protected content, and revision quality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whh110112](https://clawhub.ai/user/whh110112)

### License/Terms of Use:

MIT

## Use Case:

Developers, writers, editors, and writing agents use this skill to rewrite drafts naturally, compile task-specific writing instructions, and run focused audits for fiction, serious documents, style consistency, source grounding, protected content, and long-form continuity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can read drafts, context, originals, references, and source files selected by the user.

Mitigation: Do not pass secrets or unrelated private documents as style references or sources; provide only the files needed for the writing task.

Risk: Fix or pipeline workflows can write staged audit files or apply edits to user text when requested.

Mitigation: Use preview and output-directory modes before applying changes to an original file, and review generated edits before reuse.

Risk: Humanization and AI-trace guidance can be misread as detector evasion or authorship proof.

Mitigation: Use the skill for editing quality, continuity, and craft review; do not claim that style diagnostics prove authorship or guarantee detector outcomes.

Risk: Reference-style and source-grounding workflows can mix style evidence, factual evidence, and rewrite originals if inputs are chosen carelessly.

Mitigation: Keep original text, style references, factual sources, and project context separate, and treat supplied facts and source files as authoritative only for the relevant workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/whh110112/skills/human-writing-skills)
- [README](artifact/README.md)
- [Skill instructions](artifact/SKILL.md)
- [Long-form consistency guide](artifact/docs/long-form-consistency.md)
- [Audit pipeline guide](artifact/docs/audit-pipeline.md)
- [Protected content verification](artifact/docs/protected-content.md)
- [Editing tools guide](artifact/docs/editing-tools.md)
- [Reference style guide](artifact/docs/reference-style.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown prompt packs and audit reports, JSON diagnostics, Python CLI output, and command-line guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read user-supplied draft, context, original, reference, or source files and may write staged audit files or previewed fixes when requested.]

## Skill Version(s):

0.12.1 (source: server release metadata and pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
