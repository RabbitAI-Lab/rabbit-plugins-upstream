## Description:

Generates visually unified image-based PowerPoint decks from articles, reports, papers, notes, or outlines using dLazy for every slide image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Presentation creators use this skill to turn source documents or outlines into consistent image-based PowerPoint decks with optional speaker notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A locally stored dLazy API key may be exposed on an untrusted or shared machine.

Mitigation: Protect the local configuration and rotate the key if the machine or shared runtime is not trusted.

Risk: Slide prompts, source text, and required reference images are sent to dLazy or the configured endpoint.

Mitigation: Confirm the destination and content-sharing policy before generating slides; review project files before sharing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [dLazy PPT documentation and source](https://github.com/dlazy-ai/ai-ppt-slides)

## Skill Output:

**Output Type(s):** [Files, Markdown, Images]

**Output Format:** [PowerPoint (.pptx), PNG slide images, and Markdown outline and speaker notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Slides are full-page images rather than separately editable PowerPoint elements.]

## Skill Version(s):

1.0.14 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
