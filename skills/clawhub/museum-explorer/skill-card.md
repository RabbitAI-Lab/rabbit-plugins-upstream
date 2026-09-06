## Description:

Museum Explorer helps agents plan museum visits, guide on-site exhibit exploration, and produce post-visit journals with stamp-style exhibit artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn museum or exhibition plans into a full visit workflow: pre-visit curation cards, on-site checklists and interpretation, and post-visit printable journals with exhibit stamps. It is especially suited to museum trips where source verification, local session state, and reusable exhibit data matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated local journals can execute improperly serialized user, web-sourced, or shared-note content.

Mitigation: Review journal data before generation, prefer script-safe JSON serialization and escaping, and avoid feeding untrusted exhibit data into the journal template without validation.

Risk: Older generated journal copies may not include the latest escaping and numeric clamping fixes.

Mitigation: Use the current template for new journals and avoid reusing older generated journal files as templates.

Risk: Generated journal HTML may contact jsDelivr for a remote font stylesheet.

Mitigation: Remove or locally vendor the remote font import when offline operation or external network minimization is required.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/bonniegeng-max/skills/museum-explorer)
- [Source verification guide](artifact/references/source-verification.md)
- [Data sources guide](artifact/references/data-sources.md)
- [Stamp design guide](artifact/references/stamp-design-guide.md)
- [Exhibit record schema](artifact/references/exhibits.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown, HTML journal data, SVG stamp markup, JSON exhibit records, and shell commands when synchronization is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local templates and local journal folders; generated journal HTML may load a remote stylesheet unless hardened or modified.]

## Skill Version(s):

1.6.1 (source: server release evidence and ClawHub Meta)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
