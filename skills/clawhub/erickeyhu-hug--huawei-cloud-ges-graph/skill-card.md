## Description:

Provides guidance and Python/Node.js helpers for operating Huawei Cloud Graph Engine Service with Cypher and GQL queries, schema and label management, graph data editing, and import/export workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and engineers use this skill to configure Huawei Cloud GES access, run graph queries, manage schema and labels, edit graph data, and coordinate import/export operations from an agent-driven terminal workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs live, credentialed Huawei Cloud graph and storage operations, including destructive graph actions.

Mitigation: Use least-privileged Huawei Cloud credentials and require explicit user confirmation with parameter review before clear, bulk delete, import/export, OBS delete, or download-to-local-path operations.

Risk: Credentials may be supplied through environment variables, token values, or local configuration files.

Mitigation: Avoid plaintext long-lived secrets, do not print credentials or tokens, and prefer short-lived or scoped credentials where available.

Risk: Incorrect IAM, GES, or OBS endpoint settings can send requests to the wrong service or region.

Mitigation: Confirm IAM, GES, and OBS endpoints and regions with the user before executing live operations.

## Reference(s):

- [Huawei Cloud GES graph data format documentation](https://support.huaweicloud.com/usermanual-ges/ges_01_0153.html)
- [Huawei Cloud GES business API access guide](https://support.huaweicloud.com/api-ges/ges_03_0112.html)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with inline Python, JavaScript, bash, Cypher, GQL, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands or snippets that execute credentialed Huawei Cloud GES and OBS operations when run by an agent.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
