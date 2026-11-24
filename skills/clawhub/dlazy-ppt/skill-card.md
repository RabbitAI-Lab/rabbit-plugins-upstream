## Description:

Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines, using dLazy for every slide image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People preparing presentations can turn articles, reports, papers, notes, or outlines into visually consistent image based slide decks, with a PowerPoint file and optional presenter notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Slide content, images, and the API key are sent to the configured external service; the security scan flags this concern.

Mitigation: Only send material suitable for that service, keep DLAZY_API_KEY secret, and check that the configured endpoint uses HTTPS.

Risk: The security scan was partial and reports that dependency versions are not fully pinned.

Mitigation: Review dependency versions and the unresolved scan concerns before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [Project homepage listed in skill metadata](https://github.com/dlazy-ai/ai-ppt-slides)

## Skill Output:

**Output Type(s):** [PowerPoint presentations, Slide images, Markdown]

**Output Format:** [Image based .pptx presentation, PNG slide images, and optional outline.md and speech.md files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each slide is a complete image; text, charts, and shapes are not separately editable in the PowerPoint deck.]

## Skill Version(s):

1.0.34 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
