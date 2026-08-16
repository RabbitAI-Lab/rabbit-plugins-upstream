## Description:

Guides agents that develop, design, build, deploy, debug, migrate, or troubleshoot CloudBase projects across Web, WeChat Mini Programs, mobile, databases, cloud functions, CloudRun, storage, AI, operations, and specification workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill pack to route CloudBase work to the right local reference, prepare CloudBase resources, implement frontend or backend changes, deploy safely, and review security-sensitive CloudBase code paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation can steer agents into CloudBase-specific behavior during unrelated frontend or planning tasks.

Mitigation: Install and invoke the skill only for intentional CloudBase projects, and keep it out of generic project work.

Risk: The skill can guide changes to auth providers, permissions, roles, paid resources, public endpoints, and deployment settings.

Mitigation: Require explicit human review before applying security-sensitive or cost-affecting CloudBase changes.

Risk: Security-sensitive examples may be unsafe if copied without adaptation.

Mitigation: Review generated code for real token verification, trusted server-side ownership checks, narrow CORS allowlists, and safe secret handling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase)
- [Publisher profile](https://clawhub.ai/user/binggg)
- [CloudBase main skill](artifact/SKILL.md)
- [Activation map](artifact/references/activation-map.yaml)
- [CloudBase platform guide](artifact/references/cloudbase-platform/SKILL.md)
- [CloudBase code review guide](artifact/references/cloudbase-code-review/SKILL.md)
- [Web development guide](artifact/references/web-development/SKILL.md)
- [MCP setup guide](artifact/references/mcp-setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code blocks, command snippets, configuration examples, and file edits when used by an agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing implementation, deployment, debugging, and review guidance for CloudBase projects.]

## Skill Version(s):

1.92.57 (source: server release evidence; artifact frontmatter version 2.27.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
