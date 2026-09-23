## Description:

Set up HTTPS, manage TLS certificates, and debug secure connection issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

Developers and site operators use this skill to set up HTTPS, manage certificate formats and server configuration, automate renewal, and troubleshoot TLS errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Certificate renewal, permission, or private-key extraction commands can disrupt production systems or expose sensitive key material if run without review.

Mitigation: Review commands before execution, verify domains and file paths, and protect private keys such as privkey.pem with restrictive permissions.

Risk: The Node.js redirect example can be unsafe if it reflects an untrusted Host header.

Mitigation: Replace the dynamic redirect hostname with a fixed hostname or an allowlisted hostname before production use.

## Reference(s):

- [Certificate Format Conversions](artifact/formats.md)
- [SSL Configuration by Server](artifact/servers.md)
- [SSL Troubleshooting Guide](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
