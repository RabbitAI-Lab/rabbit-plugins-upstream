## Description:

Drive Cargo through its hosted MCP server to connect clients, discover and price actions, execute single or batch runs, poll results, and read workspace models without installing a CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to connect Cargo's hosted MCP server to clients such as Claude Desktop, ChatGPT, Cursor, or headless agents, then choose the right Cargo tool for action discovery, execution, polling, and workspace model reads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Package metadata may install a mutable local npm CLI even though hosted MCP use is described as not requiring a CLI.

Mitigation: Review install behavior before installation; prefer a pinned CLI version or an optional, user-approved CLI install path for hosted MCP-only use.

Risk: Cargo actions can spend workspace credits or operate on the wrong workspace if authentication is mis-scoped.

Mitigation: Open sessions with a workspace check, price actions before execution, sample small batches before full runs, and require user approval before bulk spending.

Risk: Actions involving personal data can create consent, suppression, or targeting concerns.

Mitigation: Confirm lawful basis, suppression checks, and job relevance before sourcing, enriching, or contacting people; refuse bulk unsolicited messaging, purchased or scraped lists, and consumer targeting.

## Reference(s):

- [Cargo hosted MCP endpoint](https://mcp.getcargo.io/mcp)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [ClawHub cargo-mcp page](https://clawhub.ai/cargo-ai/skills/cargo-mcp)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown with inline shell and JSON configuration blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP client connection guidance, Cargo tool selection advice, cost and workspace checks, and summarized run results.]

## Skill Version(s):

1.0.3 (source: server release metadata, SKILL.md frontmatter, skill-metadata.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
