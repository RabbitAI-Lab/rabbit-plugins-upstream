## Description:

Provides a Clawdbot monitoring script intended to check selected system activity and record alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deyogaid](https://clawhub.ai/user/deyogaid)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use it to run continuous checks on a Clawdbot deployment and review recorded alerts. The release guidance says not to rely on this version for breach detection or Telegram alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Advertised protections are missing or broken, and the threat-selection setting does not restrict access. Do not rely on this version for breach detection or Telegram alerts.

Mitigation: Review before installing. Request working detection, enforced threat selection, and validated intervals before continuous use. Limit file permissions and monitor log growth.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/deyogaid/skills/security-monitor)
- [Publisher profile](https://clawhub.ai/user/deyogaid)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Console status messages and JSON alert records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Status and alert records are produced as the monitor runs.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
