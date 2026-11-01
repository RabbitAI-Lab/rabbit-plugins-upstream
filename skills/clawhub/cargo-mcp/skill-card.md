## Description:

Drive Cargo from its hosted MCP server at https://mcp.getcargo.io/mcp — connect a client, discover and price an action, run it over one record or a batch, poll it, and read workspace models, with no CLI install. Also when to call an MCP tool instead of shelling out to `cargo-ai`. Triggers: "connect Cargo to Claude Desktop", "add Cargo to ChatGPT", "Cargo MCP server", "mcp.getcargo.io", "use Cargo without installing anything", "which Cargo tool do I call", "search_actions", "execute_action_batch", "MCP server is showing the wrong workspace". Tools: whoami, search_actions, get_action_schema, execute_action, execute_action_batch, get_run, query_models. Skip when: you have a shell and the job is a workflow, a project deploy, warehouse SQL, or a mailbox — use the CLI skills; when publishing an MCP server out of your own workspace or attaching one to a Cargo agent — use cargo-ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using an AI client connect to Cargo’s hosted MCP server to discover and price actions, run one-off or batch actions, and read workspace models. The skill also helps them choose between hosted MCP and the Cargo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The declared local CLI requirement may cause setup confusion for users expecting installation-free hosted MCP access.

Mitigation: For hosted MCP use, check why the installer requires a local CLI before accepting that dependency; use narrowly permissioned workspace credentials, verify the selected workspace, and review costs before approving batches.

## Reference(s):

- [Hosted Cargo MCP server](https://mcp.getcargo.io/mcp)
- [Cargo setup guide](https://github.com/getcargohq/cargo-skills)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advice and results depend on the connected Cargo workspace and the requested action.]

## Skill Version(s):

1.3.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
