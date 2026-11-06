## Description:

Analyzes plant images and videos to classify growth stages and produce structured reports for agricultural decision support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Agricultural practitioners can use plant photos or videos to identify a plant's growth stage, review developmental observations, and consult structured analysis when planning crop management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends plant images or videos to LifeEmergence for analysis, including when its no-analysis option is used.

Mitigation: Submit only media you are authorized and comfortable sending to LifeEmergence; do not rely on the no-analysis option to prevent uploads.

Risk: Automatic account handling retains sign-in credentials and may incur charges.

Mitigation: Review the account creation and credential handling behavior before use, protect stored credentials and profile data, and check for possible charges.

Risk: The package does not substantiate its immediate cloud-deletion promise, and its service-address option may be ignored.

Mitigation: Treat uploaded media as potentially retained, and do not use --api-url as a means to redirect sensitive uploads.

## Reference(s):

- [API reference](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Recommendations, Report links]

**Output Format:** [Structured analysis results, with history reports presented as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include growth-stage classification, developmental observations, recommendations, and links. Analysis is for agricultural reference.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
