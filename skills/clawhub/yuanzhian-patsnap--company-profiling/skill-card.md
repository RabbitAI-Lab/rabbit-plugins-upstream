## Description:

Extracts and analyzes pharmaceutical company intelligence to produce company profiles and investment or collaboration recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users and life-science analysts use this skill to profile pharmaceutical companies, including company overviews, financing history, R&D pipelines, patent activity, and drug deals. The skill is intended to retrieve evidence from PatSnap LifeScience MCP services and turn it into concise, structured research reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys and research queries are sent to PatSnap's external LifeScience MCP services.

Mitigation: Use an appropriate PatSnap account, avoid sensitive research queries unless permitted, and review PatSnap access and logging terms before deployment.

Risk: The skill's reports may inform investment or collaboration decisions from external pharmaceutical data.

Mitigation: Review generated reports and the cited PatSnap records before relying on conclusions for business decisions.

Risk: The skill depends on PatSnap MCP connectivity and cannot complete its intended workflow if the service or credentials are unavailable.

Mitigation: Verify MCP connectivity and credential configuration before use, and stop rather than retrying unrelated tools when connection checks fail.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/company-profiling)
- [PatSnap Life Science](https://eureka.patsnap.com/ls-landing)
- [PatSnap Developer Portal](https://open.patsnap.com/devportal)
- [PatSnap Pharma Intelligence MCP Server](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [PatSnap Chemical Molecular MCP Server](https://open.patsnap.com/marketplace/mcp-servers/713886)
- [PatSnap Biology Modality MCP Server](https://open.patsnap.com/marketplace/mcp-servers/06e741)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with tables and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PatSnap LifeScience MCP connectivity and an API key; reports are expected to include an Abstract, Roman-numeral sections, and a Conclusion.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter metadata states 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
