## Description:

Huawei Cloud algorithm auto-design (LLM4AD) skill for managing OptVerse code-evolution workflows through KooCLI, including algorithm projects, file uploads, evolve task lifecycle operations, status polling, result retrieval, log inspection, and optional IAM agency setup for OBS uploads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to operate Huawei Cloud Scientific Computing Zone algorithm auto-design workflows: create algorithm projects, upload Python or C++ sources, create and run evolve tasks, monitor progress, and retrieve results and logs. Teams that need task outputs in OBS can use the optional IAM agency and bucket authorization guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, start, stop, and delete Huawei Cloud OptVerse resources.

Mitigation: Review planned commands before execution and require explicit confirmation for destructive operations such as deleting algorithms, tasks, agencies, or permissions.

Risk: Credential and state handling can expose sensitive cloud access if AK/SK values are copied into conversations, scripts, logs, or scratchpads.

Mitigation: Use least-privilege temporary credentials where possible, verify credential presence only through safe KooCLI checks, and avoid storing secrets in agent memory or workspace artifacts.

Risk: Optional OBS result uploads require IAM agency delegation and bucket permissions that may be broader or longer-lived than needed.

Mitigation: Skip OBS upload unless required, and when delegation is needed, make agency policy time-bounded and limited to the specific bucket or prefix.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-optv-evolve-management)
- [Reference Index](references/readme.md)
- [KooCLI Installation Guide](references/cli-installation-guide.md)
- [Prerequisites](references/prerequisites.md)
- [OptVerse API to KooCLI mapping](references/api-mapping.md)
- [Algorithm project management](references/algorithm-workflow.md)
- [Evolve task management](references/evolve-task-workflow.md)
- [Results, logs, and status](references/result-logs-status.md)
- [IAM permission policies](references/iam-policies.md)
- [IAM agency creation and management](references/iam-agency.md)
- [OBS bucket authorization via agency](references/agency-policy.md)
- [Python evaluator, baseline, and algorithm guide](references/language-python.md)
- [C++ evaluator, baseline, and algorithm guide](references/language-cpp.md)
- [Parameter forms and hcloud CLI usage](references/parameter-format.md)
- [Verification methods](references/verification-method.md)
- [Troubleshooting](references/troubleshooting.md)
- [Scripts directory guide](scripts/readme.md)
- [Templates directory guide](templates/README.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell commands, code snippets, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent guidance for KooCLI-based Huawei Cloud OptVerse workflows and local helper script usage.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
