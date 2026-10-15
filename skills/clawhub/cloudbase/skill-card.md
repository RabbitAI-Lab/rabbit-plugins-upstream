## Description:

Guides developers through building, deploying, and troubleshooting CloudBase applications across web, WeChat Mini Programs, and mobile platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to plan, implement, deploy, and debug CloudBase-backed applications, including authentication, databases, cloud functions, storage, and AI integrations.

### Deployment Geography for Use:

Global (domestic and international CloudBase sites have separate accounts and differing capabilities)

## Known Risks and Mitigations:

Risk: Broad agent instructions may lead to unintended deployment or authentication changes.

Mitigation: Review proposed changes and obtain approval before applying them to live environments.

Risk: A bundled NestJS AuthGuard example does not adequately validate tokens.

Mitigation: Require real token validation before using the example to protect routes.

Risk: Suggested rm -rf env/ or temporary-directory cleanup could remove needed files.

Mitigation: Confirm the exact target path and approve cleanup before running it.

Risk: Long-lived credentials in local configuration can be exposed.

Mitigation: Prefer scoped MCP/OAuth access over static secrets in local configuration.

## Reference(s):

- [CloudBase skill release](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase MCP setup](artifact/references/mcp-setup.md)
- [CloudBase deployment workflow](artifact/references/deployment-workflow.md)
- [CloudBase AI toolkit documentation](https://docs.cloudbase.net/ai/cloudbase-ai-toolkit/)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Steps and examples require project-specific review before execution.]

## Skill Version(s):

1.92.136 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
