## Description:

Runs a bilingual HIPAA compliance checklist covering 12 core Privacy, Security, and Breach Notification Rule items and produces a scored report via the CQDev cloud compliance engine.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

Compliance teams, developers, and agents use this skill when a user requests a HIPAA medical privacy compliance check, previewing the 12 items and running a scored assessment that returns text, JSON, or HTML reports. It provides general compliance guidance and is not legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scored checks send checklist answers to compliancehub.cn.

Mitigation: Confirm the destination before running a scored check and avoid entering patient-identifying details in free-text contexts.

Risk: An API key or anonymous trial ID may be stored locally for continued use.

Mitigation: Use only the documented COMPLIANCEHUB_API_KEY environment variable or 0600 key file, and remove local credentials when they are no longer needed.

## Reference(s):

- [HIPAA Check ClawHub listing](https://clawhub.ai/wwumit/skills/hipaa-check)
- [ComplianceHub service](https://compliancehub.cn)
- [ComplianceHub account and API key page](https://compliancehub.cn/account.html?skill=hipaa-check)

## Skill Output:

**Output Type(s):** [text, JSON, files, shell commands, guidance]

**Output Format:** [Plain text, JSON, or HTML report; Markdown guidance with inline bash commands in the skill documentation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include a compliance score, pass/fail counts, item status, legal authority, and recommendations; an optional output path saves the report to a file.]

## Skill Version(s):

1.1.3 (source: evidence.release.version and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
