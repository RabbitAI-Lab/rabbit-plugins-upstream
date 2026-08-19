## Description:

Conduct comprehensive disease investigation combining academic literature, epidemiological data, clinical guidelines, pharmaceutical intelligence, and clinical trial reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Life sciences R&D and business development users use this skill to investigate disease mechanisms, epidemiology, symptoms, standards of care, drug pipelines, patent landscapes, and commercial opportunities. The skill is intended to support research and strategy reports, not to provide medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Disease, patent, drug, and business-development queries are sent to a user-configured PatSnap MCP service.

Mitigation: Install and use the skill only when the user trusts PatSnap for those query contents.

Risk: The setup flow places an API key in the MCP connection URL.

Mitigation: Protect the API key, avoid sharing configured connection strings, and rotate the key if it is exposed.

Risk: Disease investigation outputs may influence research, business, or clinical-adjacent decisions.

Mitigation: Treat outputs as research support, verify important claims against source evidence, and do not use the skill as medical advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/disease-investigation)
- [PatSnap Pharma Intelligence MCP Server](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [PatSnap Chemical Molecular MCP Server](https://open.patsnap.com/marketplace/mcp-servers/713886)
- [PatSnap Biology Modality MCP Server](https://open.patsnap.com/marketplace/mcp-servers/06e741)
- [PatSnap Life Science](https://eureka.patsnap.com/ls-landing)
- [PatSnap Dev Portal](https://open.patsnap.com/devportal)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands, configuration]

**Output Format:** [Markdown research reports with numbered sections, supporting evidence, and setup guidance when required services are not connected]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include a conclusion and cite retrieved evidence identifiers where available.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
