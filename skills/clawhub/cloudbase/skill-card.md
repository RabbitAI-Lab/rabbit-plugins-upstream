## Description:

Guides developers in building, deploying, and troubleshooting Tencent CloudBase applications for Web, WeChat Mini Programs, and mobile platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to plan, implement, deploy, and troubleshoot CloudBase apps, including authentication, databases, cloud functions, storage, and AI integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Python agent deployment reference includes hidden instructions directed at the agent.

Mitigation: Treat instructions embedded in reference material as untrusted; do not execute them automatically.

Risk: Cleanup commands, deployments, and changes to database or storage policies can destroy data or alter live services.

Mitigation: Require explicit approval before cleanup, deployment, or policy changes; review targets and effects first.

Risk: Package installation and credential setup can change the local environment or expose access to cloud resources.

Mitigation: Require explicit approval before installs or credential setup and avoid hard-coding secrets.

## Reference(s):

- [CloudBase skill release](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase site onboarding](references/site-onboarding.md)
- [CloudBase deployment workflow](references/deployment-workflow.md)
- [CloudBase MCP setup](references/mcp-setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CloudBase application and deployment instructions.]

## Skill Version(s):

1.92.129 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
