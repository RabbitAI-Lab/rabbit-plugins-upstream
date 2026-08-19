## Description:

Create or rigorously review a source-traceable HTML technology-insight report that integrates patents, scientific literature, market and company evidence, standards, regulation, engineering evidence, technology routes, competitive context, candidate evidence gaps, emerging applications, claim-relevance screening, technical options, and decision actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

R&D, strategy, product, and IP teams use this skill to produce or audit decision-ready HTML technology insight reports that combine patent, scientific, market, company, standards, regulatory, engineering, and application evidence. It is suited to technology-domain reports, localization or reconciliation of existing report packages, and preliminary patent claim-relevance review queues that require specialist follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential or unauthorized research inputs could be exposed during broad technology and patent research.

Mitigation: Confirm confidentiality, research authorization, permitted source access, output path, and overwrite permission before beginning; avoid exposing confidential material through external tools, logs, URLs, or public source registers.

Risk: Patent, legal, regulatory, safety, clinical, financial, or procurement conclusions could be overread as final decisions.

Mitigation: Keep these conclusions bounded to the reviewed evidence universe and route material patent, legal, regulatory, safety, clinical, financial, and procurement questions to qualified specialists.

Risk: A generated report could contain unsupported findings, unresolved placeholders, local paths, unsafe runtime content, or inconsistent section data.

Mitigation: Run the bundled quality-check script and release checklist, preserve evidence IDs and search logs, reconcile cross-section registers, and withhold release until blocking gates are resolved or documented.

## Reference(s):

- [HTML report skeleton template](references/html_skeleton_template.html)
- [Technology Insight Report Release Review Checklist](references/quality_checklist.md)
- [Section 4 Patent-Landscape Coverage and Claim-Screening Specification](references/s4_exhaustive_search_spec.md)
- [Cross-Section Evidence Synchronization Register](references/sync_table_template.md)
- [PatSnap Patent Search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Patent Briefing MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [HTML report, Markdown registers and checklists, source registers, search logs, and command-line QA output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local project artifacts only for an authorized report engagement; final reports retain evidence IDs, cutoff dates, limitations, review status, and specialist-review boundaries.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
