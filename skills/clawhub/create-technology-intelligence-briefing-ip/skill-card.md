## Description:

Creates auditable technology-intelligence briefings for named companies and/or technical topics using patent, scientific-literature, and current-news evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, patent researchers, and developers use this skill to produce evidence-backed technology briefings for companies or technical topics. It supports patent-and-literature scans, company comparisons, subtechnology mapping, current-news review, and reproducible research traces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled report builder loads a v2_data.py file as executable Python before rendering.

Mitigation: Review any v2_data.py file before generation, avoid storing secrets in it, and run the renderer only in an approved working directory.

Risk: Technology briefings can mislead readers if patent, literature, or news evidence is incomplete, unverifiable, or presented without limitations.

Mitigation: Keep section status, retrieval dates, source locators, scope assumptions, and limitations visible in the HTML report and Markdown trace.

## Reference(s):

- [Advanced Patent Search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [Patent Briefing MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [Deep Patent Mining MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-mining)
- [Request parsing rules](references/parse_rules.md)
- [Technology keyword expansion](references/keyword_expansion.md)
- [Technology intelligence briefing research trace](references/trace_template.md)
- [Company aliases](references/company_aliases.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python data configuration and generated static HTML plus Markdown trace deliverables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires reviewed evidence inputs and a controlled working directory before report generation.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
