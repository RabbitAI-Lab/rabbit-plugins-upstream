## Description:

Find B-roll, stock footage, music, sound effects, motion blocks, lower thirds, transitions, fonts, icons, logos, LUTs and HDRIs that an AI agent can really fetch and legally put in a video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

External video creators and agents use this skill to choose searchable sources for footage, music, sound effects, graphics, fonts, and other video assets. It provides tested search examples and licensing checks, and helps record asset credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A downloadable asset may still have a license that does not allow the intended use, or may require attribution.

Mitigation: Check each asset's current license and attribution requirements before use; treat recorded credit details as supplied information, not proof of permission.

Risk: Optional downloaded tools may have risks when run with project access.

Mitigation: Review and pin optional npm tools before running them with project access.

Risk: Search terms may be sent to external services, including the publisher's fallback catalog.

Mitigation: Use generic, non-confidential search terms.

## Reference(s):

- [Every source we tested](artifact/references/all-sources.md)
- [Tested queries](artifact/references/tested-queries.md)
- [Traps and dead ends](artifact/references/traps.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, JSON]

**Output Format:** [Markdown guidance with shell query examples; JSON asset credits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asset use requires checking the current license and any required attribution.]

## Skill Version(s):

1.0.0 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
