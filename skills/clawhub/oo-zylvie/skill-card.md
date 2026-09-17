## Description:

Zylvie lets an agent read, create, update, and delete Zylvie data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to inspect Zylvie action schemas, run Zylvie connector actions, and manage products, coupons, license keys, subscriptions, and account details through an authenticated OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote shell installers that should not be run without verification.

Mitigation: Use a safer, verified oo CLI installation method and review the installer source before execution.

Risk: The security review says redeem_license_key and refund_license_key change Zylvie state even though they are not tagged as write or destructive in the artifact.

Mitigation: Require explicit user confirmation for all state-changing Zylvie actions, including redeem_license_key and refund_license_key.

## Reference(s):

- [Zylvie ClawHub listing](https://clawhub.ai/oomol/skills/oo-zylvie)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Zylvie homepage](https://zylvie.com/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON payloads, Configuration guidance]

**Output Format:** [Markdown with inline bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
