## Description:

Configure DNS records correctly with proper TTLs, email authentication, and migration strategies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

Developers and site operators use this skill to plan DNS migrations, configure DNS records, validate email authentication, and debug DNS resolution issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect DNS, SPF, DKIM, DMARC, CAA, proxy, or TTL choices can disrupt websites, certificates, or email delivery.

Mitigation: Review proposed DNS changes before applying them at the DNS provider and test records with authoritative and public resolvers.

Risk: The skill provides DNS guidance but does not automate provider-side changes.

Mitigation: Apply changes manually through the provider and verify resulting records before considering a migration complete.

## Reference(s):

- [DNS Skill Release](https://clawhub.ai/ivangdavila/skills/dns)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline DNS record examples and diagnostic commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No automation; users apply changes through their DNS provider.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
