## Description:

Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines, using dLazy for every slide image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users preparing presentations can turn articles, reports, papers, notes, or outlines into visually unified decks with one full-slide image per page.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated connections or redirects can expose the dLazy API key.

Mitigation: Restrict authenticated connections to HTTPS and protect redirects against destination changes or downgrades.

Risk: Slide prompts and selected images are sent to dLazy for generation.

Mitigation: Use only material approved for that service.

Risk: The API key and runtime configuration persist in a shared runtime directory.

Mitigation: Limit access to the runtime directory and its key configuration.

## Reference(s):

- [Project homepage and documentation](https://github.com/dlazy-ai/ai-ppt-slides)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-ppt)

## Skill Output:

**Output Type(s):** [PowerPoint files, Slide images, Markdown project documents]

**Output Format:** [PPTX decks assembled from full-slide 16:9 images, with PNG slide assets and Markdown project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Slides are flattened images; individual text, charts, and shapes are not editable.]

## Skill Version(s):

1.0.26 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
