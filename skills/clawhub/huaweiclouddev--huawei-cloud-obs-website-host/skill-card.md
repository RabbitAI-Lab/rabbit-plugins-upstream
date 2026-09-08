## Description:

Configure Huawei Cloud OBS static website hosting with the Python SDK and a required custom domain, including website settings, DNS guidance, public-read verification, and 403/404 troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to configure or repair existing Huawei Cloud OBS buckets as static websites with required custom domains, DNS handoff or Huawei Cloud DNS records, and post-change endpoint checks.

### Deployment Geography for Use:

Global, with mainland China website hosting subject to ICP filing requirements.

## Known Risks and Mitigations:

Risk: The skill can use Huawei Cloud credentials to modify OBS bucket website settings, register custom domains, and optionally create DNS records.

Mitigation: Use least-privileged or temporary credentials and review the target bucket, custom domain, DNS zone, and IAM policy before running changes.

Risk: Credentials, tokens, or PEM private keys could be exposed if supplied in chat or command lines.

Mitigation: Prefer environment variables or secure local profile storage, and do not print AK/SK, tokens, or private key material.

Risk: Static website setup may expose bucket content publicly or remain incomplete if public-read, custom domain, DNS, or IAM settings are wrong.

Mitigation: Confirm the custom domain prerequisite, verify public-read access and DNS resolution, and run the bundled verifier before claiming completion.

## Reference(s):

- [CLI Installation and Configuration Guide](artifact/references/cli-installation-guide.md)
- [Huawei Cloud DNS Configuration for OBS Static Website](artifact/references/hcloud-dns-obs-website.md)
- [IAM Policy - Huawei Cloud OBS Website Host](artifact/references/iam-policies.md)
- [OBS Python SDK Website Configuration Notes](artifact/references/obs-python-sdk-website.md)
- [Validation Rules](artifact/references/verification-method.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, Python script invocations, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May perform live OBS bucket and DNS configuration only after the user supplies target inputs and credentials.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
