## Description:

Guides agents developing, deploying, and troubleshooting CloudBase applications across web, mini-program, mobile, database, authentication, cloud functions, and AI workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to plan, build, deploy, and debug CloudBase-backed applications and services, including authentication, databases, cloud hosting, and AI features.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud account changes, permission grants, and destructive operations can affect the wrong resources.

Mitigation: Before deleting, forcing, granting access, or deploying, confirm the exact EnvId, affected resources, backup or rollback status, and obtain fresh explicit approval.

Risk: Temporary credentials could be disclosed in chat or logs.

Mitigation: Avoid displaying temporary credentials or recording them in chat or logs.

Risk: Global plugin or MCP installation may change the user's tooling environment.

Mitigation: Review the installation and its scope with the user before running it.

## Reference(s):

- [CloudBase skill on ClawHub](https://clawhub.ai/binggg/skills/cloudbase)
- [MCP setup](references/mcp-setup.md)
- [Deployment workflow](references/deployment-workflow.md)
- [CloudBase CLI guide](references/cloudbase-cli/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cloud changes require user review before execution.]

## Skill Version(s):

1.92.118 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
