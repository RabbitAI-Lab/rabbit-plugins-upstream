## Description:

Manage Huawei Cloud ModelArts training jobs and related resources through the hcloud CLI across training job, algorithm, experiment, model import, auto search, event, tag, and image-save operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect and manage Huawei Cloud ModelArts training jobs, algorithms, experiments, imported models, hyperparameter search, events, tags, and image-save tasks. It is intended for workflows where an agent proposes or executes hcloud CLI commands after credential, known-issue, pricing, and user-confirmation checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through powerful Huawei Cloud ModelArts operations that create, delete, stop, authorize, or write cloud resources using real credentials.

Mitigation: Use a least-privilege IAM user, prefer read-only permissions until write access is needed, avoid combined wildcard policies, and review every create, delete, stop, agency, or storage-write action before approval.

Risk: Credential handling could expose Huawei Cloud AK/SK values if secrets are pasted into chat, command lines, generated SDK code, or inspected from credential files.

Mitigation: Configure credentials outside the agent session, use presence-only checks such as hcloud configure list, and do not paste, print, echo, or read AK/SK values in the agent workflow.

Risk: Chargeable training operations may create cloud costs when using public resource pools or training experiments.

Mitigation: Perform the documented BSS pricing inquiry before chargeable write operations and include pricing information in the user confirmation step.

Risk: Installer and CLI workflows may introduce supply-chain or command-execution risk.

Mitigation: Verify any CLI installer before running it and review generated shell commands before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-modelarts-training-management)
- [Huawei Cloud hcloud CLI documentation](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud ModelArts console](https://console.huaweicloud.com/modelarts/)
- [CLI command examples](references/cli-command-examples.md)
- [BSS pricing inquiry](references/pricing-inquiry.md)
- [IAM policies](references/iam-policies.md)
- [Known issues and workarounds](references/known-issues.md)
- [Verification method](references/verification-method.md)
- [API paths](references/api-paths.md)
- [Data flow diagram](references/dataflow-diagram.md)
- [CLI installation guide](references/cli-installation-guide.md)
- [Acceptance criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and console URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose hcloud CLI calls, pricing checks, IAM guidance, credential setup guidance, and ModelArts console links; write operations require user confirmation.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
