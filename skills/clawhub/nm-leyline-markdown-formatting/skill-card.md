## Description:

Enforces markdown line-wrap and structure rules for clean git diffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, documentation writers, and agents use this skill to format committed Markdown with consistent line wrapping, heading spacing, list spacing, and reference-style links for cleaner reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad triggers may activate the skill during general markdown, documentation, style, or writing tasks.

Mitigation: Narrow activation triggers or invoke the skill explicitly when only committed Markdown formatting should be affected.

## Reference(s):

- [Hybrid Line Wrapping Rules](artifact/modules/wrapping-rules.md)
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline)
- [Google Markdown style guide](https://google.github.io/styleguide/docguide/style.html)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown formatting guidance and examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Applies prose wrapping at 80 characters while preserving code blocks, tables, frontmatter, link definitions, images, and other exempt Markdown structures.]

## Skill Version(s):

1.9.19 (source: release metadata; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
