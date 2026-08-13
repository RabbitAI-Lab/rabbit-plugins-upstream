## Description:

CCPA Check is a CCPA/CPRA compliance self-check that asks 12 California privacy compliance questions and uses the CQDev cloud compliance engine to score responses and produce a local report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and compliance teams use this skill to preview CCPA/CPRA checklist items offline, run a cloud-scored California privacy compliance assessment, and generate text, JSON, or HTML reports for review. The output is general compliance guidance and is not legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scored assessments transmit CCPA/CPRA checklist answers and either an API key or anonymous trial ID to compliancehub.cn for cloud scoring.

Mitigation: Confirm the user is comfortable with cloud processing before a scored run, avoid entering confidential narrative evidence, and use the non-interactive preview for an offline view of checklist items.

Risk: The generated report is compliance guidance, not a formal legal opinion.

Mitigation: Treat results as a self-check and review important conclusions with qualified counsel before relying on them for legal or regulatory decisions.

## Reference(s):

- [CCPA Check ClawHub Page](https://clawhub.ai/wwumit/skills/ccpa-check)
- [API Key Setup](references/api_key.md)
- [ComplianceHub Cloud Service](https://compliancehub.cn)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files, Shell commands, Configuration]

**Output Format:** [Interactive terminal prompts with text, JSON, or HTML report output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scored runs send checklist answers and either an API key or anonymous trial ID to compliancehub.cn; non-interactive preview mode uses bundled checklist items offline.]

## Skill Version(s):

2.2.4 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
