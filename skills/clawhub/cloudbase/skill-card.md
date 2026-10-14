## Description:

Guides developers through building, deploying, and troubleshooting Tencent CloudBase applications across web, mini-program, and mobile platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to plan, implement, deploy, and troubleshoot CloudBase apps, including authentication, databases, cloud functions, hosting, and AI integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deployment guidance may change the wrong CloudBase resources or rebuild the wrong directory.

Mitigation: Confirm the target site, EnvId, working directory, and deployment plan before execution; verify paths before any destructive rebuild.

Risk: Following bundled authentication examples literally may result in insecure apps.

Mitigation: Use verified JWT handling with no default signing secret, required issuer, audience, and expiration checks, and server-side secret storage.

## Reference(s):

- [CloudBase skill release on ClawHub](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase deployment workflow](artifact/references/deployment-workflow.md)
- [CloudBase MCP setup](artifact/references/mcp-setup.md)
- [CloudBase site onboarding](artifact/references/site-onboarding.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deployment and resource-change instructions require user review before execution.]

## Skill Version(s):

1.92.132 (source: ClawHub release; packaged skill frontmatter says 2.35.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
