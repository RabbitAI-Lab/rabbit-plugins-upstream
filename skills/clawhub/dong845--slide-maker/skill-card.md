## Description:

Builds, redesigns, and critiques presentation slide decks tailored to the audience and supported by source material.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

Presenters, researchers, educators, and teams use the skill to plan, produce, revise, and review audience-specific PowerPoint decks from supplied materials or researched sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reviewing or rendering a third-party deck folder may execute Python files stored alongside the deck.

Mitigation: Inspect style.py and surface_*.py before running review, render, or delivery checks, or move the PPTX into a clean directory first.

Risk: Local deck-building setup and version checks can modify the working environment.

Mitigation: Run in a virtual environment or container; consider disabling automatic environment and version checks when appropriate.

## Reference(s):

- [Slide Maker release](https://clawhub.ai/dong845/skills/slide-maker)
- [Design principles](references/design-principles.md)
- [Deck setup](references/deck-setup.md)
- [Citations and bibliography](references/citations-and-bibliography.md)
- [Review rubrics](references/review-rubrics.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Files]

**Output Format:** [Markdown plans and review notes, Python build code, and PowerPoint (.pptx) decks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include rendered slide previews and quality-check reports.]

## Skill Version(s):

5.6.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
