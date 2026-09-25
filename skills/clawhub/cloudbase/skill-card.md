## Description:

Guides developers through building, deploying, and troubleshooting Tencent CloudBase applications across web, mini-program, and mobile platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to plan, implement, deploy, and diagnose CloudBase apps, including authentication, databases, cloud functions, hosting, and AI integrations. It is not intended for projects that do not use CloudBase.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation, deletion, deployment, or permission changes can alter local or cloud resources or expose services.

Mitigation: Review proposed changes and require explicit approval before carrying out these steps; grant only necessary permissions.

Risk: Copying the Coze authentication example into production can permit anonymous access or use a default JWT secret.

Mitigation: Require authentication and set a unique, securely stored JWT secret before production use.

Risk: Temporary STS credentials could be disclosed through chat or logs.

Mitigation: Keep credentials out of chat and logs, and limit token scope and lifetime.

Risk: Broad CORS settings or CloudBase permissions may expose data or services.

Mitigation: Restrict allowed origins, tokens, and resource permissions to the minimum needed.

## Reference(s):

- [CloudBase skill release](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase tooling setup](artifact/references/mcp-setup.md)
- [CloudBase deployment workflow](artifact/references/deployment-workflow.md)
- [CloudBase scenario guide](artifact/references/scenarios.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include deployment steps and troubleshooting recommendations.]

## Skill Version(s):

1.92.114 (source: ClawHub release; packaged skill frontmatter: 2.34.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
