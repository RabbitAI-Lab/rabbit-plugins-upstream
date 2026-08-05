## Description: <br>
Lists Huawei Cloud IAM roles for the authenticated account, including role ID, display name, internal name, catalog, and type, using KooCLI as the primary path with CLI or Python SDK fallback options. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Cloud administrators, security reviewers, and developers use this skill to inventory Huawei Cloud IAM roles, review permission scope, and troubleshoot account-level IAM configuration without changing IAM resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Ambiguous user requests could activate the IAM role inventory workflow when the user did not intend to query Huawei Cloud IAM. <br>
Mitigation: Confirm ambiguous requests before running IAM commands and proceed only when the user asks for Huawei Cloud IAM role metadata. <br>
Risk: The skill uses configured Huawei Cloud credentials to query IAM role metadata. <br>
Mitigation: Use least-privilege credentials with only role-list permission and never paste AK/SK secrets into chat. <br>


## Reference(s): <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Data Flow Diagram](references/dataflow-diagram.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, configuration guidance, and optional JSON role output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports IAM role metadata and total role count; uses read-only Huawei Cloud IAM list operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
