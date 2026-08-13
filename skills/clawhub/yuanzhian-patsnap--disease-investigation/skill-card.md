## Description:

Conducts disease investigation by combining academic literature, epidemiological data, clinical guidelines, pharmaceutical intelligence, and clinical trial reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Life sciences R&D and business development teams use this skill to investigate disease pathology, epidemiology, treatments, drug pipelines, patent landscapes, and commercial opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Relevant disease research queries are sent to PatSnap's remote MCP service using the user's API key.

Mitigation: Use a limited, revocable PatSnap API key and avoid sending confidential patient, business, or proprietary data unless the organization permits it.

Risk: MCP setup commands include an API key in the service URL.

Mitigation: Keep connection commands and MCP configuration private, rotate keys if exposed, and prefer keys with the narrowest practical access.

Risk: Disease, treatment, pipeline, patent, or commercial conclusions may be misleading if retrieved evidence is incomplete or stale.

Mitigation: Follow the skill's retrieve-then-fetch workflow, cite retrieved evidence, state insufficiency clearly, and require qualified review before clinical or investment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/disease-investigation)
- [PatSnap Life Science](https://eureka.patsnap.com/ls-landing)
- [PatSnap Dev Portal](https://open.patsnap.com/devportal)
- [PatSnap Pharma Intelligence MCP server](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [PatSnap Chemical Molecular MCP server](https://open.patsnap.com/marketplace/mcp-servers/713886)
- [PatSnap Biology Modality MCP server](https://open.patsnap.com/marketplace/mcp-servers/06e741)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with numbered sections and inline bash setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a connected PatSnap LifeScience MCP service; web search is used only after MCP retrieval when additional coverage or recency is needed.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter reports 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
