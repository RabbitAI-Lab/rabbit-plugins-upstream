## Description:

Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines, using dLazy for every slide image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and presentation creators use this skill to turn source material into visually unified image-based PowerPoint decks. It is best suited when full-slide generated images are acceptable rather than separately editable slide objects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and uses a dLazy API key.

Mitigation: Use a dedicated, revocable dLazy API key and avoid placing the key directly in shell commands.

Risk: Prompts and user-supplied assets may be sent to dLazy or to a configured service URL.

Mitigation: Leave DLAZY_BASE_URL at the default unless you control the endpoint, and avoid confidential documents or assets unless sending them to dLazy is acceptable.

Risk: The runtime can bootstrap Python dependencies that are not pinned to exact versions.

Mitigation: Install dependencies in an isolated environment with reviewed, pinned packages when using shared or sensitive machines.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [dLazy PPT source homepage](https://github.com/dlazy-ai/ai-ppt-slides)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [Image Generation CLI](docs/image-generation-cli.md)
- [Image Model Configuration](docs/image-model-configuration.md)
- [Workflow Gates And Progress](docs/workflow-gates-and-progress.md)
- [Outline, Style, And Sample](docs/outline-style-and-sample.md)
- [User-Supplied Assets](docs/user-supplied-assets.md)
- [Slide Generation And Subagents](docs/slide-generation-and-subagents.md)
- [Project Assembly And Reporting](docs/project-assembly-and-reporting.md)
- [Style Library](docs/style-library.md)
- [Slide Worker Prompt](prompts/slide-worker.md)
- [党政红风格](references/党政红风格.md)
- [创意杂志风](references/创意杂志风.md)
- [复古扁平插画风](references/复古扁平插画风.md)
- [手绘技术解释风](references/手绘技术解释风.md)
- [手绘白板风](references/手绘白板风.md)
- [教学课件风](references/教学课件风.md)
- [数据仪表盘风](references/数据仪表盘风.md)
- [清爽专业风](references/清爽专业风.md)
- [温暖手工风](references/温暖手工风.md)
- [电子墨水杂志风](references/电子墨水杂志风.md)
- [科研答辩风](references/科研答辩风.md)
- [麦肯锡风格](references/麦肯锡风格.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with shell commands, JSON prompt and state files, PNG slide images, speaker notes, and PPTX deck output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and a dLazy API key; generated slide images may send prompts and assets to dLazy.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
