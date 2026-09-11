## Description:

Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines, using dLazy for every slide image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to turn source material into a visually consistent PowerPoint deck. It is best suited for image-based slides where unified visual design is more important than separately editable slide objects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and transmits a dLazy API key and may send prompts or uploaded images to the configured dLazy endpoint.

Mitigation: Review before installing, use the default https://dlazy.com endpoint unless a self-hosted server is intentionally trusted, and avoid confidential source documents or images unless approved for dLazy processing.

Risk: A changed or untrusted base URL could receive API credentials, prompts, and uploaded image inputs.

Mitigation: Rotate the dLazy API key if the base URL may have been changed and verify endpoint configuration before use.

Risk: The runtime bootstrap installs dependencies from floating requirements ranges.

Mitigation: Prefer a locked or reviewed dependency installation before using the skill in a production environment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [Publisher Profile](https://clawhub.ai/user/dlazyai)
- [Project Homepage](https://github.com/dlazy-ai/ai-ppt-slides)
- [Image Generation CLI](docs/image-generation-cli.md)
- [Project Assembly And Reporting](docs/project-assembly-and-reporting.md)
- [Workflow Gates And Progress](docs/workflow-gates-and-progress.md)
- [Slide Generation And Subagents](docs/slide-generation-and-subagents.md)
- [Style Library](docs/style-library.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance, JSON prompt and state files, PNG slide images, and PPTX presentation files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Decks use full-slide generated images; final PPTX files may include speaker notes when speech.md is present.]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
