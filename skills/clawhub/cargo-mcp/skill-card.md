## Description:

Helps agents connect to Cargo's hosted MCP server, choose between Cargo MCP and CLI workflows, discover and price actions, run single or batch actions, poll runs, and read workspace models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent users use this skill to configure Cargo's hosted MCP endpoint and operate Cargo actions from MCP-capable clients. It is intended for one-shot execution, action discovery, pricing, batch polling, and model reads while routing platform-building workflows to the Cargo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent may connect to the wrong Cargo workspace and read or act on plausible but incorrect business data.

Mitigation: Open each session with whoami, name the workspace back to the user, and stop if the workspace is not the intended one.

Risk: Cargo actions can spend workspace credits, especially during batch execution.

Mitigation: Use search_actions to inspect pricing, run a 10-20 record sample when applicable, report observed cost and hit rate, and obtain approval before a full batch run.

Risk: Authentication tokens can expose workspace-scoped Cargo capabilities if copied into configuration or logs.

Mitigation: Use OAuth-capable clients where possible or load workspace-scoped API tokens from environment variables rather than inlining token values.

Risk: Actions involving people data can create privacy, consent, or outreach misuse risk.

Mitigation: Require a lawful basis, suppression checks, and job-relevant use; refuse bulk unsolicited messaging, purchased or scraped lists, and consumer targeting.

## Reference(s):

- [Cargo hosted MCP endpoint](https://mcp.getcargo.io/mcp)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo-mcp)
- [Cargo publisher profile](https://clawhub.ai/user/cargo-ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP client configuration, Cargo action selection guidance, pricing and approval summaries, batch status summaries, and links to batch outputs.]

## Skill Version(s):

1.0.1 (source: frontmatter, skill-metadata.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
