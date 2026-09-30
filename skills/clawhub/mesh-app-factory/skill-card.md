## Description:

Helps developers build and manage end-to-cloud applications on the Mesh platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyinmind](https://clawhub.ai/user/flyinmind)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and administrators use this skill to create Mesh services and client interfaces, install or update services, and administer Mesh servers and clusters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill supports high-impact Mesh server and cluster administration.

Mitigation: Require explicit approval before SSH access, autostart changes, service removal, or remote cluster operations.

Risk: Administrative workflows may expose company passwords, TOTP values, or other credentials to an agent.

Mitigation: Enter secrets yourself in a trusted terminal or use a safer secret prompt; never provide them directly to the agent.

Risk: Installation steps may run downloaded helper scripts or expose an account with a default admin password.

Mitigation: Review downloaded scripts before execution and rotate the default admin password before exposing the service.

## Reference(s):

- [Mesh app factory on ClawHub](https://clawhub.ai/flyinmind/skills/mesh-app-factory)
- [MeshServer documentation and releases](https://gitee.com/zhijian_net/MeshServer)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include service definitions, UI code, and deployment steps.]

## Skill Version(s):

1.1.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
