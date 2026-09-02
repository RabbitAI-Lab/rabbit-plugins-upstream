## Description:

Analyze the migrability of C/C++/ASM/Fortran/Go/Java/Python/Scala source code to the Kunpeng (ARM64) platform using Huawei DevKit CLI, with workflows for SSH access, DevKit installation, source scanning, report generation, and optional Kunpeng ECS provisioning on Huawei Cloud.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to assess whether application source code can migrate to Huawei Kunpeng ARM64 systems, run Huawei DevKit source migration scans, and collect migration assessment reports. It supports existing SSH-accessible servers, local supported Linux installs, or user-confirmed Huawei Cloud Kunpeng ECS provisioning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can provision paid Huawei Cloud infrastructure.

Mitigation: Require explicit user confirmation before provisioning, show the planned resource scope, and remind the user to delete or manage resources after the assessment.

Risk: The skill can use SSH access to run commands on a target server.

Mitigation: Use a disposable test server or a non-root account where practical, verify each install or scan command before execution, and limit activity to DevKit assessment tasks.

Risk: SSH secrets may persist temporarily in environment files or process state.

Mitigation: Provide credentials only through environment variables or protected temp files, avoid echoing secrets, remove temp credential files when finished, and rotate credentials after use.

Risk: DevKit installation and scans may install packages or inspect source code paths.

Mitigation: Confirm the source code path before any upload or scan, keep the assessment read-only for source code, and review package installation commands before running them.

## Reference(s):

- [Kunpeng Source Code Migration Assessment](artifact/SKILL.md)
- [Prerequisites](artifact/references/prerequisites.md)
- [Task 0: Detect Local OS and Prepare Environment](artifact/references/task-prepare-server.md)
- [Task 1: Connect to Source Code Server via SSH](artifact/references/task-connect-server.md)
- [Task 2: Install DevKit CLI Tool](artifact/references/task-install-devkit.md)
- [Task 3: Scan Source Code and Generate Migration Report](artifact/references/task-scan-source-code.md)
- [Migration Report Interpretation Guide](artifact/references/migration-report-guide.md)
- [Verification Method - Kunpeng Source Code Migration Assessment](artifact/references/verification-method.md)
- [Acceptance Criteria - Kunpeng Source Code Migration Assessment](artifact/references/acceptance-criteria.md)
- [IAM Permission Policies](artifact/references/iam-policies.md)
- [Huawei Cloud KooCLI Download](https://cn-north-4-hdn-koocli.obs.cn-north-4.myhuaweicloud.com/cli/latest/huaweicloud-cli-linux-amd64.tar.gz)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated migration report files from Huawei DevKit]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may be downloaded as HTML, JSON, CSV, or text depending on the selected DevKit report option.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
