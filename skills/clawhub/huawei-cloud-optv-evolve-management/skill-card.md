## Description:

Huawei Cloud algorithm auto-design (LLM4AD) skill that manages OptVerse algorithm projects, file uploads, evolve task lifecycle operations, results, logs, and optional IAM agency and OBS bucket authorization through KooCLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Huawei Cloud operators use this skill to run OptVerse LLM4AD code-evolution workflows, including creating algorithm projects, uploading Python or C++ assets, creating and monitoring evolve tasks, and retrieving results or logs. Operators may also use its optional IAM agency and OBS bucket guidance when result upload is required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional OBS upload setup can create a permanent, broadly privileged cloud delegation.

Mitigation: Prefer the default no-OBS-upload path; when OBS upload is required, have a Huawei Cloud operator review the permissions and scope them to the required bucket and prefix.

Risk: IAM agency and bucket authorization may leave unnecessary cloud access in place after use.

Mitigation: Avoid FOREVER duration, confirm the trusted principal, and revoke or delete the agency and policy after the workflow is complete.

Risk: Cloud credentials could be exposed if AK/SK values are copied into chat, scripts, or logs.

Mitigation: Never paste AK/SK values into chat or logs; verify only credential presence through hcloud configure list.

## Reference(s):

- [Reference Index](references/readme.md)
- [KooCLI Installation Guide](references/cli-installation-guide.md)
- [Prerequisites](references/prerequisites.md)
- [OptVerse API to KooCLI Mapping](references/api-mapping.md)
- [IAM Permission Policies](references/iam-policies.md)
- [IAM Agency Creation and Management](references/iam-agency.md)
- [OBS Bucket Authorization via Agency](references/agency-policy.md)
- [Algorithm Project Workflow](references/algorithm-workflow.md)
- [Evolve Task Workflow](references/evolve-task-workflow.md)
- [Results, Logs, and Status](references/result-logs-status.md)
- [Python Project Conventions](references/language-python.md)
- [C++ Project Conventions](references/language-cpp.md)
- [Verification Methods](references/verification-method.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline shell commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operational constraints for KooCLI execution, credential handling, IAM agency setup, OBS authorization, and Python/C++ task assets.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
