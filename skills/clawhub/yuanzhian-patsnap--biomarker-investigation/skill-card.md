## Description:

Searches academic and patent literature for biomarkers, including disease associations, biomarker availability, related techniques, patents, and clinical trial evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers and life-science R&D teams use this skill to investigate biomarkers for diseases, therapies, or biological indicators with PatSnap LifeScience MCP services. It supports biomarker landscape, patent, literature, clinical trial, drug, target, company, and related evidence reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup requires a PatSnap API key in MCP configuration.

Mitigation: Use a scoped PatSnap API key where available, keep it out of shared logs or screenshots, and rotate it if exposed.

Risk: Biomarker queries and retrieved context may be sent to PatSnap LifeScience MCP services.

Mitigation: Use the skill only for data that is permitted under the organization's PatSnap account, data handling rules, and confidentiality requirements.

Risk: Patent and clinical evidence can be misread if the agent relies on search-result summaries alone.

Mitigation: Require search-to-fetch retrieval before conclusions and have qualified reviewers check patent-risk or clinical interpretations before decision-making.

## Reference(s):

- [Biomarker Investigation skill page](https://clawhub.ai/yuanzhian-patsnap/skills/biomarker-investigation)
- [PatSnap Life Science](https://eureka.patsnap.com/ls-landing)
- [PatSnap Dev Portal](https://open.patsnap.com/devportal)
- [PatSnap Open Platform](https://open.patsnap.com)
- [Pharma Intelligence MCP server](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [Chemical Molecular MCP server](https://open.patsnap.com/marketplace/mcp-servers/713886)
- [Biology Modality MCP server](https://open.patsnap.com/marketplace/mcp-servers/06e741)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with numbered sections, citation summaries, and occasional inline shell command examples for setup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires connected PatSnap LifeScience MCP services before retrieval; outputs should be based on fetched details rather than search-result summaries.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
