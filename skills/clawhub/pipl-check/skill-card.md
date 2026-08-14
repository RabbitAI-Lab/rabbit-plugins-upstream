## Description:

PIPL Check helps users run a Chinese Personal Information Protection Law compliance self-check across 25 items, with offline preview and cloud scoring through compliancehub.cn.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT

## Use Case:

Developers, compliance teams, and privacy reviewers use this skill to preview PIPL check items locally or run a scored self-assessment that returns a compliance report with risk levels and remediation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scored checks send compliance answers to compliancehub.cn, which may reveal sensitive details about data practices, service providers, controls, or legal exposure.

Mitigation: Use --non-interactive or --non-interactive-json for local preview only, and run scored checks only after confirming the cloud destination and data-sharing posture are acceptable.

Risk: Registered scoring uses an API key, and anonymous scoring uses a local trial identifier.

Mitigation: Prefer the COMPLIANCEHUB_API_KEY environment variable on shared hosts, or store the key only in the private per-user config path described by the skill.

Risk: The report provides compliance guidance but is not a legal opinion.

Mitigation: Have qualified counsel or an accountable privacy reviewer validate findings before relying on them for formal PIPL compliance decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/pipl-check)
- [ComplianceHub cloud endpoint](https://compliancehub.cn)
- [ComplianceHub account page](https://compliancehub.cn/account.html?skill=pipl-check)

## Skill Output:

**Output Type(s):** [text, JSON, HTML, guidance]

**Output Format:** [Plain text, JSON, or HTML compliance report; offline preview can be printed as text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A scored run may write the generated report to a user-specified output file.]

## Skill Version(s):

3.0.3 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
