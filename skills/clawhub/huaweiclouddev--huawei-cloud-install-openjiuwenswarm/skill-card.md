## Description:

Installs and starts JiuwenSwarm in a local Huawei Cloud development container by downloading the runtime, configuring credentials, starting the service, and returning the workspace URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to deploy or restart JiuwenSwarm inside a Huawei Cloud development container through a standardized local workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs network downloads and package installation during local setup.

Mitigation: Review the scripts before installation and run them only in a disposable Huawei Cloud development container.

Risk: The skill reads local Huawei Cloud settings and keyring credentials and may create a local .env containing API_KEY.

Mitigation: Confirm credential scope before use, keep generated environment files restricted, and rotate credentials if exposure is suspected.

Risk: The skill may create global symlinks, modify system trust configuration, and terminate processes on JiuwenSwarm-like ports.

Mitigation: Use an isolated container, inspect affected paths and ports, and avoid running it on shared or persistent hosts.

Risk: The skill returns an externally reachable Huawei Cloud workspace URL for the started service.

Mitigation: Confirm workspace access controls and avoid processing sensitive data until the deployment is reviewed.

## Reference(s):

- [Acceptance Criteria](references/acceptance-criteria.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [JiuwenSwarm README](https://raw.gitcode.com/openJiuwen/jiuwenswarm/raw/main/README.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown progress text and a final service URL string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs local installation scripts that can download files, configure environment variables, start services, and return a Huawei Cloud workspace URL.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
