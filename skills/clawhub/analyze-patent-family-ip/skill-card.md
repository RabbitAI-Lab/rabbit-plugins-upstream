## Description:

Analyze a patent family from a patent identifier or PatSnap patent URL by defining the family scope, reconstructing priority and procedural relationships, comparing technical disclosures and claim focus, mapping themes, and generating a source-traceable offline HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts, IP counsel, portfolio teams, R&D teams, competitive-intelligence teams, and due-diligence reviewers use this skill to map patent-family structure, compare member disclosures and claims, and produce an evidence-labelled offline HTML report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow retrieves patent records through PatSnap MCP connectors.

Mitigation: Confirm the required PatSnap connectors are approved for the workspace and appropriate for the patent records being analyzed before use.

Risk: The renderer writes a local HTML report to a user-selected path.

Mitigation: Review the output path before running the renderer, especially when working in sensitive or shared workspace locations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/analyze-patent-family-ip)
- [PatSnap Patent Briefing MCP marketplace page](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [PatSnap Advanced Patent Search MCP marketplace page](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Global Core Patent Database MCP marketplace page](https://open.patsnap.com/marketplace/mcp-servers/core-patents)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance plus normalized JSON input and a self-contained offline HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The local renderer validates normalized JSON, escapes untrusted text, allowlists HTTP(S) links, and writes only the requested HTML report.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
