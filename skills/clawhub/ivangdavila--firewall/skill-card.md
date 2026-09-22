## Description:

Configure firewalls on servers and cloud providers with security best practices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

Developers and system administrators use this skill to plan firewall rules for servers and cloud providers, including SSH access, web ports, provider firewalls, Docker exposure, IPv6 coverage, and debugging checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Firewall changes can lock users out of remote systems if access rules are applied incorrectly.

Mitigation: Allow and test SSH or remote access in a second session, keep the existing session open, and verify provider-console recovery access before enabling or changing firewall rules.

Risk: Generated firewall guidance could expose unnecessary services or omit provider-specific behavior.

Mitigation: Review proposed rules against the actual services, cloud-provider firewall behavior, Docker networking, and IPv4/IPv6 requirements before applying changes.

## Reference(s):

- [Firewall skill release page](https://clawhub.ai/ivangdavila/skills/firewall)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline command and configuration recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable code; guidance should be reviewed before applying firewall changes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
