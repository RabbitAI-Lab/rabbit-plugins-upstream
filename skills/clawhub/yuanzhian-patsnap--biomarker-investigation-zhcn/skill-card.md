## Description:

根据查询搜索与生物标志物相关的学术和专利文献。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Life-science researchers and pharmaceutical R&D teams use this skill to investigate disease or treatment-related biomarkers across literature, patents, clinical trials, drugs, targets, companies, and related life-science data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects an agent to PatSnap's external MCP service using an API key.

Mitigation: Install only when the operator is comfortable authorizing PatSnap MCP access, and verify the service connection before running research queries.

Risk: Medical, clinical, and patent-risk conclusions may be incomplete or unsuitable as final professional advice.

Mitigation: Treat outputs as research support and check important conclusions against authoritative sources and qualified experts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/biomarker-investigation-zhcn)
- [PatSnap Pharma Intelligence MCP Server](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [PatSnap Chemical Molecular MCP Server](https://open.patsnap.com/marketplace/mcp-servers/713886)
- [PatSnap Biology Modality MCP Server](https://open.patsnap.com/marketplace/mcp-servers/06e741)
- [PatSnap Life Sciences](https://eureka.patsnap.com/ls-landing)
- [PatSnap Developer Documentation](https://open.patsnap.com/devportal)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, analysis, markdown]

**Output Format:** [Markdown research reports with cited evidence summaries and inline setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are structured with Roman-numeral sections and a required conclusion; web search is reserved for cases where MCP results are insufficient or freshness is required.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
