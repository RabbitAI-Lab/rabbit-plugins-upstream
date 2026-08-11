## Description:

Checks HIPAA privacy, security, and breach-notification readiness across 12 core items, with free preview and optional cloud scoring through compliancehub.cn.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

Compliance teams, developers, and health data operators use this skill to preview HIPAA checklist items, collect yes/no/not-applicable responses, and generate text, JSON, or HTML reports for internal readiness review. It is a compliance guidance aid and not legal advice.

### Deployment Geography for Use:

Global, for organizations assessing U.S. HIPAA obligations.

## Known Risks and Mitigations:

Risk: Scored runs transmit HIPAA compliance checklist answers and an API key to compliancehub.cn.

Mitigation: Use preview mode first when answers should not leave the machine; run scored mode only when comfortable with the disclosed destination, and enter only yes/no/not-applicable compliance responses rather than detailed PHI.

Risk: The API key used for scored runs must be supplied by environment variable or local key file.

Mitigation: Prefer COMPLIANCEHUB_API_KEY for temporary use, or store the key only in ~/.config/compliancehub with 0600 permissions and rotate it if exposed.

Risk: The generated report is compliance guidance, not legal advice.

Mitigation: Use the report as an internal readiness aid and have qualified counsel review decisions that affect HIPAA obligations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/hipaa-check)
- [Publisher profile](https://clawhub.ai/user/wwumit)
- [ComplianceHub account and API key page](https://compliancehub.cn/account.html?skill=hipaa-check)
- [ComplianceHub cloud endpoint](https://compliancehub.cn)

## Skill Output:

**Output Type(s):** [text, JSON, HTML, shell commands, configuration, guidance]

**Output Format:** [CLI output, JSON, or HTML report; agent guidance may include shell commands for preview, API key setup, and report generation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preview mode sends no answers; scored runs send checklist answers and the API key to compliancehub.cn.]

## Skill Version(s):

1.1.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
