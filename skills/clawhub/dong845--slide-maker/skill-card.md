## Description:

Builds, redesigns, and critiques presentation-grade PowerPoint decks from user-provided material, templates, or researched sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to plan, build, redesign, and review clean slide decks for meetings, talks, teaching, defenses, and stakeholder readouts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Normal use may install Python dependencies into the active interpreter.

Mitigation: Run the skill in a virtualenv or container, or set SLIDE_MAKER_NO_ENV_CHECK=1 to avoid automatic environment changes.

Risk: Deck building and rendering may execute local or generated Python and external rendering applications.

Mitigation: Review generated deck scripts and any third-party style.py or surface_*.py files before execution, and run rendering in a disposable workspace for untrusted material.

Risk: Some workflows may fetch web assets or check for newer versions.

Mitigation: Provide local source material and assets when possible, and set SLIDE_MAKER_NO_VERSION_CHECK=1 to avoid the automatic version check.

Risk: Cross-deck taste or template registry files may persist design preferences between runs.

Mitigation: Use a temporary SLIDE_MAKER_REGISTRY path or clear the registry when persistent local design memory is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dong845/skills/slide-maker)
- [Skill instructions](SKILL.md)
- [Design principles](references/design-principles.md)
- [Deck setup](references/deck-setup.md)
- [Security and capabilities](references/security-and-capabilities.md)
- [File inventory](references/file-inventory.md)
- [Review rubrics](references/review-rubrics.md)
- [Canvas formats](references/canvas-formats.md)
- [Image generation](references/image-generation.md)
- [Multilingual guidance](references/multilingual.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with generated Python, shell commands, configuration records, PowerPoint deck files, and review notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local slide-deck work directories, assets, renders, lint reports, and critic or handoff records.]

## Skill Version(s):

5.2.0 (source: server release evidence and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
