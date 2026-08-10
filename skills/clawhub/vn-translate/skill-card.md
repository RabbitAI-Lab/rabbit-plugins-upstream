## Description:

Translate fiction from a source language into Vietnamese using a streaming pipeline that reads raw Markdown in chunks, writes translated parts, tracks progress, maintains naming and address glossaries, and can merge or export the result as EPUB.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kaibazax-dev](https://clawhub.ai/user/kaibazax-dev)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to translate long-form fiction into Vietnamese while preserving chapter structure, paragraph boundaries, character names, and forms of address across a resumable workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow reads local source text and writes translated Markdown and state files in the active project.

Mitigation: Install and run it only in projects where that local file access and output generation are intended.

Risk: Cleanup commands can remove matching zero-byte Markdown outputs under the translation output directory.

Mitigation: List matching files before deletion and confirm they are broken generated outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kaibazax-dev/skills/vn-translate)
- [Worked translation-session example](references/session-worked-example.md)
- [Vietnamese idiom and terminology reference](references/thanh-ngu-va-tu-ngu.md)
- [Token-usage diagnostics](references/token-usage-diagnostics.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown files, JSON progress state, shell commands, and optional EPUB output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces resumable translated parts, glossary updates, merged Markdown, and optional EPUB packaging.]

## Skill Version(s):

1.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
