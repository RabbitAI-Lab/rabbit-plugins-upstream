## Description:

Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines, using dLazy for every slide image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external users use this skill to turn source material into visually consistent PowerPoint decks with full-slide generated images, speaker notes, prompt state, and final PPTX assembly. It is best suited when image-based slides are acceptable rather than separately editable textbox, chart, or shape objects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Slide prompts and attached source images are sent to the configured dLazy endpoint for generation.

Mitigation: Review source material for sensitive business data or restricted figures before generation, and configure the dLazy endpoint intentionally.

Risk: The skill stores dLazy runtime configuration and API credentials under the shared ~/.dlazy-ppt location.

Mitigation: Use the documented configuration command, keep the API key scoped to the intended organization, and rotate or revoke the key from dLazy if access changes.

Risk: Generated full-slide images may misrepresent text, figures, labels, or visual details from supplied assets.

Mitigation: Inspect each slide before assembly, validate required figures against the source assets, and regenerate or edit slides with concrete prompts when issues are found.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [dLazy AI PPT Slides homepage](https://github.com/dlazy-ai/ai-ppt-slides)
- [Image generation CLI](docs/image-generation-cli.md)
- [Image model configuration](docs/image-model-configuration.md)
- [Project assembly and reporting](docs/project-assembly-and-reporting.md)
- [Slide generation and subagents](docs/slide-generation-and-subagents.md)
- [User-supplied assets](docs/user-supplied-assets.md)
- [Built-in visual style references](references/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with JSON prompt/state files, PNG slide images, speaker notes, and PPTX output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses python3, a required DLAZY_API_KEY, optional dLazy endpoint/model settings, and project-local deck artifacts such as outline.md, speech.md, slide_jobs.json, slide_run_state.json, origin_image/slide_XX.png, and the assembled .pptx file.]

## Skill Version(s):

1.0.11 (source: server release evidence; packaged SKILL.md frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
