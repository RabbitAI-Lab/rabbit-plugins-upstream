## Description: <br>
Configure Huawei Cloud OBS static website hosting with Python SDK and a custom domain. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to enable or repair Huawei Cloud OBS static website hosting, register a required custom domain, configure Huawei Cloud DNS when applicable, and verify published website behavior. <br>

### Deployment Geography for Use: <br>
Global, subject to local domain registration and ICP filing requirements for mainland China deployments. <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Huawei Cloud credentials that can modify OBS website settings and DNS records. <br>
Mitigation: Use least-privilege IAM scoped to the exact bucket and DNS zone, prefer environment variables or secure local profiles, and avoid putting AK/SK values on command lines. <br>
Risk: Public website, DNS, or bucket-policy changes can expose content or leave the custom domain misconfigured. <br>
Mitigation: Confirm the required custom domain before configuration, verify CNAME resolution, check root and missing-path HTTP behavior, and treat 403 responses as requiring both public-read and IAM permission review. <br>
Risk: The workflow may direct users to install external Huawei Cloud CLI tooling. <br>
Mitigation: Verify downloaded CLI installers before execution and install only from documented Huawei Cloud distribution URLs. <br>


## Reference(s): <br>
- [CLI Installation and Configuration Guide](artifact/references/cli-installation-guide.md) <br>
- [Huawei Cloud DNS Configuration for OBS Static Website](artifact/references/hcloud-dns-obs-website.md) <br>
- [IAM Policy - Huawei Cloud OBS Website Host](artifact/references/iam-policies.md) <br>
- [OBS Python SDK Website Configuration Notes](artifact/references/obs-python-sdk-website.md) <br>
- [Validation Rules](artifact/references/verification-method.md) <br>
- [Huawei Cloud Domain Registration Service](https://www.huaweicloud.com/product/domain.html) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and verification results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include DNS handoff details, website verification status, and remediation steps for permission or endpoint failures.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
