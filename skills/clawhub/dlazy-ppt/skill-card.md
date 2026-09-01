## Description:

Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines, using dLazy for every slide image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn source articles, reports, papers, notes, or outlines into visually unified image-based PowerPoint decks. It guides outline approval, style selection, dLazy slide image generation, QA, speaker notes, and final PPTX assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Slide prompts and attached source images or figures are sent to dLazy under the user's organization key.

Mitigation: Use the skill only with documents and assets that are acceptable to upload to dLazy, and avoid confidential materials unless that data handling is approved.

Risk: The shared Python runtime installs dependencies from version ranges rather than fully pinned versions.

Mitigation: Review or pin dependency versions before production use.

Risk: Deck generation depends on the dLazy API key, selected image tool, required source images, and slide subagent availability.

Mitigation: Run the bundled runtime readiness check and verify required image paths before full-deck generation; report blockers instead of creating substitute outputs.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [dLazy PPT source and documentation](https://github.com/dlazy-ai/ai-ppt-slides)
- [Image generation CLI](docs/image-generation-cli.md)
- [Slide generation and subagents](docs/slide-generation-and-subagents.md)
- [Project assembly and reporting](docs/project-assembly-and-reporting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, JSON slide job files, shell commands, PNG slide images, speaker notes, and PPTX decks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Final decks are assembled from generated 16:9 full-slide images and require a configured dLazy API key for normal operation.]

## Skill Version(s):

1.0.2 (source: server release evidence; artifact frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
