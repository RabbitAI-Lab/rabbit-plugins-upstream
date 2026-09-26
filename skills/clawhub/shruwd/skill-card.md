## Description:

Track how a brand shows up in ChatGPT and Google AI Overviews answers, and act on the findings, through Shruwd's MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ilpr](https://clawhub.ai/user/ilpr)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing teams use this skill to connect an agent to a Shruwd workspace, configure brand visibility tracking, run measurement cycles, and read results for ChatGPT and Google AI Overviews presence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent actions can read from or modify a Shruwd workspace depending on the granted scope and user role.

Mitigation: Use read-only OAuth scope for reporting-only workflows and grant read/write only when workspace changes are intended.

Risk: API-key or local setups expose workspace access through SHRUWD_API_KEY.

Mitigation: Prefer hosted OAuth where possible, keep API keys out of prompts and logs, and revoke unused credentials in Shruwd.

Risk: Measurement results arrive over time and may be incomplete before a cycle closes.

Mitigation: Check cycle status before reporting visibility numbers and avoid presenting open-cycle results as final.

## Reference(s):

- [Shruwd homepage](https://shruwd.io)
- [Shruwd MCP server documentation](https://shruwd.io/docs/api/mcp-server)
- [Shruwd machine-readable documentation](https://shruwd.io/llms.txt)
- [Shruwd pricing](https://shruwd.io/pricing)
- [ClawHub skill page](https://clawhub.ai/ilpr/skills/shruwd)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with setup commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger MCP API calls to Shruwd when the configured agent uses the connected tools.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter says 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
