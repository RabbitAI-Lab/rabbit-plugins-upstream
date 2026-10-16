## Description:

Guides agents developing, deploying, and troubleshooting Tencent CloudBase applications across web, WeChat Mini Programs, mobile, databases, cloud functions, and AI integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to plan, build, deploy, and troubleshoot CloudBase-backed web, mini-program, and mobile applications, including authentication, data, hosting, and cloud services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hidden AI-directed deployment instructions may prompt unintended changes.

Mitigation: Review skill instructions and proposed commands before allowing the agent to execute them.

Risk: Cloud deployments, deletions, plan changes, or broad permission grants can affect live resources.

Mitigation: Require explicit confirmation before deploying, deleting ./env, changing plans, or attaching CAM policies.

Risk: Observability tools may expose requests, prompts, tokens, or personal data.

Mitigation: Redact sensitive content before sending telemetry to Sentry or other observability services.

Risk: Plugin installation and local configuration changes may alter the user's environment.

Mitigation: Require confirmation before installing plugins or writing local configuration files.

## Reference(s):

- [ClawHub CloudBase release](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase MCP setup](artifact/references/mcp-setup.md)
- [CloudBase deployment workflow](artifact/references/deployment-workflow.md)
- [CloudBase tooling fallback](artifact/references/tooling-fallback.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide changes to local configuration or cloud resources; review before execution.]

## Skill Version(s):

1.92.139 (source: ClawHub release; packaged skill frontmatter: 2.35.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
