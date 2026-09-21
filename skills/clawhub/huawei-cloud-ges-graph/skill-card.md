## Description:

Provides access guidance for operating Huawei Cloud Graph Database GES through local Python or Node.js scripts, including Cypher and GQL queries, schema and label management, graph summaries, and graph data editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure credentials and operate Huawei Cloud GES graph databases from an agent terminal workflow. It supports query execution, graph inspection, schema-aware graph editing, and import/export operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use Huawei Cloud credentials to mutate, export, and delete graph data.

Mitigation: Use least-privilege, test-scoped credentials and avoid reusable passwords.

Risk: Graph clearing, bulk deletion, import/export, and OBS object operations can affect production data.

Mitigation: Run these operations only with an explicit target, current backup, and user confirmation.

Risk: Security evidence states that transport issues should be fixed before trusting the skill with sensitive graph data or credentials.

Mitigation: Resolve the transport issues before using the skill with sensitive data or production credentials.

## Reference(s):

- [Configuration file format](references/ges_env.csv.example)
- [Huawei Cloud GES graph data format documentation](https://support.huaweicloud.com/usermanual-ges/ges_01_0153.html)
- [Huawei Cloud GES business API access guide](https://support.huaweicloud.com/api-ges/ges_03_0112.html)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline Python, JavaScript, bash, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated guidance may execute cloud operations through local scripts when used by an agent.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
