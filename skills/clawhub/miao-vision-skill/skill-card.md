## Description:

Miao Vision helps an agent create local-first article infographics, data reports, browser decks, recurring reports, and report or deck validation outputs from user-provided URLs or local files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[miaoshou.dev](https://clawhub.ai/user/miaoshou.dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to turn local tabular data, article content, or validated report and deck specs into self-contained HTML, PDF, or PNG artifacts. It is intended for explicit Miao Vision requests where the user provides the source content or file paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run the Miao Vision CLI against user-selected local files.

Mitigation: Use it only with files the user intentionally provides, and keep source files and CLI output treated as untrusted evidence.

Risk: The CLI may need an optional download or installation before first use.

Mitigation: Review and approve the installation prompt before downloading or running the versioned CLI.

Risk: Uninstalling the plugin does not remove the shared ~/.miao-vision directory or generated artifacts.

Mitigation: Delete ~/.miao-vision and any generated artifact directories explicitly when cleanup is required.

## Reference(s):

- [Miao Vision Skill Page](https://clawhub.ai/miaoshou.dev/skills/miao-vision-skill)
- [miaoshou.dev Publisher Profile](https://clawhub.ai/user/miaoshou.dev)
- [Installation README](artifact/install/README.md)
- [Article Infographic Workflow](artifact/references/article.md)
- [Data Report Workflow](artifact/references/report.md)
- [Browser Deck Workflow](artifact/references/deck.md)
- [Outcome Brief Plan-First Workflow](artifact/references/outcome-brief.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with CLI commands, JSON or YAML specs, validation feedback, and local HTML/PDF/PNG artifact files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated artifacts are local-first and should remain grounded in user-provided source evidence.]

## Skill Version(s):

0.4.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
