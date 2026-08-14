## Description:

Create a self-contained Miao Vision artifact when the user explicitly invokes $miao-vision and supplies an article URL or local Markdown/text for an infographic, or local Markdown/text and optional CSV, TSV, XLSX, or JSON data for an HTML/PDF report or browser deck.

This skill is ready for commercial/non-commercial use.

## Publisher:

[miaoshou.dev](https://clawhub.ai/user/miaoshou.dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to turn local articles, Markdown/text, and structured data into self-contained infographics, reports, decks, or validation-ready visualization specs. It is designed for local-first visualization workflows that need grounded claims, strict validation, and concise delivery paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires local shell execution through the Miao Vision CLI.

Mitigation: Use it only in an agent environment where shell execution is expected, review requested commands, and keep execution scoped to user-provided inputs and skill resources.

Risk: First use may install a persistent CLI executable under ~/.miao-vision/bin.

Mitigation: Approve installation only after reviewing the installer source; remove ~/.miao-vision when the shared CLI is no longer wanted.

Risk: Generated reports, decks, or infographics can contain misleading claims if source evidence is weak or validation warnings are ignored.

Mitigation: Follow the skill's strict validation and grounding rules, preserve caveats, and do not describe artifacts as verified unless validation succeeds.

## Reference(s):

- [Miao Vision ClawHub Skill Page](https://clawhub.ai/miaoshou.dev/skills/miao-vision-skill)
- [Miao Vision Skill Source](artifact/SKILL.md)
- [Plugin Installation](artifact/install/README.md)
- [Article Infographic Workflow](artifact/references/article.md)
- [Data Report Workflow](artifact/references/report.md)
- [Browser Deck Workflow](artifact/references/deck.md)
- [Outcome Brief Plan-First Workflow](artifact/references/outcome-brief.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown delivery guidance with shell command examples and generated local artifact files such as HTML, PDF, PNG, JSON, or YAML.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are local-first and should include the requested artifact path, concise status, grounded metrics or highlights when available, and blocking structured errors when rendering or validation fails.]

## Skill Version(s):

0.5.0 (source: ClawHub release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
