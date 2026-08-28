## Description: <br>
Installs, configures, starts, and reports the access URL for JiuwenSwarm inside a Huawei Cloud development container. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to deploy or recover JiuwenSwarm locally inside a Huawei Cloud development container. It covers mirror download, extraction, runtime configuration, service startup, and web URL reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill has privileged local side effects, including dependency installation, global command creation, service startup, and stop or restart behavior. <br>
Mitigation: Require explicit confirmation before package installation, global command changes, service start, service stop, or restart operations. <br>
Risk: The skill reads Huawei Cloud credentials and persists configuration values to a local .env file. <br>
Mitigation: Use least-privilege credentials, verify the .env file permissions, and remove persisted credentials when the deployment is no longer needed. <br>
Risk: The skill downloads and runs an external runtime package. <br>
Mitigation: Review the runtime source and verify downloaded artifacts before running the extracted service. <br>
Risk: The startup flow can terminate processes listening on JiuwenSwarm-related ports. <br>
Mitigation: Inspect listening processes and affected ports before allowing stop, restart, or cleanup operations. <br>


## Reference(s): <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with shell command snippets, JSON error objects, and a final plain-text access URL.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs a five-phase local deployment flow and may update local runtime configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
