## Description:

COPPA Check helps agents run a Children's Online Privacy Protection Act compliance check covering 12 core items, with local preview and optional cloud scoring through compliancehub.cn.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT

## Use Case:

Developers, product teams, and compliance reviewers use this skill to preview and run a COPPA-oriented checklist for products that may involve children under 13. It produces a reference report for internal compliance review and does not replace legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scored checks send the user's compliance answers to compliancehub.cn.

Mitigation: Tell users before scored runs, confirm the destination is compliancehub.cn, and use preview mode when cloud scoring is not acceptable.

Risk: The optional login flow accepts account credentials and stores an API key locally.

Mitigation: Prefer the account page or COMPLIANCEHUB_API_KEY when users do not want to type a password in the CLI, and treat the saved key as a local credential.

Risk: The generated COPPA report could be mistaken for legal advice.

Mitigation: Present reports as general compliance guidance and direct users to qualified counsel for legal decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/coppa-check)
- [ComplianceHub account page for COPPA Check](https://compliancehub.cn/account.html?skill=coppa-check)
- [ComplianceHub cloud endpoint](https://compliancehub.cn)

## Skill Output:

**Output Type(s):** [text, json, shell commands, files, guidance]

**Output Format:** [CLI text, JSON preview, or HTML/text/json report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scored reports use compliancehub.cn and require COMPLIANCEHUB_API_KEY or a locally saved API key; preview mode can run without a key.]

## Skill Version(s):

1.0.4 (source: package.json, _meta.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
