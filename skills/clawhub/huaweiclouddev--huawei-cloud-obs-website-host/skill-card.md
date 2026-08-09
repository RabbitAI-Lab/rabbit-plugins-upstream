## Description: <br>
Configure Huawei Cloud OBS static website hosting with Python SDK and a custom domain. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to enable, repair, and verify static website hosting for an existing Huawei Cloud OBS bucket. It guides custom-domain registration, optional Huawei Cloud DNS CNAME setup, IAM remediation, and endpoint verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change Huawei Cloud OBS website settings and DNS records. <br>
Mitigation: Use least-privilege Huawei Cloud credentials scoped to the intended bucket and DNS zone where possible. <br>
Risk: The artifact includes a remote hcloud CLI installer path. <br>
Mitigation: Prefer a signed or package-manager hcloud installation, or verify Huawei's installer before running it. <br>
Risk: Huawei Cloud AK/SK credentials or tokens could be exposed through chat, logs, or copied configuration output. <br>
Mitigation: Report only credential presence or absence, and never print or paste AK/SK/token values. <br>


## Reference(s): <br>
- [CLI Installation and Configuration Guide](references/cli-installation-guide.md) <br>
- [Huawei Cloud DNS Configuration for OBS Static Website](references/hcloud-dns-obs-website.md) <br>
- [IAM Policy - Huawei Cloud OBS Website Host](references/iam-policies.md) <br>
- [OBS Python SDK Website Configuration Notes](references/obs-python-sdk-website.md) <br>
- [Validation Rules](references/verification-method.md) <br>
- [Huawei Cloud Domain Registration Service](https://www.huaweicloud.com/product/domain.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured verification summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include JSON verification output when the bundled verifier is run with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
