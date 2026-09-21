## Description:

FastMoss MCP helps agents operate the FastMoss MCP connector through the OOMOL oo CLI for reading, creating, updating, and deleting FastMoss data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use this skill to inspect live FastMoss action schemas and run FastMoss product, creator, shop, video, live, advertising, agency, and market research workflows through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that could execute unverified code if run automatically.

Mitigation: Install the oo CLI only after vendor verification and explicit user approval; do not let an agent run curl|bash or irm|iex automatically.

Risk: Some FastMoss actions can change state or be destructive when tagged accordingly.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [FastMoss MCP homepage](https://www.fastmoss.com/zh)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fastmoss-mcp)
- [ClawHub publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON data from oo connector actions when commands are executed.]

## Skill Version(s):

1.0.0 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
