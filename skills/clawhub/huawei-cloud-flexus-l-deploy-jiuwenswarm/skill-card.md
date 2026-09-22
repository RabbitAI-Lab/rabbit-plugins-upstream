## Description:

Automates deployment of JiuwenSwarm or JiuwenClaw on Huawei Cloud Flexus L instances, including instance creation, remote service deployment, verification, model configuration, and message channel setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to provision Huawei Cloud Flexus L infrastructure and deploy JiuwenSwarm with model and messaging integrations. It is intended for users who need a guided, phased deployment workflow with verification and troubleshooting references.

### Deployment Geography for Use:

Huawei Cloud China regions supported by the skill: cn-north-4, cn-east-3, cn-south-1, and cn-southwest-2.

## Known Risks and Mitigations:

Risk: The skill requires Huawei Cloud credentials with permissions that can create resources and execute remote commands.

Mitigation: Use temporary least-privilege credentials, review the IAM permissions before execution, and rotate credentials that may have been printed or stored with broad permissions.

Risk: Deployment can create billable cloud resources and run remote root-level changes through Huawei Cloud COC.

Mitigation: Confirm target region, flavor, estimated cost, instance IDs, and customer approval before creating or modifying resources.

Risk: Opening inbound access to the JiuwenSwarm web interface can expose the service publicly.

Mitigation: Restrict security group access to port 5173, open it only when needed, and close or narrow the rule after verification.

Risk: Model and messaging credentials may be written to remote configuration files or appear in generated output.

Mitigation: Avoid sharing COC logs or generated configuration output, keep file permissions restrictive, and rotate model or messaging credentials after exposure.

Risk: The security review flags the release as suspicious because it handles secrets and remote root changes.

Mitigation: Install only after reviewing the skill behavior and accepting the required cloud permissions and operational risks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-flexus-l-deploy-jiuwenswarm)
- [API Specification](references/api-specs.md)
- [IAM Permission Policies](references/iam-policies.md)
- [Deployment Checklist](references/deployment-checklist.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Troubleshooting Guide](references/troubleshooting.md)
- [Huawei Cloud IAM FAQ](https://support.huaweicloud.com/iam_faq/iam_01_0620.html)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, status text, configuration values, and deployment URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report COC execution UUIDs, instance identifiers, public IP addresses, service status, health-check results, and configuration guidance.]

## Skill Version(s):

1.0.3 (source: server release metadata; SKILL.md frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
