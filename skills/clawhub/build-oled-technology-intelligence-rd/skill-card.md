## Description:

Build a source-traceable, multi-page technology-intelligence HTML portal for OLED or another defined technology domain.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, R&D teams, strategy teams, competitive-intelligence teams, and IP teams use this skill to build reviewed technology-watch portals that organize company, technical-route, event, publication, and patent evidence while showing coverage and uncertainty.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run a bundled Python renderer and write portal files to a user-selected output directory.

Mitigation: Run it in a controlled workspace, review the output path before execution, and inspect generated files before sharing.

Risk: Technology-intelligence summaries can become misleading if supplied records are incomplete, stale, duplicated, or insufficiently reviewed.

Mitigation: Use reviewed source records, preserve evidence IDs and cutoff dates, disclose limitations, and keep rejected-record reasons visible.

Risk: Optional research or patent tools may be used when the requested scope requires current evidence.

Mitigation: Confirm tool availability and scope before research, retain search logs, and treat patent evidence as informational rather than legal, investment, or commercial advice.

## Reference(s):

- [Organization Mapping and OLED Seed Universe](references/company-mapping.md)
- [Technology Taxonomy and OLED Seed Tags](references/tech-tags.md)
- [Portal Data Processing and Validation](references/data-processing.md)
- [Portal HTML Structure and Scientific Editorial Design](references/html-templates.md)
- [PatSnap Patent Search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Patent Briefing MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/build-oled-technology-intelligence-rd)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated local HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a self-contained multi-page HTML portal from reviewed UTF-8 JSON evidence.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
