## Description:

Build a company or portfolio-level patent landscape for small-RNA therapeutics from a supplied patent list or defined search scope.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users, patent analysts, IP teams, and R&D strategy teams use this skill to turn supplied patent identifiers or a defined small-RNA search scope into a traceable landscape, workbook, and interactive evidence timeline. The workflow supports ASO, siRNA, miRNA, mRNA, aptamer, guide RNA, and other oligonucleotide portfolio analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential company, portfolio, patent search scope, or generated IP strategy material may be sensitive.

Mitigation: Confirm authorization before using external patent services and protect generated evidence workbooks, reports, and local project files.

Risk: Patent status, claim scope, term, FTO, infringement, validity, or patentability conclusions may be misread as legal advice.

Mitigation: Treat the skill output as a landscape and strategy aid, verify material legal status in official registers, and review legal conclusions with qualified counsel.

Risk: Incomplete or missing patent records can lead to incorrect tags, timelines, or opportunity hypotheses.

Mitigation: Preserve retrieval logs, source URLs, missing-field markers, confidence levels, and human review state; do not substitute claims or create opportunity markers without evidence.

Risk: A local scaffold could overwrite analyst work if pointed at an existing project.

Mitigation: Use the provided scaffold behavior that refuses non-empty directories and choose a new project directory for reruns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/map-small-rna-patent-landscape-ls)
- [Patent Search MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [Patent Briefing MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [Small-RNA Patent Tag Taxonomy](references/tag-taxonomy.md)
- [Small-RNA Patent Landscape Workbook Schema](references/workbook-schema.md)
- [Multidimensional Small-RNA Patent Timeline Specification](references/html-dashboard.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown evidence files, JSON, CSV, XLSX workbook, self-contained HTML timeline, and local scaffold files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are generated locally from a structured analysis layer; the scaffold script creates a version-safe project directory and refuses non-empty targets.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
