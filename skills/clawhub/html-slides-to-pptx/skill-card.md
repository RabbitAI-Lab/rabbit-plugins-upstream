## Description:

Generates HTML slide decks through a guided brief, validates them against a strict HTML slide specification, and converts them to PowerPoint PPTX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cqcmj74](https://clawhub.ai/user/cqcmj74)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and presentation authors use this skill to turn requested slide content into a structured HTML slide project and a PPTX deck. It is intended for workflows that need editable PowerPoint output after HTML validation and preview checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The converter may follow local file paths or remote URL references from slide HTML.

Mitigation: Use trusted slide sources and review any file:// or http(s) references before running preview or conversion.

Risk: Installation downloads Node dependencies and Chromium.

Mitigation: Install only in environments where those downloads are acceptable and dependency review practices are in place.

Risk: The skill creates files in the active project.

Mitigation: Run it in a dedicated workspace and review generated files before using or sharing the resulting deck.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cqcmj74/skills/html-slides-to-pptx)
- [HTML slide specification](artifact/reference/html-spec.md)
- [Design principles](artifact/reference/design-principles.md)
- [Behavior baseline](artifact/reference/behavior-baseline.md)
- [Brand style source noted by artifact](https://github.com/VoltAgent/awesome-design-md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, shell commands, guidance]

**Output Format:** [Markdown guidance with HTML, CSS, JSON, JavaScript, and shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a slide project directory and PPTX output when the bundled Node tools run.]

## Skill Version(s):

1.1.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
