## Description:

Create self-contained local-first visual artifacts from user-provided article content, local Markdown/text, or local CSV/TSV/XLSX/JSON data, including infographics, HTML/PDF reports, browser decks, and report or deck spec validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[miaoshou.dev](https://clawhub.ai/user/miaoshou.dev)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use Miao Vision to turn local articles, documents, and tabular datasets into self-contained visual reports, infographics, or browser decks while keeping source data local. They can also validate report or deck specs before rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the shared Miao Vision CLI adds a local executable under ~/.miao-vision when no compatible CLI is already present.

Mitigation: Approve installation only when comfortable with the Miao Vision GitHub release binary; the installer verifies checksums, and removal is deleting ~/.miao-vision.

Risk: The skill can fetch a user-provided article URL and render local files into shareable HTML, PDF, or PNG artifacts that may contain source data.

Mitigation: Use explicit $miao-vision invocation, review install and render prompts, and treat generated reports as local artifacts unless separately choosing to share them.

Risk: Generated visual artifacts may contain incorrect or misleading claims if source data, webpages, or specs are malformed or ambiguous.

Mitigation: Keep metrics grounded in source evidence, use the CLI validation workflows, and review warnings before delivery.

## Reference(s):

- [Miao Vision Skill Listing](https://clawhub.ai/miaoshou.dev/skills/miao-vision-skill)
- [Miao Vision Release Bundle](https://github.com/miaoshou-dev/miao-vision/releases/latest/download/miao-vision-plugin.zip)
- [Article Infographic Workflow](artifact/references/article.md)
- [Data Report Workflow](artifact/references/report.md)
- [Browser Deck Workflow](artifact/references/deck.md)
- [Outcome Brief Plan-First Workflow](artifact/references/outcome-brief.md)
- [Plugin Installation](artifact/install/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands, JSON/YAML specs, and self-contained HTML, PDF, or PNG artifact files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-first artifact generation; PDF and PNG exports may require optional browser dependencies, and CLI installation downloads a checksum-verified release binary only with approval.]

## Skill Version(s):

0.6.1 (source: server release evidence and cli-compatibility.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
