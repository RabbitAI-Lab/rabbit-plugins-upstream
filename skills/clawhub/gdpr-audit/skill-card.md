## Description:

GDPR Audit guides agents through a 25-item GDPR compliance review and can generate scored text, JSON, or HTML reports using the CQDev cloud compliance engine.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

External users, compliance teams, and agents use this skill to preview GDPR checks, collect audit answers, and produce a report for internal review. The output is general compliance guidance and is not legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scored audit runs send checklist answers to compliancehub.cn and use an API key from local storage or the environment.

Mitigation: Use scored runs only when that data sharing is acceptable; otherwise use preview mode with network access blocked.

Risk: The optional login flow sends account credentials to compliancehub.cn and stores a service API key under ~/.config/compliancehub.

Mitigation: Run login only intentionally, protect or remove the stored key when no longer needed, or provide COMPLIANCEHUB_API_KEY for session-scoped use.

Risk: Preview mode may fetch the cloud rule library before displaying items, so it should not be treated as strictly offline by default.

Mitigation: Block network access when an offline preview is required.

Risk: The generated report is general compliance guidance, not legal advice.

Mitigation: Have qualified counsel review decisions before relying on the audit output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/gdpr-audit)
- [ComplianceHub account page](https://compliancehub.cn/account.html?skill=gdpr-audit)

## Skill Output:

**Output Type(s):** [text, JSON, HTML, files, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands; audit reports in text, JSON, or HTML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may be printed to stdout or written to a user-selected output file.]

## Skill Version(s):

1.0.6 (source: server release evidence, package.json, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
