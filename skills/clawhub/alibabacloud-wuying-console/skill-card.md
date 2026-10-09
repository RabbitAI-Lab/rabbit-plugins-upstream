## Description:

Helps a local agent query and manage Alibaba Cloud WUYING resources through official Aliyun CLI product plugins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Alibaba Cloud WUYING administrators use this skill to discover and run cloud-computer, browser, application delivery, user, policy, and session operations through the Aliyun CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential or token retrieval and remote command execution may expose secrets or affect managed devices.

Mitigation: Use a least-privilege Aliyun profile, redact credentials, and review exact targets before approving sensitive operations.

Risk: Deletes, resets, releases, rebuilds, and tenant security changes can disrupt service or remove resources.

Mitigation: Require explicit confirmation naming the operation and resolved targets; verify current state before execution and avoid automatic retries.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sdk-team/skills/alibabacloud-wuying-console)
- [Authentication and credential handling](references/authentication.md)
- [Least-privilege authorization](references/ram-policies.md)
- [Execution and confirmation rules](references/safety.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and reported API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports observed resource state separately from requested changes; redacts secrets from responses.]

## Skill Version(s):

0.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
