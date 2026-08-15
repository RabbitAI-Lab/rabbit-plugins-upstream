## Description:

Researches key technical dimensions from a product-feature description, searches relevant patents, and generates an HTML report with product context and patent relevance scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and patent analysts use this skill to turn a product-feature description into a structured patent landscape report with technical-dimension mapping, relevance scoring, and filtering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product-feature text may contain sensitive business information that is sent through web search or the configured patent MCP service.

Mitigation: Review the input before use and avoid sending confidential product details unless the connected services are approved for that data.

Risk: The generated HTML report may contain sensitive business information or patent-analysis conclusions.

Mitigation: Review the local session report before sharing it outside the intended audience.

## Reference(s):

- [PatSnap Open Platform](https://open.zhihuiya.com/)
- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/product-feature-patent-finder)

## Skill Output:

**Output Type(s):** [text, code, configuration, guidance]

**Output Format:** [Self-contained HTML report with embedded CSS and JavaScript]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a local session report that includes product research, patent records, relevance scores, technical-dimension tags, source links, and interactive filtering.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
