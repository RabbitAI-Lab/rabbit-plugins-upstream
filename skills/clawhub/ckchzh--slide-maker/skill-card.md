## Description:

Presentation and slide deck generator. Create outlines, full slide decks, speaker notes, pitch decks, training slides, report presentations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ckchzh](https://clawhub.ai/user/ckchzh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external content creators use this skill to generate presentation outlines, Markdown slide decks, speaker notes, pitch decks, training slides, report presentations, and design guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes local history logging for some content commands, which can store raw inputs under ~/.local/share/slide-maker.

Mitigation: Avoid confidential inputs unless local logging is acceptable, and review or clear the local data directory before sharing the environment.

Risk: Export, count, and timing utilities read user-specified files.

Mitigation: Run file-reading commands only against intended slide Markdown files and review outputs before relying on them.

Risk: Generated decks can include hard-coded footer text, placeholder business metrics, and placeholder contact details.

Mitigation: Review and edit generated slides before publishing or presenting them.

## Reference(s):

- [Slide Maker on ClawHub](https://clawhub.ai/ckchzh/skills/slide-maker)
- [BytesAgain homepage](https://bytesagain.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown slide content with slide separators, outlines, speaker notes, templates, timing/count summaries, and concise textual guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some commands can write local history or exported files under ~/.local/share/slide-maker; generated decks may include footer text and placeholders that should be reviewed before publishing.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
