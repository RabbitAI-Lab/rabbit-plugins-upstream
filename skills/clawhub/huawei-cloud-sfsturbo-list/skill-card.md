## Description:

Lists Huawei Cloud SFS Turbo file systems for the current tenant or project, returning names and selected attributes through KooCLI with a Python SDK fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and storage administrators use this skill to inventory Huawei Cloud SFS Turbo file systems, retrieve name-only lists, inspect status and size, and support routine storage reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The wrapper reports execution quality externally by default, including runtime details such as region, project_id, status, errors, and stack details.

Mitigation: Set SKILL_QUALITY_DISABLE=1 or restrict SKILL_QUALITY_ENDPOINT before use in sensitive cloud environments.

Risk: The skill requires Huawei Cloud credentials and SFS listing permissions to query tenant resources.

Mitigation: Use least-privilege IAM permission sfsturbo:shares:listShares or SFS Turbo ReadOnlyAccess, and keep AK/SK values out of chat transcripts and files.

## Reference(s):

- [Skill release page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-sfsturbo-list)
- [IAM Policies](references/iam-policies.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Verification Method](references/verification-method.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON or plain-text command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only SFS listing output; name-only mode prints one file system name per line, while full mode prints JSON lines with name, id, status, size, protocol, and region.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
