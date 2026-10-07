## Description:

Builds, redesigns, and critiques presentation-grade slide decks for audiences ranging from researchers to business stakeholders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

People preparing presentations use this skill to create or improve PowerPoint decks from their requirements and source materials, or to obtain a critique of an existing deck.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Validation may execute Python files placed beside a deck, including files supplied by someone else.

Mitigation: Inspect or remove adjacent Python files before processing an unfamiliar deck, or work in a clean folder or container.

Risk: The slide-building workflow can install Python packages, run local renderers, use network or image tools, and retain a small taste/profile registry.

Mitigation: Review these capabilities before installation and permit them only in an environment where their effects are acceptable.

## Reference(s):

- [ClawHub Slide Maker listing](https://clawhub.ai/dong845/skills/slide-maker)
- [Design principles](artifact/references/design-principles.md)
- [Security and capabilities](artifact/references/security-and-capabilities.md)

## Skill Output:

**Output Type(s):** [PowerPoint files, Markdown feedback and guidance]

**Output Format:** [PPTX deck; optional PDF and HTML preview; written critique and handoff]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional supporting assets and render previews]

## Skill Version(s):

5.7.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
