## Description:

Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines, using dLazy for every slide image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and content teams use this skill to turn source material into visually unified image-based PowerPoint decks through dLazy. It is best suited when complete slide images are acceptable instead of separately editable text boxes, charts, and shapes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached source images are sent to dLazy using the user's dLazy API key.

Mitigation: Review source material for sensitivity before generation and use only approved dLazy accounts and inputs.

Risk: The skill stores shared runtime configuration under ~/.dlazy-ppt.

Mitigation: Protect local runtime files, restrict machine access, and rotate or revoke dLazy API keys when access changes.

Risk: Dependency versions may need tighter control in stricter environments.

Mitigation: Install with a lockfile or constraints file that pins patched versions of python-pptx, Pillow, requests, and filelock.

Risk: Generated decks use full-slide images, so individual text boxes, charts, and shapes are not separately editable.

Mitigation: Use this skill only when image-based slides meet the workflow need; choose a native PowerPoint authoring workflow when editability is required.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [dLazy PPT Source/Homepage](https://github.com/dlazy-ai/ai-ppt-slides)
- [dLazy](https://dlazy.com)
- [dLazy API Key Dashboard](https://dlazy.com/dashboard/organization/api-key)
- [Image Generation CLI](artifact/docs/image-generation-cli.md)
- [Image Model Configuration](artifact/docs/image-model-configuration.md)
- [Workflow Gates And Progress](artifact/docs/workflow-gates-and-progress.md)
- [Slide Generation And Subagents](artifact/docs/slide-generation-and-subagents.md)
- [Project Assembly And Reporting](artifact/docs/project-assembly-and-reporting.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, JSON project/job files, PNG slide images, PPTX deck files, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces image-based 16:9 slide decks by default; final slide content is not separately editable as native PowerPoint objects.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
