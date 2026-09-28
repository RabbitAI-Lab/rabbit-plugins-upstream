## Description:

Guides developers through Huifu merchant and user onboarding, KYC, business activation, account management, and SDK integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huifu](https://clawhub.ai/user/huifu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers integrating Huifu use this skill to prepare merchant and user onboarding requests, map KYC fields, configure business capabilities, and troubleshoot status, signing, and notification flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live PHP integrations may use an SDK path that does not verify TLS certificates or hostnames.

Mitigation: Do not send live PHP traffic until the SDK or transport is confirmed to validate certificates and hostnames.

Risk: Debug output or examples could expose private keys and sensitive identity or banking records.

Mitigation: Disable DEBUG before loading the SDK and keep private keys and KYC materials out of logs, frontends, and examples.

Risk: Onboarding requests can send real identity, banking, image, or business-configuration data to Huifu.

Mitigation: Require explicit user approval before sending real data or changing live business configurations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huifu/skills/huifu-merchant-onboarding)
- [Huifu merchant onboarding overview](references/shared-overview.md)
- [Huifu merchant onboarding field contracts](references/merchant-onboarding-field-contracts.md)
- [Huifu user onboarding overview](references/user-onboarding-shared-overview.md)
- [Huifu official service source index](references/official-service-source-index.md)
- [Huifu merchant application status documentation](https://paas.huifu.com/partners/api/doc/shgl/shjj/api_shjj_sqdztcx.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes API field mappings and troubleshooting guidance.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
