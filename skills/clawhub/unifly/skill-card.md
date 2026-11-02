## Description:

Inspect and manage UniFi Network infrastructure with the unifly CLI, including devices, clients, VLANs, WiFi, firewall, VPN, switch ports, site settings, and cloud fleets; the skill excludes UniFi Protect camera and recording management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hyperb1iss](https://clawhub.ai/user/hyperb1iss)

### License/Terms of Use:

MIT-0

## Use Case:

Network administrators and developers use this skill to inspect, configure, monitor, and troubleshoot UniFi Network infrastructure through the unifly CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A command applied to the wrong site or with overly broad access could disrupt network services.

Mitigation: Verify the target site and use narrowly scoped credentials before making changes.

Risk: Firewall, VPN, or connectivity changes can interrupt access or network traffic.

Mitigation: Review the proposed changes and their effects before applying them.

Risk: The skill review does not certify the separately installed unifly binary.

Mitigation: Install a trusted CLI release and consult its version-matched `unifly skill` guide.

## Reference(s):

- [UniFly installation instructions](https://github.com/hyperb1iss/unifly#-install)
- [ClawHub unifly release page](https://clawhub.ai/hyperb1iss/skills/unifly)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and guidance may support inspection or network configuration, depending on the task.]

## Skill Version(s):

0.12.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
