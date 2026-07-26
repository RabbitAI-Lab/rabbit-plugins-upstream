## Description: <br>
Create Huawei Cloud FunctionGraph functions from user-provided function names, runtimes, handlers, and code. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to create, deploy, or upload Huawei Cloud FunctionGraph functions with configured runtime, handler, memory, timeout, and source code. It also provides setup, IAM, and verification guidance for confirming the deployed function. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create Huawei Cloud functions and may require broad cloud or IAM authority. <br>
Mitigation: Use a least-privilege Huawei IAM user in a test project, confirm the region, project, function name, and code before running, and avoid wildcard or IAM-admin policies unless an administrator explicitly approves them. <br>
Risk: Function code supplied to the workflow may be uploaded to Huawei Cloud. <br>
Mitigation: Do not use production credentials or sensitive source code unless the upload is intentional and has been reviewed. <br>


## Reference(s): <br>
- [FunctionGraph Documentation](https://support.huaweicloud.com/functiongraph/) <br>
- [Huawei Cloud Python SDK](https://github.com/huaweicloud/huaweicloud-sdk-python-v3) <br>
- [IAM Policies Guide](references/iam-policies.md) <br>
- [SDK Installation Guide](references/sdk-installation-guide.md) <br>
- [Verification Methods](references/verification-method.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Code, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create Huawei Cloud FunctionGraph resources when executed with valid credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
