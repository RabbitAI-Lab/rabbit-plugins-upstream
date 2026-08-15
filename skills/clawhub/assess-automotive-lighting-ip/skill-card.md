## Description:

Assess automotive-lighting component architecture, sourcing strategy, and preliminary patent and design-right risk for lamp drawings, product images, bills of materials, technical concepts, and make-versus-buy questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Automotive lighting engineers, sourcing teams, product teams, and IP reviewers use this skill to decompose lamp architectures, compare make-buy-hybrid sourcing options, and run preliminary multi-jurisdiction patent and design-risk screening. It is intended to produce evidence-backed recommendations and an accessible report while routing legal conclusions to qualified counsel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Preliminary IP screening could be mistaken for legal clearance or an infringement opinion.

Mitigation: Keep outputs labeled as preliminary, avoid launch-clearance conclusions, and route final claim construction, infringement, validity, enforceability, and clearance decisions to qualified counsel in each relevant jurisdiction.

Risk: Configured patent-research services may be needed for live FTO and design-risk execution.

Mitigation: Use the official PatSnap MCP server connection pages, keep API keys out of reports, source control, and logs, and mark searches as not executed when the required service is unavailable.

Risk: Generated local HTML and ZIP reports may contain sensitive product, sourcing, or IP information supplied by the user.

Mitigation: Review generated report files before sharing, confirm output paths, and remove secrets or temporary artifacts from archives.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/assess-automotive-lighting-ip)
- [Patsnap Patent Research MCP server](https://open.patsnap.com/marketplace/mcp-servers/patsnap-ip-searching)
- [Patent Briefing MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [Advanced Patent Search MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-search)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with generated accessible HTML report files, optionally packaged as a ZIP archive]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports exact output paths when files are created; distinguishes user facts, retrieved evidence, assumptions, and analyst inferences.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
