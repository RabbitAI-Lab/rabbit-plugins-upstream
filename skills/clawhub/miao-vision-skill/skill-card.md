## Description:

Create self-contained Miao Vision artifacts from article URLs, local Markdown or text, and local tabular data, including infographics, HTML or PDF reports, single-page data posters, browser decks, and report or deck spec validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[miaoshou.dev](https://clawhub.ai/user/miaoshou.dev)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to turn local data or article content into shareable visual artifacts while keeping source data local. It also helps validate existing Miao Vision report or deck specs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can discover, install, and execute a local Miao Vision CLI, and the shared CLI can persist outside the plugin lifecycle.

Mitigation: Review before installing, approve the installer only when the displayed source and destination are expected, and remove the shared CLI explicitly by deleting ~/.miao-vision when it is no longer needed.

Risk: CLI resolution can select executables from configured locations or PATH, which may be unsafe in sensitive environments without provenance controls.

Mitigation: Prefer a trusted absolute CLI under MIAO_VISION_HOME or ~/.miao-vision, keep PATH controlled, and avoid the unpinned global compatibility install path for sensitive environments.

## Reference(s):

- [Article Infographic Workflow](artifact/references/article.md)
- [Data Report Workflow](artifact/references/report.md)
- [Browser Deck Workflow](artifact/references/deck.md)
- [Outcome Brief Plan-First Workflow](artifact/references/outcome-brief.md)
- [Miao Vision Plugin Bundle](https://github.com/miaoshou-dev/miao-vision/releases/latest/download/miao-vision-plugin.zip)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands and generated HTML, PDF, PNG, JSON, or YAML artifact files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use local CLI execution and create delivery directories for generated artifacts; source data is intended to remain local.]

## Skill Version(s):

0.7.0 (source: server release evidence, install/README.md, cli-compatibility.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
