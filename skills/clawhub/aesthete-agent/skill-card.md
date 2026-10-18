## Description:

Helps agents design, validate, preview, and export color systems for frontend interfaces and visual content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and design teams use this skill to select accessible color palettes, check contrast and color-blind distinctions, preview designs, and export reusable design tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tool writes generated reports or previews and updates local preference files.

Mitigation: Review output paths and back up preference files before running write-enabled commands.

Risk: The source-collection playbook describes third-party browser harvesting around Cloudflare.

Mitigation: Do not follow collection steps without permission from the source site.

Risk: Unpinned npx, uvx, or MCP installation can retrieve changing third-party packages.

Mitigation: Prefer pinned versions or reviewed local artifacts before installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/docsor1212/skills/aesthete-agent)
- [Color theory and accessibility reference](artifact/references/color-theory.md)
- [Five-lens design critique](artifact/references/critique.md)
- [Visual showcase](https://docsor1212.github.io/aesthete-agent/demo/showcase.html)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration, Markdown]

**Output Format:** [Text, CSS or design-token JSON, HTML previews, and Markdown reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes contrast and color-blindness checks and optional local preview files.]

## Skill Version(s):

0.6.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
