## Description: <br>
Choose and create the right Neon branch type for testing and development, including normal branches, schema-only branches, reset-from-parent workflows, and branch lifecycle guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andrelandgraf](https://clawhub.ai/user/andrelandgraf) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to choose Neon database branch strategies for migration testing, sensitive-data workflows, isolated development, branch resets, and CI/CD branch lifecycles. It guides agents toward CLI-first branch creation, with MCP or API fallbacks when the CLI is unavailable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Creating or resetting the wrong Neon branch can affect the wrong project, parent branch, or test environment. <br>
Mitigation: Confirm the Neon project, parent branch, branch type, and expiration date before running branch creation or reset commands. <br>
Risk: Connection strings and local `.env` values are sensitive secrets. <br>
Mitigation: Treat connection strings as secrets and update a local environment file only after confirming the exact file and key to change. <br>
Risk: Reset-from-parent replaces child branch schema and data with the parent state. <br>
Mitigation: Use the preserve-under-name backup option when appropriate and confirm that branch changes can be discarded before reset. <br>


## Reference(s): <br>
- [Neon parent skill](https://neon.com/docs/ai/skills/neon/SKILL.md) <br>
- [Neon CLI quickstart](https://neon.com/docs/cli/quickstart.md) <br>
- [Neon MCP server](https://neon.com/docs/ai/neon-mcp-server.md) <br>
- [Neon branching](https://neon.com/docs/introduction/branching.md) <br>
- [Schema-only branching](https://neon.com/docs/guides/branching-schema-only.md) <br>
- [Reset from parent](https://neon.com/docs/guides/reset-from-parent.md) <br>
- [Branching with the Neon API](https://neon.com/docs/guides/branching-neon-api.md) <br>
- [Branch expiration](https://neon.com/docs/guides/branch-expiration.md) <br>
- [Neon GitHub integration](https://neon.com/docs/guides/neon-github-integration.md) <br>
- [Neon branching overview](https://neon.com/branching) <br>
- [Preview branches with Cloudflare](https://github.com/neondatabase/preview-branches-with-cloudflare) <br>
- [Preview branches with Vercel](https://github.com/neondatabase/preview-branches-with-vercel) <br>
- [Preview branches with Fly](https://github.com/neondatabase/preview-branches-with-fly) <br>
- [Neon schema diff GitHub Action](https://github.com/marketplace/actions/neon-schema-diff-github-action) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Neon CLI commands, MCP workflow guidance, API fallback guidance, and optional local environment update instructions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
