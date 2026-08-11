## Description:

Runs a GDPR compliance audit covering 25 core GDPR items, with preview mode available locally and scored reports produced through the CQDev cloud compliance engine.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

External users, compliance teams, and agents use this skill to preview GDPR audit questions or collect answers for a scored GDPR compliance report. It is intended for general compliance guidance, not legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scored audits send item answers and the API key to compliancehub.cn for scoring.

Mitigation: Use preview mode first when answers should remain local, and run scored audits only after confirming the cloud destination.

Risk: The ComplianceHub API key can be exposed if stored or shared carelessly.

Mitigation: Prefer COMPLIANCEHUB_API_KEY for temporary use, or restrict permissions on ~/.config/compliancehub/gdpr-audit.key when using the key file.

Risk: Audit output may be mistaken for legal advice.

Mitigation: Treat the report as general compliance guidance and consult qualified counsel for legal conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/gdpr-audit)
- [Publisher profile](https://clawhub.ai/user/wwumit)
- [ComplianceHub account center](https://compliancehub.cn/account.html?skill=gdpr-audit)
- [ComplianceHub cloud endpoint](https://compliancehub.cn)

## Skill Output:

**Output Type(s):** [text, JSON, HTML, shell commands, configuration, guidance]

**Output Format:** [Text, JSON, or HTML audit preview and report output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write a report file with --output; scored runs send item answers and a Bearer API key to compliancehub.cn.]

## Skill Version(s):

2.0.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
