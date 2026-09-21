## Description:

Create and manage DevBridge development tunnels on Huawei Cloud to expose local development services to remote devices through Huawei Cloud IAM-authenticated tunnel workflows.

This skill is for research and development only.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install and configure the DevBridge CLI, create temporary Huawei Cloud development tunnels, manage tunnel ports, and share local services for debugging, testing, or short-lived collaboration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or update the DevBridge CLI by running remote installer commands.

Mitigation: Require explicit approval before installer execution, verify the installer source, and review the resulting CLI path and version before continuing.

Risk: The skill can use Huawei Cloud credentials and local DevBridge authentication state.

Mitigation: Use interactive login or short-lived credentials where possible, never hardcode AK/SK values, avoid logging tokens, and clear credentials on shared machines.

Risk: The skill can expose local services over a public relay and may allow anonymous access.

Mitigation: Approve the selected local port and service before hosting, prefer authenticated access, and do not tunnel admin panels, debug endpoints, credential stores, private directories, or sensitive project files.

Risk: The skill can start long-running host or local file-serving processes in the background.

Mitigation: Approve background host processes, track their process IDs and log locations, and stop them when the tunnel is no longer needed.

Risk: The skill can delete individual tunnels or all workspace tunnels.

Mitigation: Require explicit approval for destructive tunnel operations, list affected resources first, and avoid delete-all unless the workspace scope is understood.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Permission Policies and Authentication](references/iam-policies.md)
- [CLI Command Reference](references/cli-command-reference.md)
- [REST API Reference](references/rest-api-reference.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Troubleshooting Guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, CLI output snippets, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands to install DevBridge CLI, authenticate to Huawei Cloud, create tunnels and ports, host local services, connect remote devices, and clean up tunnel resources.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
