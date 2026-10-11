## Description:

Builds, redesigns, and critiques presentation-grade slide decks tailored to the audience and source material.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

Presenters, researchers, educators, and teams use this skill to create, revise, and review PowerPoint decks from their requirements and source materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Validation of an untrusted deck folder can execute Python files named surface_*.py placed beside the deck.

Mitigation: Move the .pptx into a clean folder before validation, or inspect adjacent Python files first.

Risk: Local scripts, Python package installation, networked image/icon/version checks, and a stored taste/profile registry expand the tool's access and persistence.

Mitigation: Use an isolated virtual environment or container, and apply the documented opt-outs for capabilities you do not need.

## Reference(s):

- [Slide Maker release](https://clawhub.ai/dong845/skills/slide-maker)
- [Design principles](artifact/references/design-principles.md)
- [Security and capabilities](artifact/references/security-and-capabilities.md)

## Skill Output:

**Output Type(s):** [Presentation files, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Editable PowerPoint (.pptx) decks with text-based plans, review feedback, and handoff notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include rendered slide previews and source citations when relevant.]

## Skill Version(s):

5.8.0 (source: ClawHub release and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
