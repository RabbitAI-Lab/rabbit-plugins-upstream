## Description:

Provides terminal guidance and helper scripts for operating Huawei Cloud Graph Database GES, including Cypher and GQL queries, schema and label management, graph summaries, and graph data edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure and operate Huawei Cloud GES graph databases from an agent-assisted terminal workflow. It helps prepare Cypher and GQL queries, manage graph schema and labels, inspect graph state, and run graph data changes through bundled Python or Node.js helpers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a real Huawei Cloud GES graph and OBS resources using configured credentials, including destructive graph actions.

Mitigation: Use scoped test credentials, restrict permissions to approved graphs and buckets, and require explicit human confirmation before clearing graphs, bulk deletion, import, or export operations.

Risk: The security evidence says transport and safeguard controls are not strong enough for automatic agent use.

Mitigation: Avoid production credentials unless the skill is revised to enforce TLS verification, use HTTPS for GES access, and add force flags or equivalent controls for destructive actions.

Risk: Credential material is required for AK/SK, password, or token-based authentication.

Mitigation: Provide credentials through a managed secret path or scoped environment and do not print access keys, secret keys, passwords, or tokens in agent output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-ges-graph)
- [GES environment configuration example](references/ges_env.csv.example)
- [Huawei Cloud GES graph database format documentation](https://support.huaweicloud.com/usermanual-ges/ges_01_0153.html)
- [Huawei Cloud GES business API access guide](https://support.huaweicloud.com/api-ges/ges_03_0112.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell, Python, Node.js, and JSON examples; script operations return JSON responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Huawei Cloud GES connection settings and scoped credentials before live graph operations can run.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
