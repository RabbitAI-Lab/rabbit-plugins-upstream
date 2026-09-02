## Description:

Distill a book, paper, or thesis into a folder of terse per-concept cheatsheets with a README index.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whit3rabbit](https://clawhub.ai/user/whit3rabbit)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, writers, and other external users use this skill to turn long-form sources into concise, per-concept Markdown notes with an index and verification pass.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes scanner, hook, rewrite, file-edit, and optional model-endpoint code beyond the reading-notes workflow.

Mitigation: Review the bundled scripts before installation and run only the commands needed for note generation and verification.

Risk: Optional model processing can send flagged passages to a configured external endpoint.

Mitigation: Use --apply-model only with an endpoint you intentionally configured and trust for the source material.

Risk: Hook behavior or write modes can affect files outside a simple read-only distillation flow.

Mitigation: Avoid enabling claude_hook.py or --write modes unless you explicitly want hook scanning or in-place edits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/whit3rabbit/skills/rabbit-reads)
- [Book type: arxiv-paper](references/book-types/arxiv-paper.md)
- [Book type: fiction](references/book-types/fiction.md)
- [Book type: non-fiction](references/book-types/non-fiction.md)
- [Book type: thesis](references/book-types/thesis.md)
- [Layout: cheatsheets](references/layouts/cheatsheets.md)
- [Layout: obsidian](references/layouts/obsidian.md)
- [Fan-out prompt](references/fanout-prompt.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown notes folder with a README or index, command snippets, and verification guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one file per concept rather than one file per chapter; generated notes are expected to paraphrase source material.]

## Skill Version(s):

0.5.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
