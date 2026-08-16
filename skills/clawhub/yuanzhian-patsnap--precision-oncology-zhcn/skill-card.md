## Description:

Provides Chinese-language precision oncology reports by combining literature, epidemiology, clinical and drug guidance, clinical trial evidence, molecular biology, and histology analysis for cancer-related questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users and life-science research or business-development teams use this skill to generate Chinese-language oncology research reports covering cancer mechanisms, epidemiology, standards of care, clinical development, and commercial feasibility. The skill is intended for research and reporting workflows, not direct patient-specific medical decision making.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a PatSnap life-science MCP service and a PatSnap API key.

Mitigation: Install it only for workflows that intentionally use PatSnap data services, store the API key through the agent's MCP configuration, and verify the MCP connection before use.

Risk: Oncology outputs could be misapplied to patient-specific medical decisions.

Mitigation: Use the skill for research and business-development reporting, and verify patient-specific conclusions with qualified clinical sources.

Risk: External data retrieval may be incomplete or unavailable if the required MCP service is not connected.

Mitigation: Run the documented connectivity check before analysis and stop rather than continuing with unsupported conclusions when the service is unavailable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/precision-oncology-zhcn)
- [PatSnap Open Platform](https://open.patsnap.com)
- [PatSnap Pharma Intelligence MCP Server](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [PatSnap Life Sciences](https://eureka.patsnap.com/ls-landing)
- [PatSnap Developer Documentation](https://open.patsnap.com/devportal)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Chinese-language Markdown reports with setup commands and structured oncology analysis sections.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a connected PatSnap life-science MCP service for data retrieval; reports should be clinically verified before patient-specific use.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
