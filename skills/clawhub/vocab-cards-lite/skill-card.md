## Description:

Professional English vocabulary flashcard generator that creates black-and-white print-optimized main cards, side cards, and Baidu Baike QR-code PNGs from JSON word data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[51comic](https://clawhub.ai/user/51comic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, educators, and content creators use this skill to batch-generate printable English vocabulary flashcards from structured JSON word data. It is suited to bilingual vocabulary materials that need IPA pronunciation, definitions, examples, cultural notes, and optional Baidu Baike QR links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dependency setup installs unpinned Python packages and may affect the active Python environment.

Mitigation: Install and run the skill in a virtual environment or other isolated Python environment, and review dependencies before setup.

Risk: Generated card rendering depends on expected system fonts, and advertised bundled fonts may be missing.

Mitigation: Confirm required NotoSansCJK and DejaVu fonts are available, then run the setup validation before generating production batches.

## Reference(s):


## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [PNG image files generated from JSON input, with shell command and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs fixed-size 1000 x 1700 main, QR-enhanced, and optional side-card images; generated file names are derived from each English word.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter and _meta.json list 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
