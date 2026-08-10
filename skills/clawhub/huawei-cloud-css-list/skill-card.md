## Description: <br>
Query Huawei Cloud CSS clusters in the current project and region, including cluster IDs, names, status, endpoint, engine and version, node configuration, network IDs, tags, and enterprise project, with optional engine filtering and pagination. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and support engineers use this skill to list Huawei Cloud CSS clusters in a selected project and region, filter by datastore engine type, and inspect cluster status, endpoint, version, node, network, tag, and enterprise project details for inventory or troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Huawei Cloud credentials may be exposed if access keys are pasted into shared conversations, terminals, or logs. <br>
Mitigation: Use secure credential storage or temporary credentials where available, and never ask for or echo AK/SK values. <br>
Risk: Cluster inventory output can reveal internal infrastructure details such as endpoints, VPCs, subnets, security groups, tags, and enterprise projects. <br>
Mitigation: Review and redact query output before sharing it outside the intended operational audience. <br>
Risk: Overbroad cloud permissions can expose more CSS inventory than the task requires. <br>
Mitigation: Run the skill with a least-privilege read-only IAM identity limited to the selected project and region. <br>


## Reference(s): <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Data Flow Diagram](references/dataflow-diagram.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance, Analysis] <br>
**Output Format:** [Markdown with inline bash commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Huawei Cloud region; supports optional datastoreType, limit, and offset parameters.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
