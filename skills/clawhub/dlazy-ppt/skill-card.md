## Description:

Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines, using dLazy for every slide image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn source material into visually consistent, image-based PowerPoint decks with slide images, speaker notes, and final PPTX assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a dLazy API key and sends network requests for slide-image generation.

Mitigation: Use a dedicated or revocable dLazy key, prefer the default https://dlazy.com endpoint, and avoid custom base URLs unless they are fully trusted.

Risk: User-provided presentation images or assets may be uploaded to dLazy-controlled storage.

Mitigation: Review source assets before generation and avoid submitting sensitive or restricted material unless the upload destination is acceptable.

Risk: The local runtime is shared across agents and uses Python dependencies.

Mitigation: Use a dedicated output directory and review or pin dependency versions before use in sensitive environments.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [Project homepage](https://github.com/dlazy-ai/ai-ppt-slides)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [Image generation CLI](docs/image-generation-cli.md)
- [Workflow gates and progress](docs/workflow-gates-and-progress.md)
- [Project assembly and reporting](docs/project-assembly-and-reporting.md)

## Skill Output:

**Output Type(s):** [files, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON project state, PNG slide images, speaker notes, and PPTX deck files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces full-slide image decks through dLazy, with approval gates, recorded slide-job state, and optional reusable style guidance.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata; artifact SKILL.md frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
