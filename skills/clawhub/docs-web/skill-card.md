## Description:

Provides guidance for building interactive MCP Apps with UI-resource registration, app lifecycle patterns, host integration, and framework setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zskbot](https://clawhub.ai/user/zskbot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scaffold or add interactive MCP App UIs to MCP servers, choose frontend patterns, register app tools and resources, and test host integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary identifies the package as a mixed bundle rather than a clean single-purpose skill.

Mitigation: Review the artifact file list before installation and use only the MCP App guidance when the intended task is MCP App development.

Risk: The artifact includes unrelated OpenShift and Terraform operational guidance that could affect cloud infrastructure if followed.

Mitigation: Require explicit human approval before following cloud or infrastructure commands from this bundle.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zskbot/skills/docs-web)
- [Server-Resolved Source Repository](https://github.com/zskbot/docs-web)
- [MCP Apps SDK Examples](https://github.com/modelcontextprotocol/ext-apps.git)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline TypeScript, shell, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing implementation guidance; does not itself execute generated commands.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
