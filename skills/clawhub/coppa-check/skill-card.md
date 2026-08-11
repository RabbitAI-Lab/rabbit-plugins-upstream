## Description:

COPPA Check guides agents through a 12-item Children's Online Privacy Protection Act compliance check and can generate text, JSON, or HTML reports with compliancehub.cn cloud scoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT

## Use Case:

Developers, compliance reviewers, and product teams use this skill to preview COPPA check items, collect compliance responses, and produce a scored report for products that may involve children under 13. The report is guidance for review and is not legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scored reports send checklist answers and the API key to compliancehub.cn.

Mitigation: Use the skill only when that cloud scoring flow is acceptable, confirm the destination is compliancehub.cn, and avoid submitting sensitive details beyond the checklist responses.

Risk: Preview mode may still contact the provider even though the skill text describes it as offline.

Mitigation: Treat preview runs as potentially networked until the behavior is fixed or confirmed acceptable, and run the skill only with network access you intend to allow.

Risk: The generated COPPA report may be mistaken for legal advice.

Mitigation: Use the report as general compliance guidance and have qualified counsel review legal conclusions before relying on them.

## Reference(s):

- [COPPA Check ClawHub listing](https://clawhub.ai/wwumit/skills/coppa-check)
- [ComplianceHub account and API key page](https://compliancehub.cn/account.html?skill=coppa-check)
- [ComplianceHub service endpoint](https://compliancehub.cn)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Analysis, Files]

**Output Format:** [Markdown guidance plus generated text, JSON, or HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scored checks submit checklist answers and an API key to compliancehub.cn; reports may be printed to stdout or written to a user-specified file.]

## Skill Version(s):

1.1.0 (source: package.json and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
