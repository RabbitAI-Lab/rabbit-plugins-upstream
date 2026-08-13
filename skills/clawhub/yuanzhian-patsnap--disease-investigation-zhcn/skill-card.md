## Description:

Disease Investigation Zhcn helps agents conduct disease research across academic literature, epidemiology, clinical guidelines, drug intelligence, clinical-trial reports, patent landscape, and business-development questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users and life-science teams use this skill to structure Chinese-language disease investigations across mechanisms, epidemiology, standards of care, R&D pipelines, patents, and commercial opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries are sent to PatSnap MCP services.

Mitigation: Review confidentiality and data-sharing requirements before using the skill with sensitive research questions.

Risk: The PatSnap API key is configured in the MCP connection URL.

Mitigation: Handle the connection URL as a secret, avoid sharing logs or screenshots that expose it, and rotate the key if it is disclosed.

Risk: Biomedical research output could be mistaken for professional medical advice.

Mitigation: Use the skill for research assistance only and require qualified clinical or regulatory review before applying findings to medical decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/disease-investigation-zhcn)
- [PatSnap Open Platform](https://open.patsnap.com)
- [PatSnap Pharma Intelligence MCP](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [PatSnap Chemical Molecular MCP](https://open.patsnap.com/marketplace/mcp-servers/713886)
- [PatSnap Biology Modality MCP](https://open.patsnap.com/marketplace/mcp-servers/06e741)
- [PatSnap Life Science](https://eureka.patsnap.com/ls-landing)
- [PatSnap Developer Portal](https://open.patsnap.com/devportal)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with cited identifiers and inline shell commands or configuration guidance when MCP setup is required]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language disease research workflow that depends on PatSnap Life Science MCP services.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
