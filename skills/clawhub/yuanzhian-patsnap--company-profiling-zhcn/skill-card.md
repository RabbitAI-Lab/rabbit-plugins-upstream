## Description:

Analyzes pharmaceutical companies using PatSnap life-science data to produce Chinese company profiles covering company background, financing, pipelines, patents, deals, and investment or partnership considerations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, business development teams, life-science strategists, and developers use this skill to profile pharmaceutical companies in Chinese. It supports company overview, financing history, R&D pipeline, patent layout, drug transactions, and cooperation analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company, drug, target, patent, clinical, and deal queries may be sent to PatSnap MCP, and web search may be used when PatSnap data is insufficient or recent updates are requested.

Mitigation: Avoid submitting confidential company or deal information unless external PatSnap MCP and web-search queries are acceptable for the use case.

Risk: The skill depends on a valid PatSnap API key and a connected Pharma Intelligence MCP service.

Mitigation: Verify MCP connectivity before use and stop with setup guidance if the required service is unavailable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yuanzhian-patsnap/skills/company-profiling-zhcn)
- [PatSnap Open Platform](https://open.patsnap.com)
- [PatSnap Pharma Intelligence MCP service](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [PatSnap Life Sciences](https://eureka.patsnap.com/ls-landing)
- [PatSnap developer documentation](https://open.patsnap.com/devportal)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown report with structured sections, citations or source IDs, tables where useful, and setup commands when MCP configuration is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a PatSnap API key and connected Pharma Intelligence MCP service; web search may be used only as a fallback when PatSnap data is insufficient or recent updates are requested.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
