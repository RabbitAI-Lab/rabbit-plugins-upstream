## Description:

Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines, using dLazy for every slide image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can turn articles, reports, papers, notes, or outlines into visually unified image-based PowerPoint presentations. Each slide is a full-page generated image assembled into a PPTX file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An insecure API endpoint or redirect could expose the dLazy API key.

Mitigation: Before using a real key, confirm HTTPS enforcement and redirect handling prevent forwarding credentials to another site.

Risk: Source material and attached images are sent to dLazy for processing; uploaded images use returned public URLs.

Mitigation: Send only material authorized for dLazy processing, especially when it contains sensitive information.

Risk: Generation consumes account credits, and the shared runtime and configuration persist outside the skill installation.

Mitigation: Review expected credit use and manage persistent runtime data and configuration according to your organization's policies.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [Documentation and source repository](https://github.com/dlazy-ai/ai-ppt-slides)

## Skill Output:

**Output Type(s):** [PowerPoint presentation files, Slide images, Markdown guidance]

**Output Format:** [PPTX presentation with full-slide images; supporting Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Slides are full-page images rather than separately editable text, charts, or shapes.]

## Skill Version(s):

1.0.27 (source: server-resolved release metadata; artifact frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
