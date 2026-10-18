## Description:

Builds, redesigns, and critiques presentation slide decks for a range of audiences and languages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

Presenters and teams use this skill to create or improve editable slide decks from their materials or a brief, with design planning, review, and hand-off guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deck validation can execute Python files adjacent to a presentation supplied by someone else.

Mitigation: Move untrusted PPTX files into a clean folder before validation, or inspect and trust any adjacent surface_*.py or style.py files first.

Risk: Deck building may install dependencies, use network-backed assets or version checks, and write a preference registry.

Mitigation: Review and authorize those operations before installation or use in a sensitive environment.

## Reference(s):

- [Slide Maker on ClawHub](https://clawhub.ai/dong845/skills/slide-maker)
- [Design principles](references/design-principles.md)
- [Security and capabilities](references/security-and-capabilities.md)

## Skill Output:

**Output Type(s):** [Presentation files, Code, Guidance]

**Output Format:** [Editable PPTX and rendered slide images, with an optional PDF and browser preview plus a concise hand-off note]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [PDF and browser preview are offered after the deck is finalized.]

## Skill Version(s):

5.9.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
