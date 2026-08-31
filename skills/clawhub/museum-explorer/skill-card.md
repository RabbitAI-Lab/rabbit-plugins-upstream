## Description:

Museum Explorer helps agents plan museum visits, verify exhibit information, support on-site exhibit interpretation, and create post-visit digital journals with collectible stamp assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to prepare for museum exhibitions, continue context during an on-site visit, and turn visit notes into shareable or printable journals. It is intended for museum trip planning, exhibit checklists, source-backed interpretation, local journaling, and SVG stamp generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates and updates local journal and exhibition data files.

Mitigation: Tell users when a local session directory or journal file is created or updated, and keep visit records under the documented local journal folder.

Risk: Museum opening hours, prices, exhibition status, and exhibit details can become stale or conflict across sources.

Mitigation: Use the documented source-verification workflow, show retrieval dates, require independent sources for key facts, and mark uncertain items as pending.

Risk: The skill includes guidance for browsing public museum sources and synchronizing exhibition data.

Mitigation: Limit collection to public official or authoritative sources, avoid restricted or undocumented endpoints, and summarize changes after data updates.

Risk: Photo inputs and post-visit journal materials may contain personal visit context.

Mitigation: Keep photos and generated journals local by default, use relative paths or local copies, and allow users to decline photo use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/museum-explorer)
- [Source verification guide](artifact/references/source-verification.md)
- [Data sources guide](artifact/references/data-sources.md)
- [Stamp design guide](artifact/references/stamp-design-guide.md)
- [Exhibit record schema](artifact/references/exhibits.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown, HTML, JSON data updates, SVG assets, and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local session files, curation cards, on-site checklists, digital journal HTML, source tables, and SVG stamp assets.]

## Skill Version(s):

1.4.0 (source: server release evidence and ClawHub Meta)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
