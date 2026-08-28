## Description:

Guides agents through CloudBase project design, implementation, deployment, debugging, operations, and scenario-specific routing across Web, mini program, serverless, database, AI, and CloudRun work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route CloudBase work to the right local reference, prepare resources, implement app and backend changes, deploy through CloudBase MCP or CLI paths, and verify CloudBase projects before handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad CloudBase account and environment actions, including login, environment binding, public route changes, deletion, remote downloads, and deployments.

Mitigation: Keep human confirmation enabled for plugin or MCP installation, account login, environment binding, public route changes, database or schema deletion, remote downloads, and deployments; resolve aliases to full EnvId values before use.

Risk: Copied CloudBase examples may need production hardening for auth, CORS, logging, telemetry, storage, and security rules.

Mitigation: Review and harden auth, CORS, logging, telemetry, storage permissions, and database security rules before production use.

## Reference(s):

- [ClawHub CloudBase skill page](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase Development Guidelines](SKILL.md)
- [Activation routing map](references/activation-map.yaml)
- [Deployment workflow](references/deployment-workflow.md)
- [CloudBase MCP setup](references/mcp-setup.md)
- [Tooling fallback](references/tooling-fallback.md)
- [Scenario mapping](references/scenarios.md)
- [Console links](references/console-links.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline code, shell commands, configuration snippets, and implementation changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenario-routed output may include project file edits and CloudBase management or deployment steps when appropriate.]

## Skill Version(s):

1.92.75 (source: ClawHub release metadata; artifact frontmatter reports 2.32.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
