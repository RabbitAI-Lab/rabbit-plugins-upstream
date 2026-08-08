## Description: <br>
Lists Huawei Cloud IAM projects for an authenticated account, including project ID, name, domain ID, parent ID, enabled status, and description, using KooCLI as the primary path and the Huawei Cloud IAM Python SDK as a fallback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and account administrators use this skill to inventory Huawei Cloud IAM projects, discover project identifiers, support permission review, and plan multi-region operations without changing IAM resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses configured Huawei Cloud credentials to query IAM project inventory. <br>
Mitigation: Use least-privilege credentials with project-list permission where possible, and keep AK/SK in hcloud configuration or environment variables rather than pasting them into chat. <br>
Risk: Project inventory output can expose account structure and identifiers. <br>
Mitigation: Review returned project IDs, domain IDs, and descriptions before sharing them outside the authorized operations context. <br>


## Reference(s): <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Data Flow Diagram](references/dataflow-diagram.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only project inventory guidance using the user's configured Huawei Cloud credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
