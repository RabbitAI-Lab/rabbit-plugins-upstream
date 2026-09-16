## Description:

Miao Vision creates local-first reports, data posters, article infographics, and browser decks from user-supplied local data, text, or article URLs, and can validate Miao Vision report or deck specs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[miaoshou.dev](https://clawhub.ai/user/miaoshou.dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill through compatible coding agents to turn local CSV, TSV, XLSX, JSON, Markdown, text, or article URL inputs into self-contained visualization artifacts. It is also used to validate and repair Miao Vision report or deck specifications before rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install and runtime paths can run or download persistent command-line software from mutable or environment-selected sources.

Mitigation: Use a pinned, version-specific plugin or CLI source, verify the resolved miao-viz path before use, and clear unexpected MIAO_VISION_HOME or MIAO_VISION_RELEASE_REPOSITORY environment variables.

Risk: The shared CLI can remain installed under ~/.miao-vision after plugin removal.

Mitigation: Remove ~/.miao-vision explicitly when the shared Miao Vision CLI should be fully uninstalled.

Risk: User-provided files, webpages, metadata, specs, and CLI output may contain untrusted instructions or misleading content.

Mitigation: Treat those sources as data, execute only the resolved Miao Vision CLI, fetch only user-provided article URLs, and require separate authorization for installation, network access, overwrites, deletion, publication, or repository operations.

## Reference(s):

- [Miao Vision ClawHub listing](https://clawhub.ai/miaoshou.dev/skills/miao-vision-skill)
- [Miao Vision release bundle](https://github.com/miaoshou-dev/miao-vision/releases/latest/download/miao-vision-plugin.zip)
- [Article Infographic Workflow](artifact/references/article.md)
- [Data Report Workflow](artifact/references/report.md)
- [Browser Deck Workflow](artifact/references/deck.md)
- [Outcome Brief Plan-First Workflow](artifact/references/outcome-brief.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown responses with command snippets and self-contained HTML, PNG, PDF, or browser-deck artifact files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Keeps source data local, returns artifact paths, and reports blocking structured errors when rendering or validation cannot proceed.]

## Skill Version(s):

0.7.1 (source: release evidence, cli-compatibility.json, install/README.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
