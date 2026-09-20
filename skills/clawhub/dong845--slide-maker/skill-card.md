## Description:

Build, redesign, and critique clean, presentation-grade slide decks (.pptx) for audiences such as research meetings, work updates, conference talks, stakeholder readouts, thesis defenses, teaching, and webinars.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to plan, build, redesign, review, and iterate on presentation decks from source material, existing slides, templates, figures, or user-provided goals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can execute Python files placed beside a deck during normal gate checks, which is high-impact for decks from other people.

Mitigation: Use a virtual environment or container, review deck folders before running delivery or register gates, and remove or inspect nearby surface_*.py, style.py, and section_*.py files from untrusted sources.

## Reference(s):

- [Skill instructions](artifact/SKILL.md)
- [Design principles](artifact/references/design-principles.md)
- [Security and capabilities](artifact/references/security-and-capabilities.md)
- [Deck setup](artifact/references/deck-setup.md)
- [Review rubrics](artifact/references/review-rubrics.md)
- [ClawHub skill page](https://clawhub.ai/dong845/skills/slide-maker)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with generated Python and shell commands that build and check .pptx slide decks and related review artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local presentation files, extracted assets, rendered previews, gate reports, and handoff notes.]

## Skill Version(s):

5.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
