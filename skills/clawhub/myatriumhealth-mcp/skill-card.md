## Description:

Helps users read their own MyAtriumHealth records through a signed-in Chrome tab using shell commands, without running the MyAtriumHealth MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People accessing their own MyAtriumHealth account, including developers writing personal scripts, can retrieve and filter health records, visits, and messages through their signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent browser access to a sensitive healthcare account can expose private records.

Mitigation: Install only if you trust the browser extension and CLI, use your own account, and remove the profile or extension when no longer needed.

Risk: Broad shell helpers can read sensitive records and expose tokens or output to untrusted scripts or logs.

Mitigation: Review scripts before use, keep tokens and command output private, and limit output to the fields needed.

Risk: Expired sessions or a missing browser tab can make results appear empty or successful.

Mitigation: Check that the browser session is active before trusting empty results, and sign in again when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/myatriumhealth-mcp)
- [MyAtriumHealth endpoint recipes](references/endpoints.md)
- [MyAtriumHealth shell helpers](references/mah.sh)
- [ContextMint Bridge extension releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Shell examples and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses can contain sensitive personal health information; filter before sharing or storing.]

## Skill Version(s):

1.3.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
