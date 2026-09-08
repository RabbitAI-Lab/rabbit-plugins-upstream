## Description:

Queries Huawei Cloud ECS instance details and instance lists through KooCLI using read-only ECS APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to inspect Huawei Cloud ECS inventory, retrieve individual instance details, and support troubleshooting or resource audits without modifying cloud resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Huawei Cloud AK/SK credentials can be exposed if pasted into shared command lines or logs.

Mitigation: Use environment variables or secure CLI configuration, avoid placing AK/SK values directly in commands, and keep credentials out of transcripts and logs.

Risk: Returned ECS inventory can expose sensitive operational data, including instance names, IDs, key pair names, volumes, and IP addresses.

Mitigation: Treat query output as sensitive cloud inventory and share it only with users and systems authorized to view the account's ECS resources.

Risk: The skill depends on the Huawei Cloud hcloud installer and local CLI behavior.

Mitigation: Verify the hcloud installer source before installation and confirm the installed CLI version in the target environment.

Risk: Overbroad IAM permissions would expand the impact of credential misuse.

Mitigation: Use a least-privilege IAM identity limited to ecs:servers:get and ecs:servers:list for this skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yangaiwu/skills/huawei-cloud-ecs-detail-query)
- [Huawei Cloud KooCLI documentation](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [CLI installation and authentication guide](artifact/cli-installation-guide.md)
- [IAM policies](artifact/iam-policies.md)
- [Dataflow diagram](artifact/dataflow-diagram.md)
- [Verification method](artifact/verification-method.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance plus formatted terminal text output from ECS list and detail queries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Huawei Cloud ECS queries; output may include sensitive operational inventory such as instance IDs, names, key pair names, volumes, and IP addresses.]

## Skill Version(s):

1.0.1 (source: server release evidence and changelog; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
