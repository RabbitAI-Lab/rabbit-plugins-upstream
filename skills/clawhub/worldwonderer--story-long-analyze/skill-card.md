## Description:

Analyzes long-form web novels and manuscripts through a staged pipeline covering opening chapters, chapter summaries, plot structure, characters, setting, pacing, emotional hooks, reusable writing techniques, and style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and agents use this skill to analyze legally held long-form web-novel manuscripts and produce structured notes for understanding pacing, emotional mechanics, characters, settings, and style. It is intended for transformative literary analysis and writing guidance rather than copying source material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a full local copy of the source manuscript and derived analysis files.

Mitigation: Use only manuscripts the user is allowed to analyze, and review or delete files under `拆文库/{书名}/` when the source text is private or copyrighted.

Risk: Analysis can shape later writing decisions and may contain interpretation errors or overgeneralized lessons from a single work.

Mitigation: Review generated reports against the source text before using them as writing guidance, especially for character facts, setting details, pacing conclusions, and reusable technique recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-long-analyze)
- [OpenClaw source metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Output templates](artifact/references/output-templates.md)
- [Material decomposition methodology](artifact/references/material-decomposition.md)
- [Deconstruction notes](artifact/references/deconstruction-notes.md)
- [Pipeline operations](artifact/references/pipeline-ops.md)
- [Style profile protocol](artifact/references/style-profile-protocol.md)
- [Style profile generator](artifact/references/style-profile-generator.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown files, structured text reports, and concise text prompts with occasional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local analysis artifacts under `拆文库/{书名}/`, including source-text backup, progress tracking, chapter summaries, plot notes, character notes, setting notes, final reports, and style profiles.]

## Skill Version(s):

1.1.19 (source: ClawHub release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
