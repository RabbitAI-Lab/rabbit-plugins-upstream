## Description:

Query or update Zola wedding-planning data from a shell using curl against mobile-api.zola.com without running the zola-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and advanced Zola users use this skill to inspect or modify wedding-planning records through authenticated mobile API curl recipes when they want shell or script access instead of MCP.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a long-lived Zola browser cookie and short-lived session tokens.

Mitigation: Use a dedicated secret store and avoid exposing tokens in shared terminals, logs, screenshots, or chat.

Risk: The skill includes live update and delete commands for personal wedding-planning data.

Mitigation: Verify IDs with fresh reads before writes or deletes, preserve full object state for read-modify-write endpoints, and manually confirm destructive changes.

## Reference(s):

- [Zola mobile-api endpoints](references/mobile-api-endpoints.md)
- [Zola mobile API](https://mobile-api.zola.com)
- [Zola website](https://www.zola.com)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline curl and jq shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses authenticated live API calls and expects callers to manage Zola refresh and session tokens.]

## Skill Version(s):

1.8.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
