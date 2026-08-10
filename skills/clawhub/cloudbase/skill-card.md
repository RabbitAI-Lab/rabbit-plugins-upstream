## Description:

Guides agents through CloudBase development, deployment, debugging, migration, and troubleshooting for Web, WeChat Mini Program, mobile, backend, database, storage, AI, and operations workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route CloudBase project requests to focused local references and produce implementation, deployment, configuration, debugging, and review guidance for CloudBase-backed applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Production-facing examples may weaken authentication, expose endpoints, or leak stable identifiers if copied as written.

Mitigation: Review generated code before production use, require real JWT signature, issuer, audience, and expiry validation, and avoid logging or returning stable user identifiers unless strictly necessary.

Risk: The skill can guide account-level actions such as plugin or MCP installation, login, permission changes, public endpoint creation, deploys, and deletion of local build folders.

Mitigation: Require explicit user confirmation before those actions and review proposed CloudBase environment, permission, endpoint, and deployment changes before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase skill entry](artifact/SKILL.md)
- [Activation map](artifact/references/activation-map.yaml)
- [CloudBase scenarios](artifact/references/scenarios.md)
- [Deployment workflow](artifact/references/deployment-workflow.md)
- [MCP setup](artifact/references/mcp-setup.md)
- [Tooling fallback](artifact/references/tooling-fallback.md)
- [CloudBase pricing](https://cloud.tencent.com/document/product/876/75213)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown responses with code snippets, shell commands, configuration examples, and CloudBase console links when relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend account, permission, deployment, and endpoint changes that should be reviewed before execution.]

## Skill Version(s):

1.92.51 (source: ClawHub release evidence; artifact frontmatter lists 2.26.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
