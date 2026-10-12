## Description:

Guides developers through building, deploying, and troubleshooting Tencent CloudBase applications across web, mini-program, and mobile platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to plan, implement, deploy, and troubleshoot CloudBase-backed web, WeChat Mini Program, and mobile applications, including authentication, databases, cloud functions, hosting, and AI features.

### Deployment Geography for Use:

Global (confirm domestic or international CloudBase site and region before operating)

## Known Risks and Mitigations:

Risk: AI-directed deployment instructions may prompt consequential actions without sufficient review.

Mitigation: Review proposed actions and require explicit approval before installing plugins, logging in, binding environments, or creating, deploying, changing plans for, or deleting cloud resources.

Risk: Cleanup commands for Python agent deployment can delete local directories.

Mitigation: Confirm the working directory and exact cleanup target before allowing commands such as `rm -rf env/`.

Risk: Operations against the wrong CloudBase account, site, or environment can affect unintended resources.

Mitigation: Verify the domestic or international site and the canonical environment ID before each cloud operation.

## Reference(s):

- [ClawHub CloudBase skill listing](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase site onboarding](references/site-onboarding.md)
- [CloudBase MCP setup](references/mcp-setup.md)
- [CloudBase deployment workflow](references/deployment-workflow.md)
- [CloudBase tooling fallback](references/tooling-fallback.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CloudBase-specific guidance for domestic and international sites; verify the site and environment before deployment.]

## Skill Version(s):

1.92.131 (source: ClawHub release metadata; bundled skill frontmatter: 2.35.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
