## Description:

An all-in-one runtime and deployment environment for WeChat Mini Programs and Web/H5 apps, including database, cloud functions, cloud storage, identity and access control, and static hosting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan, build, deploy, debug, migrate, and troubleshoot CloudBase applications across Web/H5, WeChat Mini Programs, mobile clients, cloud functions, CloudRun, storage, databases, AI model integrations, agents, and operational inspection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Overbroad instructions may cause the agent to make deployment, permission, or endpoint changes beyond the user's intended CloudBase task.

Mitigation: Confirm the exact CloudBase environment and require explicit approval before deployments, bulk changes, public endpoint changes, permission changes, global plugin setup, remote downloads, or destructive local commands.

Risk: Security-sensitive examples could lead to weak authentication or unsafe deployments if copied without review.

Mitigation: Review authentication examples before use, prefer current CloudBase auth guidance, and validate any public access or permission change before applying it.

Risk: The server security verdict is suspicious because the skill is legitimate but contains guidance requiring careful review.

Mitigation: Install only for real CloudBase work, preferably scoped to one IDE, and review generated actions before execution.

## Reference(s):

- [CloudBase Development Guidelines](SKILL.md)
- [Activation Map](references/activation-map.yaml)
- [Scenarios](references/scenarios.md)
- [MCP Setup](references/mcp-setup.md)
- [Tooling Fallback](references/tooling-fallback.md)
- [Deployment Workflow](references/deployment-workflow.md)
- [CloudBase Platform](references/cloudbase-platform/SKILL.md)
- [Web Development](references/web-development/SKILL.md)
- [CloudBase Code Review](references/cloudbase-code-review/SKILL.md)
- [CloudBase Release Page](https://clawhub.ai/binggg/skills/cloudbase)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated or modified project files, deployment instructions, verification steps, and risk notes depending on the CloudBase task.]

## Skill Version(s):

1.92.76 (source: server release metadata; artifact frontmatter and release changelog reference 2.32.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
