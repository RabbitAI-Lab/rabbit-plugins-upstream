## Description:

Query Huawei Cloud public NAT gateways for the current tenant or project, returning gateway names and key attributes with optional read-only filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and infrastructure teams use this skill to inspect Huawei Cloud public NAT gateway inventory, retrieve gateway names and attributes, and support daily checks or cost reviews without changing cloud resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recommended wrapper may send run metadata and some query or result data to an external reporting service by default.

Mitigation: Set SKILL_QUALITY_DISABLE=1 when external quality reporting is not appropriate, especially for sensitive cloud inventories.

Risk: The skill requires cloud credentials and NAT list permissions, so overly broad credentials increase blast radius.

Mitigation: Use least-privilege read-only IAM permissions such as nat:publicNatGateways:list or the narrowest acceptable read-only policy.

Risk: Untrusted region or template values in test commands can lead to unintended command behavior.

Mitigation: Review region and test variable inputs before running validation or test scripts.

## Reference(s):

- [IAM Policies](references/iam-policies.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Verification Method](references/verification-method.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-nat-list)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON or TSV result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only cloud inventory output; wrapper execution may report run metadata unless disabled.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
