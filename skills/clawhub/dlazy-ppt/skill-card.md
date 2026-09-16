## Description:

Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines, using dLazy for every slide image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and presentation creators use this skill to turn source material into visually consistent image-based PowerPoint decks. It is best suited for finished presentation pages where full-slide generated images are acceptable rather than separately editable text boxes, charts, and shapes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Slide prompts and attached source images may be sent to dLazy or to a configured dLazy-compatible endpoint.

Mitigation: Review source material before generation, avoid sensitive inputs when policy prohibits external processing, and use only the default dLazy service or a deliberately trusted self-hosted endpoint.

Risk: A reusable dLazy API key is stored under ~/.dlazy-ppt for repeated use by local agents.

Mitigation: Protect the local runtime directory, rotate the key if endpoint configuration may have been tampered with, and review DLAZY_BASE_URL before running generation commands.

Risk: The runtime bootstrap can install unpinned packages into a shared environment.

Mitigation: Run the skill in a locked or reviewed runtime when package provenance matters, and inspect dependency changes before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [Project homepage from OpenClaw metadata](https://github.com/dlazy-ai/ai-ppt-slides)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [Image generation CLI](artifact/docs/image-generation-cli.md)
- [Image model configuration](artifact/docs/image-model-configuration.md)
- [Workflow gates and progress](artifact/docs/workflow-gates-and-progress.md)
- [Slide generation and subagents](artifact/docs/slide-generation-and-subagents.md)
- [Project assembly and reporting](artifact/docs/project-assembly-and-reporting.md)
- [Built-in visual style references](artifact/references/)

## Skill Output:

**Output Type(s):** [Files, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON job and state files, PNG slide images, and PPTX deck files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and a DLAZY_API_KEY; uses approval gates before final deck artifacts are generated.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
