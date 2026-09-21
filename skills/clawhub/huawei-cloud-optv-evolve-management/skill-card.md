## Description:

Guides agents through Huawei Cloud OptVerse algorithm auto-design workflows using KooCLI, including project setup, file upload, evolve task lifecycle management, result retrieval, log inspection, and optional IAM agency setup for OBS result upload.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to manage Huawei Cloud OptVerse LLM4AD projects and evolve tasks, including setup checks, hcloud command construction, status polling, result inspection, and optional OBS upload authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional OBS upload path documents broad, long-lived cloud delegation.

Mitigation: Require admin review before using OBS upload, restrict agency permissions to the exact bucket or prefix and minimal actions, and document how to detach or delete the agency after use.

Risk: The skill can operate Huawei Cloud OptVerse through configured hcloud credentials.

Mitigation: Install only in environments where agent access to those credentials is acceptable, verify credential presence without exposing AK/SK values, and use the precheck flow before cloud operations.

Risk: Destructive cloud operations such as deleting algorithms, tasks, agencies, or permissions may affect active resources.

Mitigation: Use explicit two-step confirmation before destructive hcloud operations and review the exact command and target identifiers before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-optv-evolve-management)
- [Reference index](references/readme.md)
- [Prerequisites](references/prerequisites.md)
- [KooCLI installation guide](references/cli-installation-guide.md)
- [OptVerse API mapping](references/api-mapping.md)
- [Algorithm workflow](references/algorithm-workflow.md)
- [Evolve task workflow](references/evolve-task-workflow.md)
- [IAM policies](references/iam-policies.md)
- [IAM agency](references/iam-agency.md)
- [OBS bucket authorization](references/agency-policy.md)
- [Result logs and status](references/result-logs-status.md)
- [Troubleshooting](references/troubleshooting.md)
- [Verification method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, configuration steps, and Python/C++ template code references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local helper scripts and templates; cloud actions are performed through hcloud with configured credentials.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
