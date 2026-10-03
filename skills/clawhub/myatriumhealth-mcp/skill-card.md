## Description:

Helps users read their own MyAtriumHealth test results, medications, allergies, visits, and other records through a signed-in Chrome tab using shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Patients and developers use this skill to retrieve and filter their own MyAtriumHealth records in scripts without running the separate MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The paired shell can read sensitive medical records from the signed-in portal.

Mitigation: Use only on a trusted, single-user machine; avoid shared terminals and CI, and limit what you display or share.

Risk: The browser pairing persists and an exported antiforgery token remains available in the shell session.

Mitigation: Clear MAH_TOKEN when finished and revoke or remove the fpx/bridge pairing when no longer needed.

Risk: An expired session may return a login page with HTTP 200 or empty JSON, obscuring missing results.

Mitigation: Check the signed-in session when results are unexpectedly empty, then sign in again if necessary.

## Reference(s):

- [ClawHub release](https://clawhub.ai/chrischall/skills/myatriumhealth-mcp)
- [MyAtriumHealth endpoint recipes](references/endpoints.md)
- [MyAtriumHealth shell helpers](references/mah.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Shell examples and JSON responses from the patient's portal]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses can contain sensitive personal health information; filter results before displaying or sharing.]

## Skill Version(s):

1.3.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
