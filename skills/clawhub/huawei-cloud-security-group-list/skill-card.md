## Description: <br>
Lists Huawei Cloud security groups in a VPC project with IDs, names, descriptions, enterprise project IDs, tags, and creation times using KooCLI or the Huawei Cloud VPC Python SDK fallback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud administrators, and security engineers use this skill to inventory Huawei Cloud VPC security groups for auditing, firewall-rule review, troubleshooting, and compliance reporting. It supports read-only listing and filtering by region, name, ID, enterprise project, pagination, and output format. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent may query the wrong Huawei Cloud account or region and produce misleading inventory results. <br>
Mitigation: Confirm the target account and region before execution, and pass the intended region through --cli-region. <br>
Risk: Credentials with broader permissions than needed could expose more cloud resources than the skill requires. <br>
Mitigation: Use a least-privilege credential with vpc:securityGroups:list for this read-only workflow. <br>
Risk: Huawei Cloud AK/SK secrets could be exposed if pasted into chat. <br>
Mitigation: Configure credentials through hcloud configure or environment variables, and do not paste AK/SK values into the conversation. <br>


## Reference(s): <br>
- [CLI Installation Guide](artifact/references/cli-installation-guide.md) <br>
- [VPC Policies](artifact/references/vpc-policies.md) <br>
- [Verification Method](artifact/references/verification-method.md) <br>
- [Data Flow Diagram](artifact/references/dataflow-diagram.md) <br>
- [Acceptance Criteria](artifact/references/acceptance-criteria.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-security-group-list) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON-output guidance, and Python SDK fallback code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only inventory output; may include security group IDs, names, descriptions, enterprise project IDs, tags, creation times, and total count.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
