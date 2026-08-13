## Description:

Guides an agent to use PatSnap LifeScience MCP services and optional web search to produce structured precision oncology reports on cancer biology, epidemiology, treatments, clinical trials, patents, and commercial viability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Pharmaceutical R&D and business development teams use this skill to investigate cancers or tumors, including carcinogenesis, epidemiology, standards of care, clinical trials, patents, drug pipelines, unmet needs, and market dynamics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Oncology queries may contain personal health information or other sensitive medical details.

Mitigation: Do not include personal health information unless the user understands and accepts that queries may be sent to PatSnap and, when web fallback is used, to search providers.

Risk: The skill requires a PatSnap API key for MCP connectivity.

Mitigation: Store and rotate the API key carefully, and avoid placing real keys in shared files, transcripts, or examples.

Risk: Web fallback can expose query text to search providers.

Mitigation: Use web search only after PatSnap database retrieval is complete and keep search queries concise without sensitive patient details.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/precision-oncology)
- [PatSnap Life Science](https://eureka.patsnap.com/ls-landing)
- [PatSnap Dev Portal](https://open.patsnap.com/devportal)
- [PatSnap Open Platform](https://open.patsnap.com)
- [PatSnap Pharma Intelligence MCP Service](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [PatSnap Chemical Molecular MCP Service](https://open.patsnap.com/marketplace/mcp-servers/713886)
- [PatSnap Biology Modality MCP Service](https://open.patsnap.com/marketplace/mcp-servers/06e741)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with numbered sections and optional bash commands for MCP setup]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PatSnap LifeScience MCP connectivity before analysis; web search is used only after MCP retrieval is complete and results are insufficient or current information is requested.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
