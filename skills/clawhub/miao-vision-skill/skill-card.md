## Description:

Create self-contained local-first Miao Vision artifacts for article infographics, data reports, browser decks, and report or deck spec validation when explicitly invoked with supported input.

This skill is ready for commercial/non-commercial use.

## Publisher:

[miaoshou.dev](https://clawhub.ai/user/miaoshou.dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Miao Vision to turn a user-provided article URL, local Markdown or text, or local CSV, TSV, XLSX, or JSON data into a self-contained infographic, HTML/PDF report, browser deck, or validated report/deck specification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may download and install a local Miao Vision CLI when no compatible executable exists, and environment variables can affect the selected install path or release repository.

Mitigation: Install only when the publisher is trusted, review the approval prompt, and check MIAO_VISION_HOME and MIAO_VISION_RELEASE_REPOSITORY before approving; the bundled installers verify SHA-256 checksums before installing.

Risk: Generated visual artifacts can expose local source data if prepared for third-party sharing without review.

Mitigation: Keep data local by default, use the skill's trusted interactive report checks only when needed, and review share-safety status before delivering artifacts outside the local workflow.

Risk: Reports or decks can mislead readers if metrics, claims, or recommendations are not grounded in source evidence.

Mitigation: Use the documented strict validation, evidence provenance, coverage checks, and sample warnings; do not add unsupported metrics, causal claims, or forecasts.

## Reference(s):

- [Miao Vision ClawHub skill page](https://clawhub.ai/miaoshou.dev/skills/miao-vision-skill)
- [Miao Vision plugin installation](artifact/install/README.md)
- [Article Infographic Workflow](artifact/references/article.md)
- [Data Report Workflow](artifact/references/report.md)
- [Browser Deck Workflow](artifact/references/deck.md)
- [Miao Vision plugin bundle download](https://github.com/miaoshou-dev/miao-vision/releases/latest/download/miao-vision-plugin.zip)

## Skill Output:

**Output Type(s):** [Files, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown delivery response with paths to generated HTML, PDF, PNG, or browser-deck artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are local artifacts; the skill limits default delivery summaries to concise manifest-backed status, metrics, highlights, warnings, and actions.]

## Skill Version(s):

0.3.1 (source: server release evidence, target metadata, and cli-compatibility.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
