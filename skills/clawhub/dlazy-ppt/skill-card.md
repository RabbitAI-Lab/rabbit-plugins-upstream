## Description:

Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines, using dLazy for every slide image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to turn source material into visually unified image-based PowerPoint decks with generated slide images, speaker notes, and assembled PPTX output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached local images may be sent to dLazy for cloud image generation.

Mitigation: Use this skill only when cloud processing by dLazy is acceptable, and avoid sensitive source images or documents unless that transfer is approved.

Risk: The skill can store a reusable dLazy API key in a local runtime configuration file.

Mitigation: Protect the local configuration file, rotate or revoke the key if exposed, and avoid sharing runtime directories that may contain credentials.

Risk: The skill may install Python packages into a shared local virtual environment.

Mitigation: Install and run it in a trusted environment where shared local runtime files are acceptable.

Risk: Generated decks use full-slide images, so slide text, charts, and shapes are not individually editable after assembly.

Mitigation: Use this skill when image-based slides are acceptable, and choose a different workflow when editable PowerPoint objects are required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [Project homepage](https://github.com/dlazy-ai/ai-ppt-slides)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [Image Generation CLI](docs/image-generation-cli.md)
- [Workflow Gates And Progress](docs/workflow-gates-and-progress.md)
- [Slide Generation And Subagents](docs/slide-generation-and-subagents.md)
- [Project Assembly And Reporting](docs/project-assembly-and-reporting.md)
- [Style Library](docs/style-library.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, JSON project files, PNG slide images, speaker notes, and PPTX decks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses full-slide 16:9 images; final slide text and visuals are image-based rather than independently editable PowerPoint objects.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata; artifact frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
