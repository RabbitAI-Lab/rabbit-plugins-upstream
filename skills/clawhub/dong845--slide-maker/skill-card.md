## Description:

Builds, redesigns, and critiques editable presentation-grade PowerPoint decks from user-provided material, templates, or research inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, researchers, educators, and presenters use this skill to turn source material into polished editable decks, redesign existing presentations, or critique slide quality. It supports template matching, multilingual decks, visual asset preparation, rendering, linting, and critic review workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically modify the local Python environment and run broad local automation workflows.

Mitigation: Install and run it in a dedicated virtual environment or disposable workspace, and review its actions before processing sensitive decks.

Risk: The skill may use web research, local template or taste registries, generated assets, and session-derived image outputs.

Mitigation: Use the documented opt-outs for automatic dependency or version checks and review confidentiality requirements before providing private source material.

Risk: Generated or researched slide content can become misleading if source fidelity is not reviewed.

Mitigation: Keep the built-in review, lint, and actor-critic checks enabled and verify claims against supplied source material before presentation.

## Reference(s):

- [Slide Maker on ClawHub](https://clawhub.ai/dong845/skills/slide-maker)
- [Publisher profile](https://clawhub.ai/user/dong845)
- [Design principles](references/design-principles.md)
- [Deck setup](references/deck-setup.md)
- [File inventory](references/file-inventory.md)
- [Troubleshooting and FAQ](references/troubleshooting-faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance, Python/PPTX build code, shell commands, configuration notes, and generated deck files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce editable PPTX decks, rendered slide images, review records, and validation artifacts depending on the user's request.]

## Skill Version(s):

5.0.0 (source: server release evidence and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
