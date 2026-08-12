## Description:

Helium 10 (helium10.com). Use this skill for ANY Helium 10 request — searching and reading data. Whenever a task involves Helium 10, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Helium 10 through an OOMOL-connected account, inspect live connector schemas, discover available read-only Helium 10 tools, and run verified tool calls through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the oo CLI and an OOMOL-connected Helium 10 account, so commands can fail or route data through an intermediary the user did not intend to use.

Mitigation: Install and authenticate the oo CLI only when the user intends to use OOMOL for Helium 10 access, and review the CLI install source and connected-account permissions before use.

Risk: Future write-capable or destructive Helium 10 actions could change or remove account data if invoked without review.

Mitigation: Confirm the exact payload and expected effect with the user before write actions, and require explicit approval for destructive actions.

Risk: Connector input or output schemas may change over time.

Mitigation: Fetch the live connector schema with `oo connector schema` before constructing each payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-helium10)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Helium 10 Homepage](https://www.helium10.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, API Calls, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before tool invocation; command responses include JSON data and execution metadata when run with --json.]

## Skill Version(s):

1.0.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
