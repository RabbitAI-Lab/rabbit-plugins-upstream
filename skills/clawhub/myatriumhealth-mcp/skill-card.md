## Description:

Helps users read their own MyAtriumHealth records from a shell through a signed-in Chrome tab, including test results, medications, allergies, immunizations, health issues, visits, and goals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Patients and developers use this skill to retrieve their own MyAtriumHealth portal data in one-off shell queries or scripts without running a separate MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Raw command output may expose personal health information.

Mitigation: Avoid saving, logging, or sharing raw output; select only the fields needed.

Risk: The browser bridge retains trust after pairing and grants shell access to the signed-in account.

Mitigation: Install only if you intend to access your own data; review the CLI and bridge source or checksums before pairing.

Risk: An expired session or missing browser tab can yield empty or misleading results.

Mitigation: Check the signed-in session and reopen or reauthenticate the browser tab before relying on empty results.

## Reference(s):

- [MyAtriumHealth skill release](https://clawhub.ai/chrischall/skills/myatriumhealth-mcp)
- [Endpoint recipes](references/endpoints.md)
- [Shell helpers](references/mah.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return sensitive personal health information from the signed-in user's account.]

## Skill Version(s):

1.3.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
