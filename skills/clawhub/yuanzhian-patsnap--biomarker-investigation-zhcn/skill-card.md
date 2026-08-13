## Description:

Searches academic and patent literature for biomarkers, disease-related biomarker availability, and biomarker-related technologies or patents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users and life-science R&D teams use this skill to investigate disease biomarkers, retrieve patent, literature, clinical, drug, target, and organization evidence through PatSnap services, and produce structured Chinese research reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on PatSnap remote MCP services and uses a PatSnap API key.

Mitigation: Install only when PatSnap MCP access is intended, configure the API key through PatSnap guidance, and verify MCP connectivity before research use.

Risk: Patent infringement or patent barrier discussion may be mistaken for a legal conclusion.

Mitigation: Treat patent-risk output as research support and obtain qualified legal review before making legal or commercial decisions.

Risk: The skill may supplement PatSnap database results with web search when database results are insufficient or current updates are requested.

Mitigation: Review cited external sources for reliability, recency, and relevance before relying on the report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/biomarker-investigation-zhcn)
- [Publisher profile](https://clawhub.ai/user/yuanzhian-patsnap)
- [PatSnap Open Platform](https://open.patsnap.com)
- [PatSnap Pharma Intelligence MCP](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [PatSnap Life Science](https://eureka.patsnap.com/ls-landing)
- [PatSnap Developer Documentation](https://open.patsnap.com/devportal)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown report with inline citations and setup commands when MCP is not connected]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PatSnap Life Science MCP connectivity; may supplement MCP results with web search only after MCP retrieval is insufficient or current information is requested.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
