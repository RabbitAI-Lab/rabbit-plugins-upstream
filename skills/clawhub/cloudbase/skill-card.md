## Description:

Guides agents through developing, deploying, and troubleshooting Tencent CloudBase applications across web, WeChat Mini Program, and mobile platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to plan, build, deploy, and troubleshoot CloudBase applications, including authentication, databases, cloud functions, storage, and AI integrations.

### Deployment Geography for Use:

Global; choose the appropriate domestic or international CloudBase site for the target environment.

## Known Risks and Mitigations:

Risk: Environment deletion can bypass safety checks.

Mitigation: Require explicit confirmation of the exact environment and consequences; do not use DestroyEnv bypass or force flags without that authorization.

Risk: Cloud-management changes can alter permissions, data access, or public exposure.

Mitigation: Confirm role-policy grants, database and RLS changes, bucket and domain changes, and deployments before execution.

Risk: Credential disclosure or global plugin installation can affect accounts outside the project.

Mitigation: Obtain explicit approval before revealing credentials or installing a global plugin.

## Reference(s):

- [CloudBase skill release](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase MCP setup](references/mcp-setup.md)
- [CloudBase deployment workflow](references/deployment-workflow.md)
- [CloudBase site onboarding](references/site-onboarding.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cloud actions may require access to a selected CloudBase environment.]

## Skill Version(s):

1.92.120 (source: ClawHub release; bundled skill frontmatter: 2.34.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
