## Description:

Queries Huawei Cloud SWR namespaces in the current project and region, with optional namespace filtering and read-only reporting of namespace IDs, names, creators, auth levels, access user counts, and repository counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and support engineers use this skill to inspect Huawei Cloud SWR namespace inventory for daily checks and troubleshooting. It helps list all namespaces, filter by namespace name, and review read-only namespace attributes before deciding whether follow-up operational work is needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Overbroad cloud permissions could expose more SWR resources than needed.

Mitigation: Use a least-privilege IAM user with SWR read-only permissions such as swr:namespace:list, or the SWR ReadOnlyAccess policy when appropriate.

Risk: Huawei Cloud access keys or secret keys could be exposed in shared conversations, terminals, or logs.

Mitigation: Use configured CLI profiles or environment variables and avoid pasting, echoing, or logging real AK/SK values.

Risk: Installing the Huawei Cloud CLI with elevated privileges can introduce supply-chain or local system risk.

Mitigation: Verify the KooCLI download source before installation and review any command that uses sudo.

Risk: Untrusted region or namespace values could change test-script behavior.

Mitigation: Confirm region and namespace values with the user and do not pass untrusted values to the shell-based test script.

## Reference(s):

- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [CLI Installation Guide](references/cli-installation-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only SWR namespace listing; requires a confirmed Huawei Cloud region and existing CLI profile or environment-based credentials.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
