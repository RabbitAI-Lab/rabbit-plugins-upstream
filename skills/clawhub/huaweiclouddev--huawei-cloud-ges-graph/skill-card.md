## Description:

Provides access guidance for Huawei Cloud Graph Database GES service, covering Cypher and GQL queries, schema and label management, summary queries, and graph data editing via terminal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure a Huawei Cloud GES connection and have an agent run Cypher or GQL operations, inspect graph metadata, manage labels and schema, and edit, import, or export graph data from the terminal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change or delete Huawei Cloud GES graph data.

Mitigation: Use narrowly scoped, revocable credentials and review import, export, clear, and delete requests before execution.

Risk: Credential handling and transport safeguards require review before production use.

Mitigation: Avoid storing long-lived secrets in the skill directory and do not use the skill against production data until TLS verification and destructive-operation confirmations are fixed.

## Reference(s):

- [Configuration file template](references/ges_env.csv.example)
- [Huawei Cloud GES graph data format documentation](https://support.huaweicloud.com/usermanual-ges/ges_01_0153.html)
- [Huawei Cloud GES business API access guide](https://support.huaweicloud.com/api-ges/ges_03_0112.html)
- [ClawHub skill release page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-ges-graph)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with inline bash, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on configured Huawei Cloud GES credentials and may trigger remote graph operations.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
