## Description:

Creates modern, responsive HTML presentations, converts PowerPoint files to HTML decks, and helps generate presentation-derived social cover assets using design-system specifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[helloyxs](https://clawhub.ai/user/helloyxs)

### License/Terms of Use:

MIT

## Use Case:

Developers, designers, and presentation authors use this skill to have an agent plan, design, generate, validate, or convert rich HTML slide decks and related social cover assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill writes deck and cover files into the user's workspace.

Mitigation: Review generated files and keep work in a project-scoped directory before publishing or sharing outputs.

Risk: Generated decks may reference remote fonts or scripts, which can be unsuitable for confidential or air-gapped work.

Mitigation: Disable, vendor, or replace remote assets before opening or distributing decks in restricted environments.

Risk: Presentation or cover outputs can contain incorrect, sensitive, or misleading content.

Mitigation: Review generated presentations and cover images before external publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/helloyxs/skills/generate-html-ppt)
- [README_en.md](README_en.md)
- [STYLE_GALLERY.md](designs/STYLE_GALLERY.md)
- [STYLE_PRESETS.md](designs/STYLE_PRESETS.md)
- [selection-index.json](designs/bold-template-pack/selection-index.json)
- [requirements-checklist.md](references/requirements-checklist.md)
- [image-treatments.md](references/image-treatments.md)
- [covers.md](references/covers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTML, CSS, JavaScript, Python, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces or modifies local presentation and cover files in the user's workspace.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
