## Description: <br>
Queries Huawei Cloud IAM resources with read-only Python SDK scripts, covering users, groups, policies, agencies, access keys, MFA devices, security policies, compliance settings, and quotas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and security engineers use this skill to inspect Huawei Cloud IAM identity, policy, access-key, MFA, compliance, and quota information without creating or modifying cloud resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles Huawei Cloud credentials while TLS verification is disabled. <br>
Mitigation: Use least-privileged read-only credentials, run only on trusted networks and proxy settings, and prefer a version that enables TLS verification before broad deployment. <br>
Risk: The environment setup performs automatic dependency installation and credential validation. <br>
Mitigation: Review setup behavior before installation and run it in a controlled environment before using production credentials. <br>
Risk: Dependencies are not pinned to exact versions. <br>
Mitigation: Pin or verify dependency versions before commercial deployment. <br>


## Reference(s): <br>
- [IAM Script Usage Guide](artifact/references/iam/guide.md) <br>
- [Python Dependencies](artifact/requirements.txt) <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-iam-query) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON query results from packaged scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only query outputs depend on Huawei Cloud credentials, selected region, and script-specific parameters.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
