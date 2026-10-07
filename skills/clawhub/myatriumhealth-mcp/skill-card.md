## Description:

Helps users read their MyAtriumHealth records, including test results, medications, allergies, and visits, through a signed-in Chrome tab and shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Patients and their authorized agents use this skill to retrieve and selectively summarize their own MyAtriumHealth records from a signed-in browser session without running a separate MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser bridge retains access to a signed-in MyAtriumHealth session.

Mitigation: Use only on a private device and remove the bridge profile or extension when access is no longer needed.

Risk: Raw API responses, shell output, and MAH_TOKEN can expose sensitive medical information.

Mitigation: Use a private, unrecorded terminal; limit output to the fields needed and protect the token and results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/myatriumhealth-mcp)
- [Endpoint recipes](references/endpoints.md)
- [Shell helpers](references/mah.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON projection examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Selected patient-record data may appear in command output; treat it as sensitive.]

## Skill Version(s):

1.3.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
