## Description: <br>
Neon routes agents to current guidance for Neon and Lakebase Postgres backend primitives, CLI or MCP setup, and branch-first development workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andrelandgraf](https://clawhub.ai/user/andrelandgraf) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to choose the right Neon capability, install or update Neon agent tooling, and follow Neon CLI, MCP, infrastructure-as-code, and branch-first workflows for app backends. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers for backend, database, storage, or AI gateway requests may route an agent to Neon guidance when the user intended another provider. <br>
Mitigation: Confirm that Neon, Lakebase Postgres, or a specific Neon primitive is in scope before applying setup guidance. <br>
Risk: Suggested npx, Neon CLI, or skill commands may install or update tooling, sometimes globally. <br>
Mitigation: Review commands and flags before running them, and prefer project-scoped installation when that matches the workspace policy. <br>
Risk: Neon link or checkout workflows can write Neon environment variables into local .env files. <br>
Mitigation: Use --no-env-pull or runtime environment injection when secrets should not be written to disk. <br>
Risk: Object Storage, Functions, and AI Gateway guidance covers public beta services with us-east-2 project availability requirements. <br>
Mitigation: Confirm project region and beta service availability before using those feature-specific instructions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/andrelandgraf/skills/neon) <br>
- [Neon documentation index](https://neon.com/docs/llms.txt) <br>
- [Neon agent skills registry](https://neon.com/.well-known/agent-skills) <br>
- [Neon CLI installation](https://neon.com/docs/cli/install.md) <br>
- [Connect Neon MCP clients](https://neon.com/docs/ai/connect-mcp-clients-to-neon.md) <br>
- [Neon TypeScript configuration reference](https://neon.com/docs/reference/neon-ts.md) <br>
- [Neon agent skills repository](https://github.com/neondatabase/agent-skills) <br>
- [Neon for agent platforms repository](https://github.com/neondatabase/neon-for-agent-platforms) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and TypeScript examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill advises checking current Neon documentation and may suggest Neon CLI, MCP, or skill installation commands.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
