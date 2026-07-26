## Description: <br>
Automates local download, extraction, configuration, startup, and URL reporting for JiuwenSwarm inside a Huawei Cloud development container. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to perform a standardized local JiuwenSwarm deployment in a Huawei Cloud development container, including runtime download, extraction, configuration, service startup, and access URL retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill downloads and runs a JiuwenSwarm runtime without evidence of pinned integrity verification. <br>
Mitigation: Install only in a disposable Huawei Cloud development container and prefer a release that pins and verifies the downloaded runtime before execution. <br>
Risk: The skill persists API configuration, including API key material, in a local .env file. <br>
Mitigation: Keep the container disposable, restrict file access, avoid printing or sourcing the .env file in shared terminals or logs, and rotate credentials after testing when appropriate. <br>
Risk: The skill can install global commands, start a long-running exposed service, and kill or replace local processes using selected port ranges. <br>
Mitigation: Review the planned writes and process changes before execution, run in an isolated environment, and avoid co-locating unrelated workloads in the same container. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-install-openjiuwenswarm) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Huawei Cloud CodeDao Skill Development Standards](https://developer.huawei.com/consumer/cn/doc/service/skill-development-standards-0000002592931546) <br>
- [Skill Information Security Review and Listing Review Standards](https://developer.huawei.com/consumer/cn/doc/service/skill-review-standards-0000002623371049) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Text] <br>
**Output Format:** [Markdown progress text, JSON error messages, shell command execution, and a final service URL] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs a five-phase local deployment flow and writes runtime configuration under the user's JiuwenSwarm config directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
