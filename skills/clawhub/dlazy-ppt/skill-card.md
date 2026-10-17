## Description:

Generates visually consistent, image-based PowerPoint decks from articles, reports, papers, notes, or outlines using dLazy for slide images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Presentation creators and teams use this skill to turn source material into cohesive image-based PPTX decks with optional speaker notes. Slides are full-page images rather than individually editable elements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied images used for slide generation or editing are uploaded to dLazy cloud services.

Mitigation: Avoid confidential material unless dLazy's data handling is acceptable for your use case.

Risk: The skill stores a dLazy API key in local configuration and uses a shared Python runtime.

Mitigation: Protect the local API-key file and review the runtime setup before installing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [Publisher-listed project documentation](https://github.com/dlazy-ai/ai-ppt-slides)
- [Image generation instructions](artifact/docs/image-generation-cli.md)
- [Project assembly and reporting](artifact/docs/project-assembly-and-reporting.md)

## Skill Output:

**Output Type(s):** [Markdown, Configuration, Image files, PowerPoint files, Guidance]

**Output Format:** [Markdown outline and speaker notes, JSON slide jobs, PNG slide images, and PPTX deck]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [PowerPoint pages are full-slide images; individual slide elements are not separately editable.]

## Skill Version(s):

1.0.21 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
