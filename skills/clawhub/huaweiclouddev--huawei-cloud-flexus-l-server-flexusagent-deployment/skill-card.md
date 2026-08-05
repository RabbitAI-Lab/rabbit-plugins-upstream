## Description: <br>
Deploys the Dify-based FlexusAgent AI Agent development platform on Huawei Cloud Flexus L instances and supports password management, MaaS model configuration, and workflow import. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to create and operate a Huawei Cloud Flexus L instance running the FlexusAgent AI Agent platform. It guides deployment, post-deployment password setup, MaaS model provider configuration, and workflow import. <br>

### Deployment Geography for Use: <br>
Huawei Cloud regions cn-north-4, cn-east-3, cn-south-1, and cn-southwest-2. <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles Huawei Cloud access keys, security tokens, admin passwords, and MaaS API keys that could be exposed through chat, logs, or command history. <br>
Mitigation: Use a dedicated least-privilege, time-limited Huawei Cloud identity; pass secrets through environment variables where possible; avoid command-line secrets; and do not share run logs. <br>
Risk: The skill performs high-privilege cloud deployment and operations that can affect production accounts. <br>
Mitigation: Review before installing, confirm required IAM permissions, run in a dedicated account or project, and verify each deployment parameter before execution. <br>
Risk: Deployment can expose a Web UI on public port 80 and create prepaid cloud resources that incur costs. <br>
Mitigation: Confirm that public HTTP exposure is acceptable, restrict security group access when possible, and require explicit user confirmation before creating resources. <br>
Risk: The release depends on external Python packages and cloud-side scripts or services. <br>
Mitigation: Inspect or pin externally fetched dependencies and scripts before production use, and review the generated deployment plan against organizational security policy. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-flexus-l-server-flexusagent-deployment) <br>
- [Flexus L Instance Purchase Guide](https://support.huaweicloud.com/api-flexusl/create_instance_0001.html) <br>
- [Flexus L Instance Specifications](https://support.huaweicloud.com/productdesc-flexusl/pd_01_0003.html) <br>
- [IAM Permission Policy Reference](references/iam-policies.md) <br>
- [Skill Verification Method](references/verification-method.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with command snippets and configuration steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Huawei Cloud credentials, selected deployment region/specification, optional MaaS API key, and explicit user confirmation for cost-incurring deployment operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
