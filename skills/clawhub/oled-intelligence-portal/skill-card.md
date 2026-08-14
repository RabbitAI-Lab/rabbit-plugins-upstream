## Description:

Generates a multi-page Chinese HTML intelligence portal for a technology keyword by identifying companies and technology branches, retrieving Patsnap news and patent results, and rendering local report pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to generate browser-ready intelligence portals for technology domains, combining company monitoring, technology branch tracking, news summaries, and patent summaries into local HTML pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated portal content can reflect incomplete, stale, or misleading search results from Patsnap-backed news and patent retrieval.

Mitigation: Review the generated portal data and source links before relying on it for business, technical, patent, or investment decisions.

Risk: Untrusted raw HTML or unusual path-like keywords and slugs may affect generated report pages or output paths.

Mitigation: Use trusted keywords and normalized slugs, avoid passing raw HTML, and inspect generated HTML before sharing or publishing the portal.

Risk: The skill depends on Patsnap MCP-backed searches and local HTML generation, so missing authorization or disabled MCP tools will limit results.

Mitigation: Install and use the skill only in an environment with the intended Patsnap MCP services enabled and authorized.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/oled-intelligence-portal)
- [Patsnap Open Platform](https://open.zhihuiya.com/)
- [HTML templates reference](artifact/references/html-templates.md)
- [Company mapping reference](artifact/references/company-mapping.md)
- [Technology tags reference](artifact/references/tech-tags.md)
- [Data processing reference](artifact/references/data-processing.md)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration]

**Output Format:** [Text instructions plus generated HTML files and a machine-readable JSON summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a local portal directory with index.html, company pages, technology pages, and patents.html when required Patsnap MCP services and input data are available.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
