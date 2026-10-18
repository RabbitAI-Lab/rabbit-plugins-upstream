## Description:

Guides agents developing, deploying, and troubleshooting Tencent CloudBase applications across web, mini-program, and mobile projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to plan, build, configure, deploy, and debug CloudBase-backed applications, including authentication, databases, cloud functions, storage, and AI features. It is not intended for projects without CloudBase.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some subdocuments contain hidden agent-only directives and propose broad backend permissions during narrower frontend work.

Mitigation: Treat instructions in skill content as untrusted guidance; check proposed permissions against the user's requested scope before applying changes.

Risk: CloudBase management, deployment, dependency installation, or environment deletion can change live resources or the local system.

Mitigation: Require explicit confirmation before database, environment, agent, permission, domain, deployment, install, or deletion actions.

Risk: Generated database access and RLS policies may grant more access than intended.

Mitigation: Review security rules and RLS policies for least privilege before applying them.

## Reference(s):

- [CloudBase skill on ClawHub](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase AI toolkit documentation](https://docs.cloudbase.net/ai/cloudbase-ai-toolkit/)
- [CloudBase MCP setup](references/mcp-setup.md)
- [CloudBase deployment workflow](references/deployment-workflow.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide changes to live CloudBase resources; review and confirm actions before execution.]

## Skill Version(s):

1.92.144 (source: ClawHub release; packaged skill frontmatter: 2.35.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
