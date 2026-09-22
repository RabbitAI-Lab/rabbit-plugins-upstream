## Description:

Manages Huawei Cloud SWR enterprise instance lifecycle workflows with hcloud CLI and a Python SDK helper for instance creation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pintudeyudi](https://clawhub.ai/user/pintudeyudi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to administer Huawei Cloud SWR enterprise instances, namespaces, registries, credentials, endpoints, custom domains, image artifacts, and verification workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can delete SWR instances, namespaces, repositories, artifacts, credentials, endpoints, domains, and job records.

Mitigation: Require explicit human confirmation for destructive actions and verify the target resource before execution.

Risk: Credential workflows can create or expose long-term and temporary registry credentials.

Mitigation: Use least-privileged IAM users, keep secrets in approved secret stores, avoid inline secret values, and rotate credentials regularly.

Risk: Public registry access or skipped TLS verification can expose registries or weaken transport security.

Mitigation: Require reviewed IP allowlists, avoid 0.0.0.0/0 except under documented exception, and keep TLS verification enabled.

Risk: The Python helper depends on Huawei Cloud SDK packages to perform instance creation.

Mitigation: Pin and review SDK dependencies before running the helper in a production environment.

## Reference(s):

- [Huawei Cloud SWR Enterprise Console](https://console.huaweicloud.com/swr-instance)
- [SWR Enterprise Instance - Command Reference](references/command-reference.md)
- [SWR Instance API Reference Guide](references/swr-instance-api-guide.md)
- [IAM Permission Policies - SWR Enterprise Instance Skill](references/iam-policies.md)
- [SWR Enterprise Instance - Parameter Reference](references/parameter-reference.md)
- [SWR Enterprise Instance - Output Format](references/output-format.md)
- [Verification Method - SWR Enterprise Instance Skill](references/verification-method.md)
- [Common Pitfalls & Solutions](references/common-pitfalls.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose hcloud CLI commands, Python helper invocations, IAM policy snippets, and verification steps.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
