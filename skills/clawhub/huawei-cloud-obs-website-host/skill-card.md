## Description:

Configures and verifies static website hosting for an existing Huawei Cloud OBS bucket with a custom domain and, when applicable, Huawei Cloud DNS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to configure an existing OBS bucket as a static website, connect a custom domain, and troubleshoot access, DNS, and HTTPS verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud credentials or TLS private keys could be exposed during setup.

Mitigation: Use temporary, least-privilege credentials scoped to the bucket and DNS zone; prefer managed certificate IDs and keep secrets off command lines and logs.

Risk: OBS website and DNS changes can persist and make bucket content publicly accessible.

Mitigation: Confirm the intended bucket, domain, public-read scope, and DNS zone before changes, then verify the custom-domain endpoint.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-obs-website-host)
- [OBS Python SDK website configuration](artifact/references/obs-python-sdk-website.md)
- [Huawei Cloud DNS configuration](artifact/references/hcloud-dns-obs-website.md)
- [IAM permissions](artifact/references/iam-policies.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with verification results and remediation steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports custom-domain access checks; does not upload website files.]

## Skill Version(s):

1.0.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
