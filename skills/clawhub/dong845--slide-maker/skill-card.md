## Description:

Builds, redesigns, and critiques presentation-grade .pptx slide decks from user goals, source materials, templates, or research, with interview checkpoints and an actor-critic review loop.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external presenters, and developers use this skill to turn supplied documents, code, figures, templates, or goals into clear presentation decks, and to review or redesign existing decks. It is aimed at research, business, teaching, conference, thesis, webinar, and stakeholder presentation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run Python, install packages, call network services, and write files while building and checking decks.

Mitigation: Install in a virtualenv or container, review the skill before installing, and disable automatic setup or version checks with SLIDE_MAKER_NO_ENV_CHECK=1 and SLIDE_MAKER_NO_VERSION_CHECK=1 when those behaviors are not wanted.

Risk: Third-party style.py or section_*.py files can execute Python when loaded by the deck workflow.

Mitigation: Review third-party style and section files before running them, and only use files from trusted sources.

Risk: Image sourcing, web research, icon fetching, and version checks may involve network access.

Mitigation: Provide explicit source material and image paths when possible, avoid network-backed branches that are not needed, and prefer explicit session or asset paths over broad fallbacks.

## Reference(s):

- [Security and capabilities](references/security-and-capabilities.md)
- [Design principles](references/design-principles.md)
- [Deck setup](references/deck-setup.md)
- [Content plan spec](references/content-plan-spec.md)
- [Review rubrics](references/review-rubrics.md)
- [Image generation](references/image-generation.md)
- [File inventory](references/file-inventory.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, Python code, shell commands, configuration notes, and generated deck artifacts such as .pptx files with optional PDF/PNG renders.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce checkpoint records, source records, lint reports, critic reviews, and asset files during deck construction.]

## Skill Version(s):

5.4.0 (source: server release metadata and artifact VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
