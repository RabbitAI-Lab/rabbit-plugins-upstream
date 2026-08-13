## Description:

Helps agents investigate biomarkers by searching PatSnap life-science data across academic literature, patents, clinical trials, drug, target, and company records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Pharmaceutical R&D and life-science research users use this skill to investigate disease-related biomarkers, supporting literature review, patent review, clinical-trial research, and cross-domain biomarker analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may expose a PatSnap API key while configuring MCP services.

Mitigation: Use a limited-scope PatSnap API key where possible and avoid pasting real keys into shared terminals, screenshots, or logs.

Risk: Patent-infringement conclusions may be mistaken for legal advice.

Mitigation: Treat outputs as research support and have qualified counsel review legal conclusions before relying on them.

Risk: The skill depends on PatSnap LifeScience MCP connectivity and may fail or produce incomplete work if the service is unavailable or unauthenticated.

Mitigation: Verify MCP connectivity before analysis and stop with setup guidance if the required service is not connected.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/biomarker-investigation)
- [PatSnap Life Science](https://eureka.patsnap.com/ls-landing)
- [PatSnap Developer Portal](https://open.patsnap.com/devportal)
- [PatSnap Pharma Intelligence MCP Server](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [PatSnap Chemical Molecular MCP Server](https://open.patsnap.com/marketplace/mcp-servers/713886)
- [PatSnap Biology Modality MCP Server](https://open.patsnap.com/marketplace/mcp-servers/06e741)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with setup commands and structured research sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are expected to include numbered sections, an abstract, citations or identifiers, and a conclusion.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact metadata lists 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
