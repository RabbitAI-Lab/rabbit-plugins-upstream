## Description:

Assesses hydroponic nutrient concentration qualitatively from root and leaf images or video, then provides adjustment guidance and structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Hydroponic growers use the skill to review root and leaf images for visible signs of nutrient stress and receive qualitative guidance on whether to dilute or replenish the solution. It also provides structured analysis reports and links to cloud-stored history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup-only option may still run cloud analysis.

Mitigation: Treat setup mode as potentially online; check which action will run and use only images approved for cloud processing.

Risk: Authenticated requests need safeguards on which service addresses they can reach.

Mitigation: Restrict authenticated requests to approved service addresses.

Risk: Automatic account creation and token handling lack safeguards, and report retention is not explained.

Mitigation: Review account creation and token storage before installation, keep credentials out of shared workspaces, and clarify report retention.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-hydroponic-nutrient-assessment-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured qualitative analysis report with observations, adjustment guidance, and report links; history is presented as a Markdown table.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual assessment is qualitative and does not provide EC or ppm values.]

## Skill Version(s):

1.0.12 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
