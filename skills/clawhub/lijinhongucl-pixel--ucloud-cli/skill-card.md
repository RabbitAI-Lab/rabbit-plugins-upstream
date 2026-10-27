## Description:

Guides agents in using the UCloud CLI to manage cloud resources and deploy web applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lijinhongucl-pixel](https://clawhub.ai/user/lijinhongucl-pixel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage UCloud hosts, networks, IP addresses, load balancers, and databases, or to deploy web applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent can create, change, or delete live, billable cloud resources.

Mitigation: Use a limited-permission profile and review the exact resources, scope, and cost before each change.

Risk: Credentials or account data may be exposed in command output or chat.

Mitigation: Use existing profiles or approved login flows; mask keys, tokens, and sensitive account details in responses.

Risk: Ambiguous targets or defaults may affect the wrong project or incur unexpected charges.

Mitigation: Confirm the active profile, project, region, target IDs, and billing choices before provisioning or destructive actions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lijinhongucl-pixel/skills/ucloud-cli)
- [UCloud CLI quick start](https://docs.ucloud.cn/cli/intro)
- [UCloud CLI repository and documentation](https://github.com/ucloud/ucloud-cli)
- [UCloud API documentation](https://github.com/UCloudDoc-Team/api)
- [CLI usage guidance](references/cli-usage.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with tables and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes operations and resource details; omits or masks secrets in user-facing output.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
