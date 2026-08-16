## Description:

GDPR Check runs a bilingual 12-item GDPR compliance checklist and can generate text, JSON, or HTML reports using the CQDev cloud scoring service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

Compliance, privacy, and engineering teams use this skill to preview GDPR checklist items, collect pass/fail/not-applicable answers, and generate a local compliance report. It is useful for structured self-assessment, but the generated guidance is not legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scored checks send checklist answers to compliancehub.cn for cloud scoring.

Mitigation: Use --non-interactive to preview items without sending answers, and run scored checks only after confirming the destination and data-sharing posture.

Risk: API keys and generated reports may contain sensitive compliance context if handled carelessly.

Mitigation: Provide the API key only through COMPLIANCEHUB_API_KEY or the documented key file, and review any report output path before using -o.

## Reference(s):

- [ClawHub GDPR Check skill page](https://clawhub.ai/wwumit/skills/gdpr-check)
- [Publisher profile: wwumit](https://clawhub.ai/user/wwumit)
- [ComplianceHub account and API key page](https://compliancehub.cn/account.html?skill=gdpr-check)
- [ComplianceHub service endpoint](https://compliancehub.cn)

## Skill Output:

**Output Type(s):** [Text, JSON, HTML, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Terminal text, JSON preview, JSON report, or HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may be printed to stdout or written to a user-selected output path.]

## Skill Version(s):

1.1.3 (source: server release evidence and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
