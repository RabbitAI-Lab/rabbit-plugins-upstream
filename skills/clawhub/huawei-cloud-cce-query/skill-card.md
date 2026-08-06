## Description: <br>
Query Huawei Cloud CCE (Cloud Container Engine) clusters and report their names, IDs, statuses, versions, and node information across a project. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and SRE teams use this skill to inspect Huawei Cloud CCE clusters, retrieve cluster details, and list cluster nodes for inventory, daily operations, and troubleshooting. It focuses on read-only status and capacity visibility through the hcloud CLI or Python SDK fallback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Huawei Cloud credentials and may expose sensitive account access if credentials are pasted into shared shell history or logs. <br>
Mitigation: Use short-lived or tightly scoped credentials, prefer environment variables or secure local configuration, and avoid sharing command history that contains access keys. <br>
Risk: The hcloud CLI installation steps download binaries and use sudo to move them into the system path. <br>
Mitigation: Review the downloaded CLI source and integrity before privileged installation, or install through an approved internal software distribution process. <br>
Risk: Overbroad IAM permissions could allow more access than the read-only CCE queries need. <br>
Mitigation: Use CCE ReadOnlyAccess or a finer-grained policy limited to cluster and node get/list actions. <br>


## Reference(s): <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Data Flow Diagram](references/dataflow-diagram.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-cce-query) <br>
- [Publisher Profile](https://clawhub.ai/user/erickeyhu-hug) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, Python SDK examples, and summarized query results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Huawei Cloud CCE inventory and status guidance; requires user-provided region and, for detail queries, cluster or node identifiers.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.json release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
