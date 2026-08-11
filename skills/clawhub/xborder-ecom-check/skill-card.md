## Description:

Cross-Border E-Commerce Compliance Check helps agents review customs, product safety, consumer protection, tax, advertising, and destination-market data privacy requirements for cross-border e-commerce.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT

## Use Case:

External users and compliance teams use this skill to preview a 12-item cross-border e-commerce compliance checklist and, with explicit opt-in and a user-supplied API key, generate scored compliance reports through the CQDev cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scored checks send compliance answers to CQDev's compliancehub.cn cloud service.

Mitigation: Use --non-interactive or --non-interactive-json for local-only preview, and run scored checks only after explicit user opt-in.

Risk: Scored checks require a user-supplied API key.

Mitigation: Provide the key through COMPLIANCEHUB_API_KEY or a 0600 key file, and avoid entering sensitive business details unless cloud scoring is intended.

Risk: The generated compliance report is guidance, not legal advice.

Mitigation: Have qualified counsel review compliance decisions before relying on the report for regulated business activity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/xborder-ecom-check)
- [CQDev ComplianceHub account page](https://compliancehub.cn/account.html?skill=xborder-ecom-check)
- [CQDev ComplianceHub service](https://compliancehub.cn)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Plain text, JSON, or HTML reports with optional local file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline preview uses bundled checklist items; scored runs require COMPLIANCEHUB_API_KEY and may contact compliancehub.cn.]

## Skill Version(s):

1.2.0 (source: server release metadata, package.json, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
