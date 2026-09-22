## Description:

Configure Huawei Cloud OBS static website hosting for an existing bucket with Python SDK helpers, required custom-domain registration, optional Huawei Cloud DNS records, and endpoint verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to enable or repair Huawei Cloud OBS static website hosting, register the mandatory custom domain, configure Huawei Cloud DNS when applicable, and verify DNS and HTTP behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can configure an existing Huawei OBS bucket and register a public custom domain.

Mitigation: Use temporary or least-privilege Huawei Cloud credentials and review bucket, custom-domain, and IAM changes before approving execution.

Risk: DNS changes can expose or redirect a public website incorrectly.

Mitigation: Confirm the intended custom domain, hosted zone, CNAME target, and propagation checks before allowing Huawei Cloud DNS record changes.

Risk: Credential or TLS private-key material could be exposed if entered directly into commands or logs.

Mitigation: Avoid pasting secrets into command lines, never print AK/SK or private keys, and prefer certificate IDs over direct PEM private-key input.

## Reference(s):

- [OBS Python SDK Website Configuration Notes](references/obs-python-sdk-website.md)
- [IAM Policy - Huawei Cloud OBS Website Host](references/iam-policies.md)
- [Huawei Cloud DNS Configuration for OBS Static Website](references/hcloud-dns-obs-website.md)
- [CLI Installation and Configuration Guide](references/cli-installation-guide.md)
- [Validation Rules](references/verification-method.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured verification results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include DNS handoff details, IAM remediation steps, and JSON verification output when requested.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
