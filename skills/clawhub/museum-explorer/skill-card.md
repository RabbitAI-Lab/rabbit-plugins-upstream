## Description:

museum-explorer helps agents plan museum and gallery visits, guide on-site exhibit interpretation, and create post-visit journals with checklist records, source notes, and SVG stamp assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to prepare exhibition visit cards, maintain on-site checklists, answer exhibit questions with source discipline, and produce printable post-visit journals with local records and SVG stamps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores visit notes, checklist updates, stamps, and optional local photo references in local journal and data folders.

Mitigation: Tell users before writing local visit records and keep photo handling local unless the user explicitly chooses otherwise.

Risk: Generated exhibition facts can become stale or may be marked pending when sources are incomplete.

Mitigation: Re-check key facts before travel and keep pending or conflicting facts visibly labeled with source dates.

Risk: Rendered journal HTML may request a webfont from a CDN when opened.

Mitigation: Review the generated HTML in environments where external font requests or network access are restricted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/museum-explorer)
- [README](README.md)
- [Source verification guide](references/source-verification.md)
- [Data sources guide](references/data-sources.md)
- [Stamp design guide](references/stamp-design-guide.md)
- [Exhibits schema](references/exhibits.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown, HTML journal data, JSON exhibit records, and SVG stamp files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local journal, checklist, exhibit data, photo references, and stamp files under the skill workspace.]

## Skill Version(s):

1.5.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
